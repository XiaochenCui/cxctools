class Node:
    def __init__(self, key=None, init_data=None, next_node=None):
        self.key = key
        self.data = init_data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return '{cls}: {key}--{data}'.format(cls=self.__class__.__name__,
                                             key=self.key,
                                             data=self.data)

    __str__ = __repr__


if __name__ == '__main__':
    temp = Node('he', 93)
    print(temp.get_data())
    print(temp)
