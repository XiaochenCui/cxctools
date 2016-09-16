class temp_context_manager(object):
    def __init__(self, old_object, new_object):
        self.new = new_object
        self.old = old_object
        self.old_code = eval(old_object)

    def __enter__(self):
        globals()[self.old] = self.new

    def __exit__(self, type, value, traceback):
        globals()[self.old] = self.old_code
