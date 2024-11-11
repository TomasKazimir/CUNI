from typing import List


class Matrix:
    def __init__(self, values: List[List]):
        self.r = len(values)
        self.c = len(values[0])
        self.values = values

    def is_symmetric(self) -> bool:
        """Returns True if the matrix is symmetric."""
        if self.r != self.c:
            return False
        for i in range(self.r):
            for j in range(i, self.c):
                if self.values[i][j] != self.values[j][i]:
                    return False
        return True

    def vals(self) -> List[List]:
        """Returns a list of lists of numbers containing the values in this Matrix."""
        return self.values

    def dims(self) -> tuple:
        """Returns a tuple of integers (r, c) with the matrix's dimensions."""
        return self.r, self.c

    def __add__(self, other):
        return Matrix([[self.values[i][j] + other.values[i][j]
                        for j in range(self.c)]
                       for i in range(self.r)])

    def __sub__(self, other):
        return Matrix([[self.values[i][j] - other.values[i][j]
                        for j in range(self.c)]
                       for i in range(self.r)])

    def __mul__(self, other):
        if type(other) == Matrix:
            return Matrix([[sum([self.values[i][k] * other.values[k][j]
                                 for k in range(self.c)])
                            for j in range(other.col_len)]
                           for i in range(self.r)])

        return Matrix([[self.values[i][j] * other
                        for j in range(self.c)]
                       for i in range(self.r)])

    def __repr__(self):
        return "\n".join([" ".join(str(_) for _ in row) for row in self.values])


def zero_matrix(r: int, c: int, x = 0) -> Matrix:
    """Returns a Matrix of zeroes of dimensions r x c."""
    return Matrix([[x for _ in range(c)] for _ in range(r)])


def identity_matrix(n: int) -> Matrix:
    """Returns an identity Matrix of dimensions n x n."""
    return Matrix([[1 if j == i else 0 for j in range(n)] for i in range(n)])


def pprint(x, sep_len: int = 40) -> None:
    print(x)
    print("-" * sep_len)


if __name__ == '__main__':
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[10, 11], [20, 21], [30, 31]])
    pprint(a)
    pprint(a.is_symmetric())
    pprint(b)
    pprint(a * b)
    pprint(identity_matrix(10).is_symmetric())
    pprint(zero_matrix(10, 3))
    pprint(identity_matrix(10))
