from functools import partial
from utils_ak.simple_vector import *
from utils_ak.properties import *
from utils_ak.block_tree import Block

from utils_ak.clock import *


def x_cumsum_acc(parent, child, key, default=None, formatter=None):
    if parent:
        return parent[key].add(
            relative_acc(parent, child, key, default=default, formatter=formatter)
        )
    return SimpleVector(
        list(
            relative_acc(
                parent, child, key, default=default, formatter=formatter
            ).values
        )
    )


class ParallelepipedBlock(Block):
    def __init__(self, block_class, n_dims=2, **props):
        self.n_dims = n_dims

        if "x" not in props:
            props["x"] = SimpleVector(n_dims)
        if "size" not in props:
            props["size"] = SimpleVector(n_dims)

        self.size_cached = None

        super().__init__(
            block_class,
            props_formatters={
                "x": lambda k, v: SimpleVector([int(v[0]), int(v[1])]),
                "size": lambda k, v: SimpleVector([int(v[0]), int(v[1])]),
            },
            # props_cache_keys=["x"],
            **props,
        )

        self.props.accumulators["x"] = x_cumsum_acc
        self.props.accumulators[
            "x_rel"
        ] = lambda parent_props, child_props, key: relative_acc(
            parent_props, child_props, "x"
        )
        self.props.accumulators["size"] = relative_acc
        self.props.accumulators["axis"] = partial(relative_acc, default=0)
        self.props.accumulators["is_parent_node"] = partial(relative_acc, default=False)

    @property
    def x(self):
        return self.props["x"]

    @property
    def x_rel(self):
        return self.props["x_rel"]

    @property
    def y(self):
        return self.x + self.size

    @property
    def y_rel(self):
        return self.x_rel + self.size

    def add_child(self, block):
        super().add_child(block)
        self.size_cached = None

    def remove_child(self, block):
        super().remove_child(block)
        self.size_cached = None

    @property
    def size(self):
        if not self.size_cached:
            size = self.props["size"]
            values = []
            for axis in range(self.n_dims):
                if size[axis] == 0:
                    if not self.children:
                        values.append(0)
                    else:
                        start = min([c.x_rel[axis] for c in self.children] + [0])
                        values.append(
                            max([c.y_rel[axis] - start for c in self.children])
                        )
                else:
                    values.append(size[axis])
            self.size_cached = SimpleVector(values)
        return self.size_cached

    def to_dict(self, props=None, with_children=True):
        props = props or []

        res = {}
        res["cls"] = self.props["cls"]

        res["props"] = {}

        for prop in props:
            if isinstance(prop, str):
                res["props"][prop] = self.props.get(prop)

            elif isinstance(prop, dict):
                if "cls" not in prop or (
                    "cls" in prop and self.props["cls"] == prop["cls"]
                ):
                    key = prop["key"]
                    value = prop.get("value", key)
                    if isinstance(value, str):
                        res["props"][key] = self.props[key]
                    elif callable(value):
                        res["props"][key] = value(self)
                    else:
                        raise Exception("Value should be either callable or string")

        if with_children:
            res["children"] = [
                child.to_dict(props, with_children) for child in self.children
            ]
        return res

    def __str__(self):
        res = (
            self.props["cls"]
            + " "
            + " x ".join([f"({self.x[i]}, {self.y[i]}]" for i in range(self.n_dims)])
        )

        for child in self.children:
            for line in str(child).split("\n"):
                if not line:
                    continue
                res += "\n  " + line
        return res

    def __repr__(self):
        return self.tabular()

    def is_leaf(self):
        return not self.children and not self.props["is_parent_node"]

    def tabular(self):
        res = ""
        for b in self.iter():
            if b.size[0] != 0:
                res += (
                    " " * int(b.x[0])
                    + "=" * int(b.size[0])
                    + f' {b.props["cls"]} '
                    + " x ".join([f"({b.x[i]}, {b.y[i]}]" for i in range(b.n_dims)])
                )
                res += "\n"
        return res


def test_parallelepiped_block():
    a = ParallelepipedBlock("a", n_dims=2, x=[1, 2])
    b = ParallelepipedBlock("b", n_dims=2)
    c = ParallelepipedBlock("c", n_dims=2, x=[3, 4], size=[1, 5])
    a.add_child(b)
    b.add_child(c)

    print(a)
    print(b)
    print(c)
    print(a.x, a.size, a.y)
    print(b.x, b.size, b.y)
    print(c.x, c.size, c.y)

    print()
    print(a["b"]["c"])

    print(a.__repr__())

    print(a.to_dict())
    print(a.to_dict(["x", {"key": "size", "value": lambda b: list(b.props["size"])}]))


if __name__ == "__main__":
    test_parallelepiped_block()
