# it is a still needs accurately object needs dunder methods
class link(object):
    def __init__(self, obj):
        if obj[:3] == 'htt' and isinstance(obj, str):
            self.obj = obj

    def __str__(self):
        return self.obj

