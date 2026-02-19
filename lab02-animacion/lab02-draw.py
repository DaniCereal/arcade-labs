"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
#800 ancho 600 alto
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Get ready to draw

#left: float, right: float, bottom: float, top: float, color: RGBOrA255
# Draw some clouds down
arcade.draw_lrbt_rectangle_filled(300, 390, 40, 80, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(400, 490, 35, 75, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(500, 590, 30, 70, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(600, 690, 55, 95, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(700, 790, 50, 90, arcade.color.WHITE)

# Draw some clouds up
arcade.draw_lrbt_rectangle_filled(10, 90, 535, 575, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(100, 190, 530, 570, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(200, 290, 545, 585, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(300, 390, 540, 580, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(400, 490, 535, 575, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(500, 590, 530, 570, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(600, 690, 555, 595, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(700, 790, 550, 590, arcade.color.WHITE)


# --- Draw the tower ---

# Tower base
#left: float, right: float, bottom: float, top: float, color: RGBOrA255
arcade.draw_lrbt_rectangle_filled(30, 230, 50, 500, arcade.color.ASH_GREY)


# first window row

arcade.draw_rect_filled(arcade.XYWH(100, 430, 60, 80), arcade.color.BLACK)
arcade.draw_rect_filled(arcade.XYWH(100, 430, 50, 70), arcade.color.ALABAMA_CRIMSON)

#x: AsFloat y: AsFloat, weight: AsFloat, height: AsFloat,
arcade.draw_rect_filled(arcade.XYWH(180, 430, 60, 80), arcade.color.BLACK)
arcade.draw_rect_filled(arcade.XYWH(180, 430, 50, 70), arcade.color.ALABAMA_CRIMSON)

# second window row

arcade.draw_rect_filled(arcade.XYWH(100, 300, 60, 80), arcade.color.BLACK)
arcade.draw_rect_filled(arcade.XYWH(100, 300, 50, 70), arcade.color.ALABAMA_CRIMSON)

#x: AsFloat y: AsFloat, weight: AsFloat, height: AsFloat,
arcade.draw_rect_filled(arcade.XYWH(180, 300, 60, 80), arcade.color.BLACK)
arcade.draw_rect_filled(arcade.XYWH(180, 300, 50, 70), arcade.color.ALABAMA_CRIMSON)

# Small door

#x: AsFloat y: AsFloat, weight: AsFloat, height: AsFloat,
arcade.draw_rect_filled(arcade.XYWH(140, 180, 60, 80), arcade.color.DARK_BROWN)
arcade.draw_rect_filled(arcade.XYWH(140, 180, 50, 70), arcade.color.WOOD_BROWN)
arcade.draw_circle_filled(150, 170, 5, arcade.color.DARK_BROWN)

#Drawing the hill
#center_x: float, center_y: float, radius: float
arcade.draw_circle_filled(130, 0, 150, arcade.color.GREEN)

# --- Draw the tractor ---

# Draw the engine
arcade.draw_rect_filled(arcade.XYWH(550, 300, 300, 70), arcade.color.GRAY)
arcade.draw_rect_filled(arcade.XYWH(710, 285, 90, 40), arcade.color.GRAY)
arcade.draw_circle_filled(750, 285, 20, arcade.color.BLACK)
arcade.draw_circle_filled(700, 305, 20, arcade.color.WHITE)
arcade.draw_rect_filled(arcade.XYWH(550, 300, 300, 70), arcade.color.GRAY)

#drawing the window
arcade.draw_rect_filled(arcade.XYWH(665, 315, 70, 20), arcade.color.WHITE)
arcade.draw_circle_filled(750, 285, 20, arcade.color.GRAY)

# Draw the Front side
arcade.draw_rect_filled(arcade.XYWH(710, 285, 90, 40), arcade.color.GRAY)

# Superior
arcade.draw_triangle_filled(
    600, 300,
    680, 340,
    640, 300,
    arcade.color.DARK_GRAY
)

# Inferior wing
arcade.draw_triangle_filled(
    600, 300,
    680, 260,
    640, 300,
    arcade.color.DARK_GRAY
)

# Drawing the tail
arcade.draw_triangle_filled(
    500, 320,   # Punto 1
    550, 350,   # Punto 2
    550, 290,   # Punto 3
    arcade.color.GRAY
)



# Draw the smoke stack
arcade.draw_rect_filled(arcade.XYWH(580, 175, 10, 40), arcade.color.BLACK)

# --- Finish drawing ---

# Keep the window up until someone closes it.
arcade.finish_render()
arcade.run()