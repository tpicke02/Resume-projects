
from globals import *
from flyingobjects import FlyingObject


class Bullet(FlyingObject):

    # Sets the base properties of bullets
    def __init__(self):
        super().__init__()
        self.age = 0
        self.radius = BULLET_RADIUS

    # Draws the bullet with the dimensions given in the globals file
    def draw(self):
        if self.alive == True:
            bullet = "images/laserBlue01.png"
            texture = arcade.load_texture(bullet)

            width = texture.width
            height = texture.height
            alpha = 1  # For transparency, 1 means not transparent

            x = self.center.x
            y = self.center.y
            angle = self.angle

            arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    # Fires the bullet and adjusts the velocity dependent upon the angle it is fired
    def fire(self, angle, pnt):
        self.center.x = pnt.x
        self.center.y = pnt.y
        self.angle = angle
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED

    # Sets the age property to decide how long the bullet lives
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
        if self._age > BULLET_LIFE:
            self.alive = False
        else:
            self.alive = True


