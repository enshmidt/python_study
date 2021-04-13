"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple
from collections import Counter


def major_and_minor_elem_old(inp: List) -> Tuple[int, int]:
    return *major(inp), *minor(inp)


def minor(inp: List):
    """The least common element is the element that appears fewer than other."""
    count_list = [inp.count(i) for i in inp]
    min_value = min(count_list)
    index_list = []
    for ind, value in enumerate(count_list):
        if value == min_value:
            index_list.append(ind)
    values = {inp[i] for i in index_list}
    return values


def major(inp: List):
    """The most common element is the element that appears more than inp // 2 times."""
    index_list = []
    for index, value in enumerate(inp):
        if inp.count(value) > len(inp)//2:
            index_list.append(index)
    values = [inp[i] for i in index_list]
    return set(values)


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    c = Counter(inp)
    dict_c = dict(c.most_common())
    max_repeat = max(dict_c.values())
    min_repeat = min(dict_c.values())
    list_of_min_items = [key for key, val in dict_c.items() if val == min_repeat]
    list_of_max_items = [key for key, val in dict_c.items() if val == max_repeat & val > len(inp)//2]
    return *list_of_max_items, *list_of_min_items


# inputV = [3, 2, 3]
# inputV2 = [2,2,1,1,1,2,2]
# inputV3 = [2,2,1,1,1,2,2,5,8,5,1,7,2,4]
