def c_for(first, test, update):
    while test(first):
        yield first
        first = update(first)
