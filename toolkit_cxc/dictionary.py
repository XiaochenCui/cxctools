from copy import deepcopy


def remove_key(dic, key):
    """
    Make a deepcopy of dict, then del dict[key] if exist.

    :param dic: dict
    :param key:
    """
    dict_copy = deepcopy(dic)
    if key in dict_copy:
        del dict_copy[key]
    return dict_copy


def get_the_value(d: dict):
    """
    对于长度为1的dict，返回那个唯一的val

    Args:
        d:
    """
    val = list(d.values())[0]
    return val


def get_the_key(d: dict):
    """
    对于长度为1的dict，返回那个唯一的key

    Args:
        d:
    """
    val = list(d.keys())[0]
    return val


def dict_to_tuple(d: dict, *args):
    """
    将长度为1的dict转为tuple
    {a: b} -> (a, b)

    Args:
        d:
        *args:

    Returns:

    """
    return (get_the_key(d), get_the_value(d), *args)
