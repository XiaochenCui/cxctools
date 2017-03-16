def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


def char_at(s, index):
    """
    Return the str[index] in int class.

    Args:
        s:
        index:
    Returns:
        value (int): the int value of s[index], -1 for IndexError.
    """
    if index < len(s):
        value = ord(s[index])
    else:
        value = -1
    return value
