import operator
from collections import defaultdict


# sort a dict by key and return a sorted list
def sort_key(dic, reverse=False):
    assert type(dic) in {dict, defaultdict}
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(0), reverse=reverse)
    return sorted_dic


# sort a dict by value and return a sorted list
def sort_val(dic, reverse=False):
    assert type(dic) in {dict, defaultdict}
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=reverse)
    return sorted_dic


# sort a dict by len of key and return a sorted list
def sort_len_key(dic, reverse=False):
    assert type(dic) in {dict, defaultdict}
    sorted_dic = sorted(dic, key=lambda k: len(k), reverse=reverse)
    return [(i, dic[i]) for i in sorted_dic]


# sort a dict by len of value and return a sorted list
def sort_len_val(dic, reverse=False):
    assert type(dic) in {dict, defaultdict}
    sorted_dic = sorted(dic, key=lambda k: len(dic[k]), reverse=reverse)
    return [(i, dic[i]) for i in sorted_dic]


if __name__ == '__main__':
    d = {"one": [(1, 3), (1, 4)], "two": [(1, 2), (1, 2), (1, 3)], "three": [(1, 1)]}
    d_1 = {(1, 2, 3, 4): 1, (1, 2): 2, (1, 2, 3, 4, 5): 3}
    print(sort_len_val(d))
    print(sort_len_key(d_1))
