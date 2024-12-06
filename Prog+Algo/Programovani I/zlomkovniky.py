from math import gcd, log2


# region StandardFraction

class StandardFraction:
    def __init__(self, numerator, denominator):
        if (common_divisor := gcd(numerator, denominator)) != 1:
            numerator //= common_divisor
            denominator //= common_divisor
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "(" + str(self.numerator) + "/" + str(self.denominator) + ")"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        common_divisor = gcd(new_numerator, new_denominator)
        new_numerator //= common_divisor
        new_denominator //= common_divisor
        return StandardFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return StandardFraction(-self.numerator, self.denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __mul__(self, other):
        if type(other) == StandardFraction:
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return StandardFraction(new_numerator, new_denominator)
        if type(other) == int:
            return StandardFraction(self.numerator * other, self.denominator)

    def __truediv__(self, other):
        return self * StandardFraction(other.denominator, other.numerator)


# a = StandardFraction(1240, 180)
# b = StandardFraction(28, 180)
# c = StandardFraction(10, 3)
# print((a - b) * c)


# endregion

class MagicFraction:
    def __init__(self, numerator, denominator):
        # if (common_divisor := gcd(numerator, denominator)) != 1:
        #     numerator //= common_divisor
        #     denominator //= common_divisor
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        # if self.denominator == 1:
        #     return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator)
        # return "(" + str(self.numerator) + "/" + str(self.denominator) + ")"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        new_numerator = self.numerator + other.numerator
        new_denominator = self.denominator + other.denominator
        return MagicFraction(new_numerator, new_denominator)


class FracNode:
    def __init__(self, left, right, depth=0):
        self.parents = (left, right)
        self.value = left + right
        if depth == 0:
            self.left = None
            self.right = None
        else:
            self.left = FracNode(self.parents[0], self.value, depth - 1)
            self.right = FracNode(self.value, self.parents[1], depth - 1)


class FracTree:
    def __init__(self, left, right, depth):
        self.left_origin = left
        self.right_origin = right
        self.root = FracNode(left, right, depth)

    def inorder(self):
        """Prints values in the tree-set from smallest to biggest (='inorder')."""

        def inorder(root, s):
            if root is not None:
                inorder(root.left, s)
                s.append(str(root.value))
                inorder(root.right, s)
            return s

        return [self.left_origin] + inorder(self.root, []) + [self.right_origin]

    def inorder_row(self, depth):

        def inorder(root, s, d):
            if root is not None:
                inorder(root.left, s)
                s.append(str(root.value))
                inorder(root.right, s)
            return s

        return [self.left_origin] + inorder(self.root, []) + [self.right_origin]

    def grow(self):
        pass


def grow_fractree(tree, steps=1):
    new_tree = [tree[0]]
    for i in range(len(tree) - 1):
        new_tree.append(tree[i] + tree[i + 1])
        new_tree.append(tree[i + 1])
    if steps == 1:
        return new_tree
    else:
        return grow_fractree(new_tree, steps - 1)


def print_fractree_string_first(tree, width=4):
    depth = int(log2(len(tree) - 1))
    width = width
    out = []
    for d in range(0, depth + 1):
        line = ""
        pad = " " * (width * (2 ** d - 1))
        for i in range(0, len(tree), 2 ** d):
            line += str(tree[i]).ljust(width) + pad
        out.append(line.rstrip())
    out.reverse()
    print(*out, sep="\n")


def print_fractree_line_by_line(tree, width=4):
    depth = int(log2(len(tree) - 1))
    width = width
    for d in range(depth + 1, 1, -1):
        line = ""
        pad = " " * (width * (2 ** d - 1))
        for i in range(0, len(tree), 2 ** d):
            line += str(tree[i]).ljust(width) + pad
        print(line)


# -----------------------------------

DEPTH = 6
LEFT_ORIGIN = MagicFraction(0, 1)
RIGHT_ORIGIN = MagicFraction(1, 0)

print("\n\ngrowing fractree, depth = " + str(DEPTH) + ", left = " + str(LEFT_ORIGIN) + ", right = " + str(RIGHT_ORIGIN))
fractree1 = FracTree(left=LEFT_ORIGIN, right=RIGHT_ORIGIN, depth=DEPTH)
print_fractree_string_first(fractree1.inorder(), 6)

# fractree1 = [LEFT, RIGHT]
# print("growing fractree")
# fractree1 = grow_fractree(fractree1, DEPTH)
# print("fractree has matured")
#
# print_fractree_string_first(fractree1, 5)

# print("growing fractree")
# fractree1 = FracTree(left=LEFT_ORIGIN, right=RIGHT_ORIGIN, depth=DEPTH)
# print("fractree has matured")
# print_fractree_string_first(fractree1.inorder(), 3)

# for DEPTH in range(0, 7):
#     LEFT_ORIGIN = MagicFraction(0, 1)
#     RIGHT_ORIGIN = MagicFraction(2 ** (DEPTH + 1), 1)
#
#     print("\n\ngrowing fractree, depth = " + str(DEPTH) + ", right = " + str(RIGHT_ORIGIN))
#     fractree1 = FracTree(left=LEFT_ORIGIN, right=RIGHT_ORIGIN, depth=DEPTH)
#     print_fractree_string_first(fractree1.inorder(), 5)