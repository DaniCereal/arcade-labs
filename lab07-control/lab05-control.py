import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Plane:
    def __init__(self):
        """Initialize plane properties"""
        self.position_x = 600
        self.position_y = 300

        # Movement variables
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """Update plane position"""
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.change_x:
            self.position_x = self.change_x

        if self.position_x > SCREEN_WIDTH - self.change_y:
            self.position_x = SCREEN_WIDTH - self.change_y

        if self.position_y < self.change_y:
            self.position_y = self.change_y

        if self.position_y > SCREEN_HEIGHT - self.change_x:
            self.position_y = SCREEN_HEIGHT - self.change_x

    def on_draw(self):

        x = self.position_x
        y = self.position_y

        # Draw the engine
        arcade.draw_rect_filled(arcade.XYWH(x, y, 300, 70), arcade.color.GRAY)
        arcade.draw_rect_filled(arcade.XYWH(x + 160, y - 15, 90, 40), arcade.color.GRAY)

        arcade.draw_circle_filled(x + 200, y - 15, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(x + 150, y + 5, 20, arcade.color.WHITE)

        # Window
        arcade.draw_rect_filled(arcade.XYWH(x + 115, y + 15, 70, 20), arcade.color.WHITE)

        # Front side
        arcade.draw_rect_filled(arcade.XYWH(x + 160, y - 15, 90, 40), arcade.color.GRAY)

        # Superior wing
        arcade.draw_triangle_filled(
            x + 50, y,
            x + 130, y + 40,
            x + 90, y,
            arcade.color.DARK_GRAY
        )

        # Inferior wing
        arcade.draw_triangle_filled(
            x + 50, y,
            x + 130, y - 40,
            x + 90, y,
            arcade.color.DARK_GRAY
        )

        # Tail
        arcade.draw_triangle_filled(
            x - 50, y + 20,
            x, y + 50,
            x, y - 10,
            arcade.color.GRAY
        )

        # Smoke stack
        arcade.draw_rect_filled(arcade.XYWH(x + 30, y - 125, 10, 40), arcade.color.BLACK)


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Plane Example")

        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        self.plane = Plane()
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            self.joystick = None

    def on_draw(self):

        self.clear()

        # Clouds
        arcade.draw_lrbt_rectangle_filled(300, 390, 40, 80, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(400, 490, 35, 75, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(500, 590, 30, 70, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(600, 690, 55, 95, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(700, 790, 50, 90, arcade.color.WHITE)

        arcade.draw_lrbt_rectangle_filled(10, 90, 535, 575, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(100, 190, 530, 570, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(200, 290, 545, 585, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(300, 390, 540, 580, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(400, 490, 535, 575, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(500, 590, 530, 570, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(600, 690, 555, 595, arcade.color.WHITE)
        arcade.draw_lrbt_rectangle_filled(700, 790, 550, 590, arcade.color.WHITE)

        # Tower
        arcade.draw_lrbt_rectangle_filled(30, 230, 50, 500, arcade.color.ASH_GREY)

        arcade.draw_rect_filled(arcade.XYWH(100, 430, 60, 80), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(100, 430, 50, 70), arcade.color.ALABAMA_CRIMSON)

        arcade.draw_rect_filled(arcade.XYWH(180, 430, 60, 80), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(180, 430, 50, 70), arcade.color.ALABAMA_CRIMSON)

        arcade.draw_rect_filled(arcade.XYWH(100, 300, 60, 80), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(100, 300, 50, 70), arcade.color.ALABAMA_CRIMSON)

        arcade.draw_rect_filled(arcade.XYWH(180, 300, 60, 80), arcade.color.BLACK)
        arcade.draw_rect_filled(arcade.XYWH(180, 300, 50, 70), arcade.color.ALABAMA_CRIMSON)

        arcade.draw_rect_filled(arcade.XYWH(140, 180, 60, 80), arcade.color.DARK_BROWN)
        arcade.draw_rect_filled(arcade.XYWH(140, 180, 50, 70), arcade.color.WOOD_BROWN)
        arcade.draw_circle_filled(150, 170, 5, arcade.color.DARK_BROWN)

        arcade.draw_circle_filled(130, 0, 150, arcade.color.GREEN)

        # Draw plane
        self.plane.on_draw()

    #   UPDATE + JOYSTICK
    def on_update(self, delta_time):
        """Update game logic"""
        self.plane.update()
        if self.joystick:
            x_axis = self.joystick.x
            y_axis = self.joystick.y

            self.plane.position_x += x_axis * 5
            self.plane.position_y += y_axis * 5        

    #   KEYS CONTROL
    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.plane.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:
            self.plane.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self.plane.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.plane.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.plane.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.plane.change_x = 0

    #   MOUSE CONTROL
    #   Mouse Movement
    def on_mouse_motion(self, x, y, dx, dy):
        """Move the plane with the mouse"""
        self.plane.position_x = x
        self.plane.position_y = y
    
    #   Mouse click (play sound)
    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        laser_sound = arcade.load_sound("laser.wav")

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(laser_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(laser_sound)


def main():
    window = MyGame()
    arcade.run()


main()