
from globals import math

class Velocity:

    # Sets the base velocity of objects
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0


    # Calculates the velocity according to the angle and speed of the object
    def calc_velocity(self, angle, speed):
        self.dx = math.cos(math.radians(angle)) * speed
        self.dy = math.sin(math.radians(angle)) * speed

    # Adds velocity
    def add(self, velocity):
        self.dx += velocity.dx
        self.dy += velocity.dy