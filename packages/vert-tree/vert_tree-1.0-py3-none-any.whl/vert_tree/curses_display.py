import curses
import time

from vert_tree.base import BaseTreeDisplay
from vert_tree.common import Edge


class CursesDisplay(BaseTreeDisplay):
    def __init__(self, timeout=-1):
        self.timeout = timeout

    def _init_display(self, tree):
        self.height = tree.vertical_length
        self.width = tree.total_width
        try:
            self.pad = curses.newpad(self.height, self.width)
        except:
            print("The curses lib cannot handle a tree so large! Height: {} width: {}".format(self.height, self.width))
            return False
        # curses reads will block for only this time amount in millis
        self.pad.timeout(500)
        return True

    def _display_curses_tree(self, stdscr, root, edge_spacing):
        # TODO center on root?
        super(CursesDisplay, self).display_vert_tree(root, edge_spacing)
        if not hasattr(self, "pad"):
            return
        x = y = 0
        time_end = self._get_end_time()
        while time.time() < time_end:
            win_height, win_width = stdscr.getmaxyx()
            self.pad.refresh(y, x, 0, 0, win_height - 1, win_width - 1)
            char = self.pad.getch()
            if char == ord("q"):
                break
            elif char == curses.KEY_UP:
                y = max(y - 1, 0)
            elif char == curses.KEY_DOWN:
                y = min(y + 1, self.height - win_height)
            elif char == curses.KEY_RIGHT:
                x = min(x + 1, self.width - 1)
            elif char == curses.KEY_LEFT:
                x = max(x - 1, 0)

    def _get_end_time(self):
        if self.timeout >= 0:
            return time.time() + self.timeout
        return float("inf")

    def display_vert_tree(self, root, edge_spacing=1):
        curses.wrapper(self._display_curses_tree, root, edge_spacing)

    def _print_edges(self, level_edges, level, width, edge_spacing, lines_required):
        if not level_edges:
            return
        for edge in level_edges:
            curr_level = 0
            curr_pos = edge.parent_pos
            if edge.direction == "/":
                while curr_level < lines_required:
                    curr_pos -= edge.get_step_width(edge_spacing, curr_pos - edge.child_pos)
                    y = edge.distance_from_top + curr_level
                    self.pad.addch(y, curr_pos, edge.direction)
                    curr_level += 1
            else:
                while curr_level < lines_required:
                    curr_pos += edge.get_step_width(edge_spacing, edge.child_pos - curr_pos)
                    y = edge.distance_from_top + curr_level
                    self.pad.addch(y, curr_pos, edge.direction)
                    curr_level += 1

    def _print_vertices(self, level_verts, width):
        self._truncate_node_vals(level_verts)
        for vertex in level_verts:
            self.pad.addstr(vertex.distance_from_top, vertex.start, vertex.node.val)
