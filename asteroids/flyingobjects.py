
from globals import *
from point import Point
from velocity import Velocity

class FlyingObject(ABC):

    # Sets the base properties of flying objects
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self._speed = 0.0
        self._angle = 0.0
        self.radius = 0.0
        self.alive = True

    # Advances the object forward dependent upon it's velocity
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    # Sets up an abstract draw method that the bullet and target files will utilize
    @abstractmethod
    def draw(self):
        pass

    # Sets the angle property
    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        self._angle = angle % 360

    # Sets the speed property
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < -6:
            self._speed = -6
        elif speed > 6:
            self._speed = 6
        else:
            self._speed = speed