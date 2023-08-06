import unittest

from util import *
from vert_tree import TerminalDisplay


class TestTerminal(unittest.TestCase):
    def setUp(self):
        self.display = TerminalDisplay(False)

    def test_tree_1(self):
        root = create_tree_1()
        with captured_output() as (stdout, stderr):
            self.display.display_vert_tree(root, 4)
            output = stdout.getvalue().splitlines()
        assert output[0][4] == "a"
        assert output[2][2] == "b"
        assert output[2][6] == "c"
        assert output[1][3] == "/"
        assert output[1][5] == "\\"

    def test_tree_2(self):
        root = create_tree_2()
        with captured_output() as (stdout, stderr):
            self.display.display_vert_tree(root, 4)
            output = stdout.getvalue().splitlines()
        assert output[0][8] == "a"
        assert output[2][4] == "b"
        assert output[2][12] == "c"
        assert output[4][2] == "d"
        assert output[4][6] == "e"
        assert output[4][10] == "f"
        assert output[4][14] == "g"
        assert output[1][6] == "/"
        assert output[1][10] == "\\"
        assert output[3][3] == "/"
        assert output[3][5] == "\\"
        assert output[3][11] == "/"
        assert output[3][13] == "\\"

    def test_tree_3(self):
        root = create_tree_3()
        with captured_output() as (stdout, stderr):
            self.display.display_vert_tree(root, 4)
            output = stdout.getvalue().splitlines()
        assert output[0][16] == "a"
        assert output[2][8] == "b"
        assert output[2][24] == "c"
        assert output[4][4] == "d"
        assert output[4][12] == "e"
        assert output[4][20] == "f"
        assert output[4][28] == "g"
        assert output[6][2] == "h"
        assert output[1][12] == "/"
        assert output[1][20] == "\\"
        assert output[3][6] == "/"
        assert output[3][10] == "\\"
        assert output[3][22] == "/"
        assert output[3][26] == "\\"
        assert output[5][3] == "/"
