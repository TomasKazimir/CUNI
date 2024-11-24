class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeSet:
    def __init__(self):
        self.root = None
        self._size = 0

    def add(self, x: int):
        """Adds `x` to the set if not already present."""
        n = self.root
        if n is None:
            self.root = Node(x)
            self._size = 1
            return

        while True:
            if n.val == x:
                return
            elif n.val > x:
                if n.left is None:
                    n.left = Node(x)
                    self._size += 1
                    return
                else:
                    n = n.left
            else:
                if n.right is None:
                    n.right = Node(x)
                    self._size += 1
                    return
                else:
                    n = n.right

    def remove(self, x: int):
        """Removes `x` from the tree-set if present."""
        self.root = self._remove(self.root, x)

    def _remove(self, n: Node, x: int) -> Node | None:
        """Recursively removes a node with the value `x` from the tree-set starting at the given node `n`."""
        if n is None:
            return None
        if x < n.val:
            n.left = self._remove(n.left, x)
        elif x > n.val:
            n.right = self._remove(n.right, x)
        elif x == n.val:
            if n.left == n.right is None:
                self._size -= 1
                return None
            if n.left is None:
                self._size -= 1
                return n.right
            if n.right is None:
                self._size -= 1
                return n.left
            s = self._min(n.right)
            n.val = s.val
            n.right = self._remove(n.right, s.val)
        return n

    def min(self) -> int | None:
        """Returns smallest value in the tree-set, None if empty."""
        if self.root is None:
            return None
        return self._min(self.root).val

    def _min(self, n: Node) -> Node:
        """Returns the smallest value node in the subtree `n`."""
        if n.left is None:
            return n
        return self._min(n.left)

    def max(self) -> int | None:
        """Returns biggest value in the tree-set, None if empty."""
        if self.root is None:
            return None
        return self._max(self.root).val

    def _max(self, n: Node) -> Node:
        """Returns the biggest value node in subtree `n`."""
        if n.right is None:
            return n
        return self._max(n.right)

    def size(self) -> int:
        """Returns number of values in the tree-set."""
        return self._size

    def count(self, lo: int, hi: int) -> int:
        """Returns number of values x in the tree-set such that lo <= x <= hi."""

        def rec_count(n) -> int:
            if n is None:
                return 0
            if n.val < lo:
                return rec_count(n.right)
            if n.val > hi:
                return rec_count(n.left)
            return 1 + rec_count(n.left) + rec_count(n.right)

        return rec_count(self.root)

    def contains(self, x: int) -> bool:
        """Returns True if `x` is present in the tree-set, False otherwise."""
        n = self.root
        while n is not None:
            if n.val == x:
                return True
            if n.val < x:
                n = n.right
            else:
                n = n.left
        return False

    def inorder(self):
        """Prints values in the tree-set from smallest to biggest (='inorder')."""

        def inorder(root, s):
            if root is not None:
                inorder(root.left, s)
                s.append(str(root.val))
                inorder(root.right, s)
            return s

        return inorder(self.root, [])


# import random
#
# t = TreeSet()
# v = [i for i in range(1, 101)]
#
# for _ in range(100):
#     x = random.choice(v)
#     v.remove(x)
#     t.add(x)
#
# print(*t.inorder())
# print(t.count(20, 40))
#
# def print_bst(root: Node, level: int = 0, prefix: str = "Root: "):
#     if root is not None:
#         print(" " * (level * 4) + prefix + str(root.val))
#         if root.left or root.right:  # Print children if they exist
#             print_bst(root.left, level + 1, "L--- ")
#             print_bst(root.right, level + 1, "R--- ")
#     else:
#         print(" " * (level * 4) + prefix + "None")
#
# # print_bst(t.root)