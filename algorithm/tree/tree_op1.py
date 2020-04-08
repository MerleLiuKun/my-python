"""
    列表之列表
"""
from typing import List


def binary_tree(val: int) -> List:
    return [val, [], []]


def get_left_child(r: List) -> List:
    return r[0]


def get_right_child(r: List) -> List:
    return r[1]


def set_root_val(r: List, val: int) -> None:
    r[0] = val


def get_root_val(r: List) -> int:
    return r[0]


def insert_left(r: List, branch: int) -> List:
    t = r.pop(1)
    if len(t) > 1:
        r.insert(1, [branch, t, []])
    else:
        r.insert(1, [branch, [], []])
    return r


def insert_right(r: List, branch: int) -> List:
    t = r.pop(2)
    if len(t) > 1:
        r.insert(2, [branch, [], t])
    else:
        r.insert(2, [branch, [], []])
    return r
