from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while x < 800:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x +=2
    delay(0.01)

y = 90
while y < 600:
    clear_canvas_now()
    character.draw_now(800, y)
    grass.draw_now(400, 30)
    y +=2
    delay(0.01)


x = 800
while x > 0:
    clear_canvas_now()
    character.draw_now(x, 600)
    grass.draw_now(400, 30)
    x = x-2
    delay(0.01)

y = 600
while y > 90 :
    clear_canvas_now()
    character.draw_now(0, y)
    grass.draw_now(400, 30)
    y -=2
    delay(0.01)


delay(5)

# fill here

close_canvas()
