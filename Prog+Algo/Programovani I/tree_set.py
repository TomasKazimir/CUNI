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
                    n = n.right_parent

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
                n = n.right_parent
            else:
                n = n.left_parent
        return False

    def inorder(self):
        """Prints values in the tree-set from smallest to biggest (='inorder')."""

        def inorder(root, s):
            if root is not None:
                inorder(root.left_parent, s)
                s.append(str(root.val))
                inorder(root.right_parent, s)
            return s

        return inorder(self.root, [])

if __name__ == "__main__":
    import random
    import math

    t = TreeSet()
    k = 16
    v = [i for i in range(k)]

    for i in range(1, round(math.log2(k))+2):
        for j in range(k//(2*i), k, k//(2*i)):
            t.add(v[j])

    print(*t.inorder())
    print(t.count(20, 40))

    def print_bst(root: Node, level: int = 0, prefix: str = "Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left or root.right:  # Print children if they exist
                print_bst(root.left, level + 1, "L--- ")
                print_bst(root.right, level + 1, "R--- ")
        else:
            print(" " * (level * 4) + prefix + "None")

    # print_bst(t.root)

    def PrintTree(root):
        def height(root):
            return 1 + max(height(root.left_parent), height(root.right_parent)) if root else -1

        nlevels = height(root)
        width = pow(2, nlevels + 1)

        q = [(root, 0, width, 'c')]
        levels = []

        while (q):
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left_parent, level + 1, x - seg, 'l'))
                q.append((node.right_parent, level + 1, x + seg, 'r'))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].val)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2]
                if n[3] == 'l':
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)

    print_bst(t.root)
    PrintTree(t.root)