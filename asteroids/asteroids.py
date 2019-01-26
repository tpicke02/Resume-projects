
from globals import *
from flyingobjects import FlyingObject
from point import Point
from velocity import Velocity


class Asteroids(FlyingObject, ABC):

    # Sets the base properties of asteroids in general
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(0, SCREEN_WIDTH)
        self.center.y = random.uniform(0, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(-1.5, 1.5)
        self.velocity.dy = random.uniform(-1.5, 1.5)


    # Sets up an abstract draw method that the different targets will utilize
    @abstractmethod
    def draw(self):
        pass

    # Sets up an abstract hit method that the different targets will utilize
    @abstractmethod
    def hit(self, asteroids):
        pass

    # Sets up the rotate property
    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        self._rotate = rotate

class Big(Asteroids):

    # Sets the base properties of big asteroids
    def __init__(self):
        super().__init__()
        self.radius = BIG_ROCK_RADIUS
        self.rotate = BIG_ROCK_SPIN

    # Draws the big asteroid
    def draw(self):
        big = "images/meteorGrey_big1.png"
        texture = arcade.load_texture(big)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        self.angle += self.rotate

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)

    # Splits the asteroid into the smaller asteroids after getting hit
    def hit(self, asteroids):
        self.alive = False

        m1P = Point()
        m1P.x = self.center.x
        m1P.y = self.center.y
        m1V = Velocity()
        m1V.dx = self.velocity.dx
        m1V.dy = 2

        m2P = Point()
        m2P.x = self.center.x
        m2P.y = self.center.y
        m2V = Velocity()
        m2V.dx = self.velocity.dx
        m2V.dy = -2

        s1P = Point()
        s1P.x = self.center.x
        s1P.y = self.center.y
        s1V = Velocity()
        s1V.dx = 5
        s1V.dy = self.velocity.dy

        asteroids.append(Medium(m1P, m1V, self.angle))
        asteroids.append(Medium(m2P, m2V, self.angle))
        asteroids.append(Small(s1P, s1V, self.angle))



class Medium(Asteroids):

    # Sets the base properties of medium asteroids
    def __init__(self, center, velocity, angle):
        super().__init__()
        self.center = center
        self.velocity = velocity
        self.angle = angle
        self.radius = MEDIUM_ROCK_RADIUS
        self.rotate = MEDIUM_ROCK_SPIN

    # Draws the medium asteroid
    def draw(self):
        medium = "images/meteorGrey_med1.png"
        texture = arcade.load_texture(medium)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        self.angle += self.rotate

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)

    # Splits the asteroid into smaller asteroids after being hit
    def hit(self, asteroids):
        self.alive = False

        s1P = Point()
        s1P.x = self.center.x
        s1P.y = self.center.y
        s1V = Velocity()
        s1V.dx = 1.5
        s1V.dy = 1.5

        s2P = Point()
        s2P.x = self.center.x
        s2P.y = self.center.y
        s2V = Velocity()
        s2V.dx = -1.5
        s2V.dy = -1.5

        asteroids.append(Small(s1P, s1V, self.angle))
        asteroids.append(Small(s2P, s2V, self.angle))

class Small(Asteroids):

    # Sets the base properties for small asteroids
    def __init__(self, center, velocity, angle):
        super().__init__()
        self.center = center
        self.velocity = velocity
        self.angle = angle
        self.radius = SMALL_ROCK_RADIUS
        self.rotate = SMALL_ROCK_SPIN

    # Draws the small asteroids
    def draw(self):
        small = "images/meteorGrey_small1.png"
        texture = arcade.load_texture(small)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        self.angle += self.rotate

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)

    # Makes the asteroid not live after being hit
    def hit(self, asteroids):
        self.alive = False







