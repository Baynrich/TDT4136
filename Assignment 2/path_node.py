class Path_Node():
    def __init__(self, position, parent, g, h, f):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f

    def get_pos(self):
        return self.position

    def get_x(self):
        return self.position[0]
    
    def get_y(self):
        return self.position[1]
    
    def get_parent(self):
        return self.parent

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def get_f(self):
        return self.f