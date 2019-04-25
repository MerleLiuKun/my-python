"""
    归并排序

    优化手段：
    1. 对分组小于某阈值时，使用插入排序
    2.
"""


###################
#   基于递归的归并   #
###################

def divide_array(arr):
    """
    :param arr: 待排序数组
    :return: 排序完毕数组
    """
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2

    left = divide_array(arr[:middle])
    right = divide_array(arr[middle:])
    return merge(left, right)


def merge(l_arr, r_arr):
    """

    :param l_arr:
    :param r_arr:
    :return:
    """
    l_idx = r_idx = 0
    res = []
    while len(l_arr) > l_idx and len(r_arr) > r_idx:
        if l_arr[l_idx] < r_arr[r_idx]:
            res.append(l_arr[l_idx])
            l_idx += 1
        else:
            res.append(r_arr[r_idx])
            r_idx += 1

    res += l_arr[l_idx:]
    res += r_arr[r_idx:]

    return res


###################
#   基于循环的归并   #
###################


def loop_merge(arr):
    pass


def loop_merge_pass():
    pass


if __name__ == '__main__':
    array = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    print(divide_array(array))
