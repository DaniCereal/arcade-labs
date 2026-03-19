import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_BAD = 0.2
COIN_COUNT = 50
BAD_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bad_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("Heart.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Heals.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_y = -0.5

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(BAD_COUNT):

            # Create the bad guy instance
            # enemy image from kenney.nl
            bad = arcade.Sprite("Pettels.png", SPRITE_SCALING_COIN)

            # Position the enemy
            bad.center_x = random.randrange(SCREEN_WIDTH)
            bad.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the bad to the lists
            self.bad_list.append(bad)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_list.draw()
        self.bad_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.bad_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        bads_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.bad_list)

            
        #Make enemies follow the player
        for bad in self.bad_list:
            dx = self.player_sprite.center_x - bad.center_x
            dy = self.player_sprite.center_y - bad.center_y

            dist = (dx**2 + dy**2) ** 0.5

            if dist != 0:
                dx /= dist
                dy /= dist

            # --- PARÁMETROS ---
            velocidad = 2
            distancia_segura = 150

            # --- COMPORTAMIENTO ---
            if dist < distancia_segura:
                move_x = -dx * velocidad
                move_y = -dy * velocidad
            else:
                move_x = dx * (velocidad * 0.5)
                move_y = dy * (velocidad * 0.5)

            perp_x = -dy
            perp_y = dx

            move_x += perp_x * 1.5
            move_y += perp_y * 1.5

            # Aplicar movimiento
            bad.center_x += move_x
            bad.center_y += move_y

            # --- LIMITES DE PANTALLA ---
            if bad.left < 0:
                bad.left = 0
            if bad.right > SCREEN_WIDTH:
                bad.right = SCREEN_WIDTH
            if bad.bottom < 0:
                bad.bottom = 0
            if bad.top > SCREEN_HEIGHT:
                bad.top = SCREEN_HEIGHT
        # Move coins down
        for coin in self.coin_list:
            coin.center_y += coin.change_y

            # Si sale por abajo, reaparece arriba
            if coin.top < 0:
                coin.bottom = SCREEN_HEIGHT
                coin.center_x = random.randrange(SCREEN_WIDTH)
        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        
        for bad in bads_hit_list:
            bad.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

