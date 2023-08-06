import unittest

from util import *
from vert_tree.common import Edge, Tree, TreeNode, Vertex


class TestBase(unittest.TestCase):
    def test_tree_left_width(self):
        # left width is increased by two in Tree constructor to accomodate longer node vals in leftmost position
        assert Tree(create_tree_1(), 1).left_width == 4
        assert Tree(create_tree_2(), 1).left_width == 8
        assert Tree(create_tree_3(), 1).left_width == 16

    def test_tree_right_width(self):
        assert Tree(create_tree_1(), 1).right_width == 2
        assert Tree(create_tree_2(), 1).right_width == 6
        assert Tree(create_tree_3(False), 1).right_width == 14

    def test_tree_depth(self):
        assert Tree(create_tree_1(), 1).depth == 2
        assert Tree(create_tree_2(), 1).depth == 3
        assert Tree(create_tree_3(), 1).depth == 4
        assert Tree(create_tree_3(False), 1).depth == 4

    def test_tree_vertical_length(self):
        assert Tree(create_tree_1(), 1).vertical_length == 3
        assert Tree(create_tree_2(), 1).vertical_length == 7
        assert Tree(create_tree_3(), 1).vertical_length == 15
        assert Tree(create_tree_3(False), 1).vertical_length == 15
        # with arrow spacing = 2
        assert Tree(create_tree_1(), 2).vertical_length == 3
        assert Tree(create_tree_2(), 2).vertical_length == 5
        assert Tree(create_tree_3(), 2).vertical_length == 9
        # with arrow spacing = 4
        assert Tree(create_tree_1(), 4).vertical_length == 3
        assert Tree(create_tree_2(), 4).vertical_length == 5
        assert Tree(create_tree_3(), 4).vertical_length == 7

    def test_vertex_val_overlap(self):
        # vert_1 bound by 0
        vert_1 = Vertex(TreeNode("abc"), 0, 0, 0, 100)
        vert_2 = Vertex(TreeNode("def"), 0, 4, 0, 100)
        assert vert_1.start == 0
        assert vert_1.end == 3
        assert vert_2.start == 3
        assert vert_2.end == 6
        assert vert_1.does_overlap(vert_2) == True
        # no longer bound
        vert_1 = Vertex(TreeNode("abc"), 0, 2, 0, 100)
        vert_2 = Vertex(TreeNode("def"), 0, 6, 0, 100)
        assert vert_1.start == 1
        assert vert_1.end == 4
        assert vert_2.start == 5
        assert vert_2.end == 8
        assert vert_1.does_overlap(vert_2) == False
        vert_1 = Vertex(TreeNode("abc"), 0, 2, 0, 100)
        vert_2 = Vertex(TreeNode("def"), 0, 0, 0, 100)
        assert vert_1.start == 1
        assert vert_1.end == 4
        assert vert_2.start == 0
        assert vert_2.end == 3
        assert vert_1.does_overlap(vert_2) == True
        vert_1 = Vertex(TreeNode("abc"), 0, 4, 0, 100)
        vert_2 = Vertex(TreeNode("def"), 0, 6, 0, 100)
        assert vert_1.start == 3
        assert vert_1.end == 6
        assert vert_2.start == 5
        assert vert_2.end == 8
        assert vert_1.does_overlap(vert_2) == True
        vert_1 = Vertex(TreeNode("abcdef"), 0, 4, 0, 100)
        vert_2 = Vertex(TreeNode("g"), 0, 5, 0, 100)
        assert vert_1.start == 1
        assert vert_1.end == 7
        assert vert_2.start == 5
        assert vert_2.end == 6
        assert vert_1.does_overlap(vert_2) == True
        vert_1 = Vertex(TreeNode("abcgh"), 0, 2, 0, 100)
        vert_2 = Vertex(TreeNode("def"), 0, 6, 0, 100)
        assert vert_1.start == 0
        assert vert_1.end == 5
        assert vert_2.start == 5
        assert vert_2.end == 8
        assert vert_1.does_overlap(vert_2) == True

    def test_step_width(self):
        assert Edge.get_step_width(4, 16) == 4
        assert Edge.get_step_width(4, 3) == 2
        assert Edge.get_step_width(4, 2) == 1
        assert Edge.get_step_width(4, 1) == 1

    def test_edge_length(self):
        # levels_below, edge_spacing
        assert Edge.get_edge_length(1, 1) == 1
        assert Edge.get_edge_length(2, 1) == 3
        assert Edge.get_edge_length(3, 1) == 7
        assert Edge.get_edge_length(4, 1) == 15
        # spacing = 2
        assert Edge.get_edge_length(1, 2) == 1
        assert Edge.get_edge_length(2, 2) == 1
        assert Edge.get_edge_length(3, 2) == 3
        assert Edge.get_edge_length(4, 2) == 7
        # spacing = 4
        assert Edge.get_edge_length(1, 4) == 1
        assert Edge.get_edge_length(2, 4) == 1
        assert Edge.get_edge_length(3, 4) == 1
        assert Edge.get_edge_length(4, 4) == 3

    def test_offset(self):
        assert Vertex(TreeNode("a"), 0, 10, 0, 100).offset == 0
        assert Vertex(TreeNode("ab"), 0, 10, 0, 100).offset == 1
        assert Vertex(TreeNode("abc"), 0, 10, 0, 100).offset == 1
        assert Vertex(TreeNode("abcd"), 0, 10, 0, 100).offset == 2
        assert Vertex(TreeNode("abcd"), 0, 10, 0, 100).start == 8
        # offset bound by 0
        assert Vertex(TreeNode("abcd"), 0, 2, 0, 100).start == 0
        assert Vertex(TreeNode("abcd"), 0, 1, 0, 100).start == 0
        assert Vertex(TreeNode("abcd"), 0, 0, 0, 100).start == 0
        # offset bound by width max
        assert Vertex(TreeNode("abcd"), 0, 98, 0, 100).start == 97
        assert Vertex(TreeNode("abcd"), 0, 98, 0, 100).node.val == "ab"
