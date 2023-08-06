from __future__ import unicode_literals

import subprocess

from vert_tree.base import BaseTreeDisplay
from vert_tree.common import Edge


class TerminalDisplay(BaseTreeDisplay):
    def __init__(self, test_terminal_width=True):
        self.test_terminal_width = test_terminal_width

    def _init_display(self, tree):
        if self.test_terminal_width:
            # support python 2/3
            terminal_width = int(subprocess.check_output(["stty", "size"]).split()[0])
            if tree.total_width > terminal_width:
                print("Error: tree width is {}, terminal width is {}".format(tree.total_width, terminal_width))
                return False
        return True

    def _print_vertices(self, level_verts, width):
        self._truncate_node_vals(level_verts)
        vertex_line = [" "] * width
        for vertex in level_verts:
            vertex_line[vertex.start : vertex.end] = vertex.node.val
        print(str("".join(vertex_line)))

    def _print_edges(self, level_edges, level, width, edge_spacing, lines_required):
        if not level_edges:
            return
        edge_lines = [[" "] * width for _ in range(lines_required)]
        for edge in level_edges:
            curr_level = 0
            curr_pos = edge.parent_pos
            if edge.direction == "/":
                while curr_level < lines_required:
                    curr_pos -= edge.get_step_width(edge_spacing, curr_pos - edge.child_pos)
                    edge_lines[curr_level][curr_pos] = edge.direction
                    curr_level += 1
            else:
                while curr_level < lines_required:
                    curr_pos += edge.get_step_width(edge_spacing, edge.child_pos - curr_pos)
                    edge_lines[curr_level][curr_pos] = edge.direction
                    curr_level += 1
        for line in edge_lines:
            print(str("".join(line)))
