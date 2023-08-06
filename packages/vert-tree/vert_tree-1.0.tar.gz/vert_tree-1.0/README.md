# vert_tree

This simple library displays conventional Python binary trees in an intuitive, vertical manner to either the terminal
or a curses pad (useful for large trees!).

A compatible Tree representation class:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

and example tree:

```python
root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
```

# terminal display

using our simple example tree, we can display it to terminal, attempt to mirror it, and display it again:

```python
from vert_tree import TerminalDisplay

def mirror(node):
    if (node == None):
        return
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp

terminal = TerminalDisplay()
terminal.display_vert_tree(root)
mirror(root)
print('after mirroring...')
terminal.display_vert_tree(root)
```

execution output:

```bash
$ python test.py
    a
   / \
  b   c
after mirroring...
    a
   / \
  c   b
```

# curses display

terminal display is restricted by the width of the current terminal. Should a tree be too large, it can be displayed
vertically in a curses pad instead.

the basic format is similar to our terminal display:

```python
from vert_tree import CursesDisplay
curses_display = CursesDisplay()
curses_display.display_vert_tree(root)
```
except when executed a curses window will allow for scrolling around the displayed tree. Arrow keys will move the screen
and 'q' will exit the window.

Additionally, a curses display can be configured to exit automatically after a number of seconds by passing a timeout
argument to the CursesDisplay constructor.

```
from vert_tree import CursesDisplay
curses_display = CursesDisplay(5)
curses_display.display_vert_tree(root)
```
in the above case the curses window will exit automatically after 5 seconds.

# arrow spacing

some trees with considerable depth may take up a lot of space if we print consistent edge lines. For example:

```bash
                                                       Ragnar
                                                         / \
                                                        /   \
                                                       /     \
                                                      /       \
                                                     /         \
                                                    /           \
                                                   /             \
                                                  /               \
                                                 /                 \
                                                /                   \
                                               /                     \
                                              /                       \
                                             /                         \
                                            /                           \
                                           /                             \
                                          /                               \
                                         /                                 \
                                        /                                   \
                                       /                                     \
                                      /                                       \
                                     /                                         \
                                    /                                           \
                                   /                                             \
                                  /                                               \
                                 /                                                 \
                                /                                                   \
                               /                                                     \
                              /                                                       \
                             /                                                         \
                            /                                                           \
                           /                                                             \
                      Lagertha                                                          Floki
                         / \                                                             / \
                        /   \                                                           /   \
                       /     \                                                         /     \
                      /       \                                                       /       \
                     /         \                                                     /         \
                    /           \                                                   /           \
                   /             \                                                 /             \
                  /               \                                               /               \
                 /                 \                                             /                 \
                /                   \                                           /                   \
               /                     \                                         /                     \
              /                       \                                       /                       \
             /                         \                                     /                         \
            /                           \                                   /                           \
           /                             \                                 /                             \
        Rollo                           Bjorn                         Gunnhild                          Ubbe
         /                                                                                               /
        /                                                                                               /
       /                                                                                               /
      /                                                                                               /
     /                                                                                               /
    /                                                                                               /
   /                                                                                               /
Harald                                                                                          Ivar
                                                                                                   \
                                                                                                    \
                                                                                                     \
                                                                                                  Hvitserk
                                                                                                     /
                                                                                                Torstein
```

by passing the arrow_spacing argument to either Terminal or Curses Displays, we can eliminate some of the depth by
spacing out the edge representations to only print slashes every 'n'  number of chars. For instance the same tree can be
displayed in a much more compact format:

```python
terminal.display_vert_tree(root, arrow_spacing=4)
```
output:
```bash
                                                       Ragnar
                                                      /       \
                                                  /               \
                                              /                       \
                                          /                               \
                                      /                                       \
                                  /                                               \
                              /                                                       \
                      Lagertha                                                          Floki
                      /       \                                                       /       \
                  /               \                                               /               \
              /                       \                                       /                       \
        Rollo                           Bjorn                         Gunnhild                          Ubbe
      /                                                                                               /
Harald                                                                                          Ivar
                                                                                                    \
                                                                                                  Hvitserk
                                                                                                     /
                                                                                                Torstein
```
# limitations

1) TerminalDisplay can only handle Trees that can fit within the current terminal screen width. If the tree is too wide
   it will exit.
2) CursesDisplay can handle LARGE trees (up to 32767x32767 on my system) but the underlying curses lib will eventually
   crash given a large enough tree.
2) TreeNode vals can be of any length, the displays will attempt to center them to the extent that they can. Any
   collision with the bounds of the display or other TreeNode val's will result in the longer val getting trimmed.
