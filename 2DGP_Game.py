from pico2d import *

open_canvas()
ironclad = load_image('ironclad.png')
x = 0
frame = 0
while x < 800:
    clear_canvas()
    ironclad.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 15
    x += 5
    get_events()
    delay(0.1)
close_canvas()
