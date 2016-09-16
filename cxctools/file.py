import errno
import os


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred
    except TypeError as e:
        print(filename)
        print(type(filename))


# return a file object with open it.
# delete the old file if it exists.
def silent_create(filename):
    silent_remove(filename)
    f = open(filename, 'w+b')
    return f
