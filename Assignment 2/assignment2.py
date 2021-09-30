import math
from operator import attrgetter

from Map import Map_Obj


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



map = Map_Obj()



goal_pos = map.get_goal_pos()
start_pos = map.get_start_pos()
end_node = None
opens = []
closed = []


start_h = math.sqrt((goal_pos[0] - start_pos[0])**2 + (goal_pos[1] - start_pos[1])**2)
start_node = Path_Node(start_pos, None, 0, start_h, start_h)
opens.append(start_node)
while len(opens) > 0:
    current_node = min(opens,key=attrgetter('f'))
    opens.remove(current_node)
    closed.append(current_node)

    # First, check if we've won.
    if current_node.get_pos() == goal_pos:
        end_node = current_node
        break

    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        
        # If child already in closed list we skip
        if len([node for node in closed if (node.get_x() == current_node.get_x() + x) and (node.get_y() == current_node.get_y() + y) ]) > 0:
            #print('Node already closed')
            continue

        # If child not walkable we skip
        if(map.get_cell_value([current_node.get_x() + x, current_node.get_y() + y])) < 0:
            #print('Cell not walkable')
            continue

        # Find g value
        child_g = current_node.get_g() + 1
        child_from_opens = [node for node in opens if (node.get_x() == current_node.get_x() + x) and (node.get_y() == current_node.get_y() + y) ]
        if len(child_from_opens) > 0:
            if (child_g > child_from_opens[0].get_g()):
                #print('Cell already in opens with better g value')
                continue
            else:
                opens.remove(child_from_opens[0])

        # Calculate h(x) euclidian distance from child to end.
        child_h = math.sqrt((goal_pos[0] - current_node.get_x())**2 + (goal_pos[1] - current_node.get_y())**2)
        child_f = child_g + child_h
        opens.append(Path_Node([current_node.get_pos()[0] + x, current_node.get_pos()[1] + y ], current_node, child_g, child_h, child_f))

path = []
while(end_node != None and end_node.get_parent() != None):
    path.append(end_node.get_pos())
    end_node = end_node.get_parent()
path.append(end_node.get_pos())

map.show_map_with_path(path)