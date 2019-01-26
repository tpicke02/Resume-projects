
from globals import *
from flyingobjects import *
from velocity import *


class Ship(FlyingObject):

    # Sets the base properties of the ship
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.angle = 90
        self.speed = 0.0
        self.radius = SHIP_RADIUS

    # Draws the ship
    def draw(self):
        ship = "images/playerShip1_orange.png"
        texture = arcade.load_texture(ship)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle - 90

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    # Rotates ship left
    def rotate_left(self):
        self.angle += SHIP_TURN_AMOUNT

    # Rotates ship right
    def rotate_right(self):
        self.angle -= SHIP_TURN_AMOUNT

    # Increases the ship's velocity
    def apply_thrust(self):
        if self.alive:
            self.speed += SHIP_THRUST_AMOUNT
            self.velocity.calc_velocity(self.angle, self.speed)

    # Decreases the ship's velocity
    def apply_reverse(self):
        if self.alive:
            self.speed -= SHIP_THRUST_AMOUNT
            self.velocity.calc_velocity(self.angle, self.speed)

