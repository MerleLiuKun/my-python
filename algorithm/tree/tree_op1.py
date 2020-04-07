"""
    列表之列表
"""

def binary_tree(r):
    return [r, [], []]

def get_left_child(r):
    return r[0]


def get_right_child(r):
    return r[1]

def set_root_val(r, val):
    r[0] = val

def get_root_val(r):
    return r[0]


def insert_left(r, branch):
    t = r.pop(1)
    if len(t) > 1:
        r.insert(1, [branch, t, []])
    else:
        r.insert(1, [branch, [], []])
    return r

def insert_right(r, branch):
    t = r.pop(2)
    if len(t) > 1:
        r.insert(2, [branch,[], t])
    else:
        r.insert(2, [branch, [], []])
    return r
