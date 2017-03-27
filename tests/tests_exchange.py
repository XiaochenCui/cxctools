from cxctools.exchange import exch


def test():
    l = ["a", "b", "c"]
    exch(l, 0, 2)
    assert l == ["c", "b", "a"]
