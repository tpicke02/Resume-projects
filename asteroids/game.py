
from globals import *
from flyingobjects import FlyingObject
from asteroids import *
from ship import *
from bullets import Bullet


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.asteroids = [Big(), Big(), Big(), Big(), Big()]
        self.bullets = []
        self.ship = Ship()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        space = "images/Space-Free-PNG-Image.png"
        texture = arcade.load_texture(space)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, texture)

        # TODO: draw each object
        for asteroids in self.asteroids:
            if asteroids.alive == True:
                asteroids.draw()

        for bullets in self.bullets:
            if bullets.alive == True:
                bullets.draw()

        if self.ship.alive == True:
            self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collision()

        # TODO: Tell everything to advance or move forward one step in time
        for asteroids in self.asteroids:
            if asteroids.alive == True:
                asteroids.advance()
                self.wrap(asteroids)

        for bullets in self.bullets:
            if bullets.alive == True:
                bullets.advance()
                self.wrap(bullets)
                bullets.age += 1

        if self.ship.alive == True:
            self.ship.advance()
            self.wrap(self.ship)

        # TODO: Check for collisions

    def wrap(self, flying):

        # Used to wrap objects cleanly around the screen
        if flying.center.x > SCREEN_WIDTH + 50:
            flying.center.x = flying.center.x - (SCREEN_WIDTH + 50)

        if flying.center.x < -50:
            flying.center.x = flying.center.x + (SCREEN_WIDTH + 50)

        if flying.center.y > SCREEN_HEIGHT + 50:
            flying.center.y = flying.center.y - (SCREEN_HEIGHT + 50)

        if flying.center.y < -50:
            flying.center.y = flying.center.y + (SCREEN_HEIGHT + 50)

    def check_collision(self):

        # Checks for collisions between ship, bullets, and asteroids and calls for clean up
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                        abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        asteroid.hit(self.asteroids)

        for asteroid in self.asteroids:
            if asteroid.alive and self.ship.alive:
                too_close = asteroid.radius + self.ship.radius

                if (abs(asteroid.center.x - self.ship.center.x) < too_close and
                    abs(asteroid.center.y - self.ship.center.y) < too_close):
                    # its a hit!
                    self.ship.alive = False

        self.cleanup_zombies()

    def cleanup_zombies(self):

        # Removes the bullets and asteroids from their lists when they are not alive
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)


    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()

        if arcade.key.UP in self.held_keys:
            self.ship.apply_thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.apply_reverse()

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                angle = self.ship.angle

                pnt = Point()
                pnt.x = self.ship.center.x
                pnt.y = self.ship.center.y

                bullet = Bullet()
                bullet.fire(angle, pnt)

                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()