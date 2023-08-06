import math


class Vertex:
    def __init__(self, node, distance_from_top, position_from_left, levels_below, tree_width):
        self.node = node
        self.distance_from_top = distance_from_top
        self.position_from_left = position_from_left
        self.levels_below = levels_below
        self.tree_width = tree_width
        self.calculate_offset()

    def calculate_offset(self):
        self.offset = 0
        if len(self.node.val) > 1:
            self.offset = max(int(len(self.node.val) / 2), 1)
        self.start = max(0, self.position_from_left - self.offset)
        self.end = self.start + len(self.node.val)
        if self.end >= self.tree_width:
            self.trim_val()

    def trim_val(self):
        self.node.val = self.node.val[:-1]
        self.calculate_offset()

    def does_overlap(self, other_vertex):
        if (self.start <= other_vertex.start) and (self.end >= other_vertex.start):
            return True
        elif (other_vertex.start <= self.start) and (other_vertex.end >= self.start):
            return True
        return False

    def longer_val_node(self, other_vertex):
        if len(self.node.val) > len(other_vertex.node.val):
            return self
        else:
            return other_vertex


class Edge:
    def __init__(self, distance_from_top, parent_pos, child_pos, direction):
        self.distance_from_top = distance_from_top
        self.parent_pos = parent_pos
        self.child_pos = child_pos
        self.direction = direction

    @staticmethod
    def get_step_width(edge_spacing, distance):
        if edge_spacing >= distance:
            return max(int(math.ceil(float(distance) / 2)), 1)
        else:
            return edge_spacing

    @staticmethod
    def get_edge_length(levels_below, edge_spacing):
        distance = pow(2, levels_below)
        return max(1, int(distance / edge_spacing) - 1)


class Tree:
    def __init__(self, root, edge_spacing):
        self.edge_spacing = edge_spacing
        self.depth = self.get_max_depth(root)
        self.vertical_length = self.get_vertical_length()
        tree_width = self.get_tree_width(root, self.depth)
        self.left_width = tree_width[0] + 2
        self.right_width = tree_width[1]
        self.total_width = tree_width[2] + 4

    def get_tree_width(self, root, depth, left_width=0, right_width=0):
        if root.left:
            left_width = self.get_tree_width(root.left, depth - 1, left_width + pow(2, depth - 1), right_width)[0]
        if root.right:
            right_width = self.get_tree_width(root.right, depth - 1, left_width, right_width + pow(2, depth - 1))[1]
        return left_width, right_width, 1 + left_width + right_width

    def get_max_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))

    def get_vertical_length(self):
        total_length = 0
        for i in range(self.depth):
            if i == 0:
                total_length += 1
            else:
                total_length += 1 + Edge.get_edge_length(i, self.edge_spacing)
        return total_length


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
