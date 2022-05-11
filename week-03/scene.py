# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
  
    draw_rectangle(canvas, 0, 0, 800, 500, fill='blue4')
    draw_rectangle(canvas, 0, 0, 800, 175, fill='darkGreen')    
    draw_cloud(canvas, 450, 400, 350)
    draw_cloud(canvas, 300, 400, 350)
    draw_cloud(canvas, 250, 400, 350)


    for x2 in range (25, 900, 55):
        draw_pine_tree(canvas, x2, 100, 170)
        x2 = x2 + 25

    for x1 in range(25, 900, 50):
        draw_pine_tree(canvas, x1, 100, 150)

    for x in range(100, 900, 50):
        x = x + 100
     
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_pine_tree(canvas, center_x, bottom, height):
    #draw tree trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill='brown')

    #tree skirt
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill='forestGreen')


def draw_cloud(canvas, center_x, bottom, height):
    #draw clouds
    cloud_width = height / 5
    cloud_height = height / 7
    left_cloud = center_x - cloud_height
    bottom_cloud = bottom
    right_cloud = center_x + cloud_height
    cloud_top = bottom + cloud_height
    draw_oval(canvas, left_cloud, bottom_cloud, right_cloud, cloud_top, outline="salmon", fill='white')

# Call the main function so that
# this program will start executing.
main()