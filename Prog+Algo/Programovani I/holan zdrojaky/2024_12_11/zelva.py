import turtle


class Zelva(turtle.Turtle):
    def __init__(self, zvetseni):
        super().__init__()
        self.zvetseni = zvetseni

    def forward(self, vzdalenost):
        super().forward(self.zvetseni * vzdalenost)


zelva = Zelva(3)
zelva.left(90)
zelva.forward(100)
zelva.right(90)

zelva.speed(10)
zelva.color("red")
zelva.width(5)

###################################
M = 6
N = 11
for j in range(M):
    for i in range(N):
        zelva.forward(100)
        zelva.left(150)
    zelva.right(280)
    zelva.forward(100)
###################################