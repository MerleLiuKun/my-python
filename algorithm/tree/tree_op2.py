"""
    节点与引用
"""

from typing import Optional


class BinaryTree:
    def __init__(self, val: int):
        self.value = val
        self.left = None
        self.right = None

    def insert_left(self, val: int) -> None:
        t = BinaryTree(val)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def insert_right(self, val: int) -> None:
        t = BinaryTree(val)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t

    def get_root_value(self):
        return self.value

    def set_root_value(self, val: int):
        self.value = val

    def get_left_child(self) -> "BinaryTree":
        return self.left

    def get_right_child(self) -> "BinaryTree":
        return self.right


if __name__ == "__main__":
    r = BinaryTree(1)
    assert r.get_root_value() == 1
    assert r.get_left_child() is None

    r.insert_left(5)
    r.insert_left(3)
    assert r.get_left_child().get_left_child().get_root_value() == 5
