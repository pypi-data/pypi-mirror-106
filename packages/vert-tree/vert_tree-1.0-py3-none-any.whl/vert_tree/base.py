import abc
from collections import deque

import six
from vert_tree.common import Edge, Tree, Vertex


@six.add_metaclass(abc.ABCMeta)
class BaseTreeDisplay:
    @abc.abstractmethod
    def _init_display(self, tree):
        pass

    @abc.abstractmethod
    def _print_vertices(self, level_verts, width):
        pass

    @abc.abstractmethod
    def _print_edges(self, level_edges, level, width, edge_spacing):
        pass

    def display_vert_tree(self, root, edge_spacing=1):
        tree = Tree(root, edge_spacing)
        if not self._init_display(tree):
            return
        current_level, next_level = deque(), deque()
        distance_from_top, level_verts, level_edges = 0, [], []
        current_level.append(Vertex(root, distance_from_top, tree.left_width, tree.depth - 1, tree.total_width))
        while current_level:
            curr = current_level.popleft()
            level_verts.append(curr)
            next_edge_len = Edge.get_edge_length(curr.levels_below, edge_spacing)
            child_dis = distance_from_top + next_edge_len + 1
            if curr.node.left:
                child_pos = curr.position_from_left - pow(2, curr.levels_below)
                next_level.append(Vertex(curr.node.left, child_dis, child_pos, curr.levels_below - 1, tree.total_width))
                level_edges.append(Edge(distance_from_top + 1, curr.position_from_left, child_pos, "/"))
            if curr.node.right:
                child_pos = curr.position_from_left + pow(2, curr.levels_below)
                next_level.append(
                    Vertex(curr.node.right, child_dis, child_pos, curr.levels_below - 1, tree.total_width)
                )
                level_edges.append(Edge(distance_from_top + 1, curr.position_from_left, child_pos, chr(92)))
            if not current_level:
                self._print_vertices(level_verts, tree.total_width)
                self._print_edges(level_edges, curr.levels_below, tree.total_width, edge_spacing, next_edge_len)
                distance_from_top += next_edge_len + 1
                level_edges, level_verts = [], []
                current_level = next_level
                next_level = deque()

    def _truncate_node_vals(self, level_verts):
        for i in range(len(level_verts) - 1):
            left = level_verts[i]
            right = level_verts[i + 1]
            while left.does_overlap(right):
                longer = left.longer_val_node(right)
                longer.trim_val()
