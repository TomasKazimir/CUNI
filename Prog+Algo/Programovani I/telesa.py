import turtle as t
from math import sqrt
from time import sleep

class Body:
    def __init__(self, x, y, velx = 0, vely = 0, mass = 1, is_fixed = False):
        self.x = x
        self.y = y
        self.mass = mass
        self.velx = velx
        self.vely = vely
        self.accx = 0
        self.accy = 0
        self.fx = 0
        self.fy = 0
        self.positions = [(x, y) for _ in range(50)]
        self.counter = 0
        self.is_fixed = is_fixed
    
    def move(self, dt = 1):
        if self.is_fixed:
            return
        self.x += self.velx * dt
        self.y += self.vely * dt
        self.counter += 1
        if self.counter % 1 == 0:
            self.counter = 0
            self.positions.pop(0)
            self.positions.append((self.x, self.y))
    
    def update_vel(self):
        if self.is_fixed:
            return
        self.velx += self.accx
        self.vely += self.accy
        
    def update_acc(self):
        if self.is_fixed:
            return
        self.accx = self.fx / self.mass
        self.accy = self.fy / self.mass
        self.fx = 0
        self.fy = 0


def force(B1: Body, B2: Body):
    dx = B2.x - B1.x
    dy = B2.y - B1.y
    distance = sqrt(dx**2 + dy**2)
    if distance == 0:
        return 0, 0
    
    F = (9.81 * B1.mass * B2.mass) / distance
    
    sin_alpha = dy / distance
    cos_alpha = dx / distance
    Fx = F * cos_alpha
    Fy = F * sin_alpha
    
    return Fx, Fy
    

bodies = []
bodies.append(Body(-100, -100, velx =   0, vely = 200, mass = 30))
bodies.append(Body(-100,  100, velx = 100, vely =   0, mass = 30))
bodies.append(Body( 100,  100, velx =   0, vely =-100, mass = 30))
bodies.append(Body( 100, -100, velx =-100, vely =   0, mass = 30))

# bodies.append(Body(-100, -100, velx =   0, vely = 110, mass = 20))
# bodies.append(Body( 100,  100, velx =   0, vely =   0, mass = 20))
# bodies.append(Body(   0,    0, velx =   0, vely =-100, mass = 30))

# bodies.append(Body(   0,   0, velx =   0, vely =    0, mass = 1000, is_fixed=True))
# bodies.append(Body(   0, 100, velx =990, vely =    0, mass =    1))
# bodies.append(Body( 200,   0, velx =    0, vely = 990, mass =    1))
# bodies.append(Body(   0, 300, velx =990, vely =    0, mass =    1))
# bodies.append(Body( 400,   0, velx =    0, vely = 990, mass =    1))
# bodies.append(Body(   0, 500, velx =990, vely =    0, mass =    1))
# bodies.append(Body( 600,   0, velx =    0, vely = 990, mass =    1))
# bodies.append(Body(   0, 700, velx =990, vely =    0, mass =    1))
# bodies.append(Body( 800,   0, velx =    0, vely = 990, mass =    1))
# bodies.append(Body(   0, 900, velx =990, vely =    0, mass =    1))

dt = 0.01

t.setup(1000, 1000)
screen = t.Screen()
screen.tracer(0, 0)
t.hideturtle()
t.penup()
t.pensize(3)

while True:
    for body in bodies:
        for pos in body.positions:
            t.goto(pos[0], pos[1])
            t.pendown()
        t.dot((body.mass*0.239)**(1/3)*10, "Red")
        t.penup()
    
    for i in range(1):
        for body in bodies:
            for b in bodies:
                if b != body:
                    fx, fy = force(body, b)
                    body.fx += fx
                    body.fy += fy

        for body in bodies:
            body.update_acc()
            body.update_vel()
            body.move(dt)
    
    t.update()
    t.clear()
    
        
