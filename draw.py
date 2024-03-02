import turtle

# Initialize the top_left and bottom_right coordinates
top_left = None
bottom_right = None

def on_click(x, y, button, pressed):
    global top_left, bottom_right
    if pressed and not top_left:
        top_left = (int(x), int(y))
        print('Top left:', top_left)
    elif pressed and top_left and not bottom_right:
        bottom_right = (int(x), int(y))
        print('Bottom right:', bottom_right)
        draw_rectangle()
        return False
    if not pressed:
        return True

# Function to draw a rectangle
def draw_rectangle():
    global top_left, bottom_right
    turtle.penup()
    turtle.goto(top_left[0], top_left[1])
    turtle.pendown()
    turtle.goto(top_left[0], bottom_right[1])
    turtle.goto(bottom_right[0], bottom_right[1])
    turtle.goto(bottom_right[0], top_left[1])
    turtle.goto(top_left[0], top_left[1])
    turtle.penup()

# Set up event handling
turtle.onscreenclick(on_click, btn=1)

# Keep the window open
turtle.done()