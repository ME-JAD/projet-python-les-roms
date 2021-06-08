import tkinter
import time
from tkinter import messagebox

__WIDTH = 800
__HEIGHT = 600

window = tkinter.Tk()
window.title = 'test'
window.geometry(str(__WIDTH) + 'x' + str(__HEIGHT))

canvas = tkinter.Canvas(window)
canvas.pack(fill='both', expand='True')
canvas.configure(bg='black')

player_x = 100
player_y = 100
player_size = 5
stepX = 0
stepY = 0

direction = 1


def turn_left(event=0):
    global direction
    direction = (direction - 1) % 4


def turn_right(event=0):
    global direction
    direction = (direction + 1) % 4


def warp():
    global direction, player_x, player_y
    if direction == 0:
        player_y = player_y + __HEIGHT - player_size
    elif direction == 1:
        player_x = player_x - __WIDTH + player_size
    elif direction == 2:
        player_y = player_y - __HEIGHT + player_size
    elif direction == 3:
        player_x = player_x + __WIDTH - player_size


player = canvas.create_rectangle(player_x, player_y,
                                 player_x + player_size, player_y + player_size, fill='green', outline='white')

window.bind('<KeyPress-Left>', turn_left)
window.bind('<KeyPress-Right>', turn_right)

while True:
    canvas.create_rectangle(player_x, player_y,
                            player_x + player_size, player_y + player_size, fill='red', outline='white')

    if direction == 0:
        player_y -= player_size
    elif direction == 1:
        player_x += player_size
    elif direction == 2:
        player_y += player_size
    elif direction == 3:
        player_x -= player_size

    canvas.coords(player, player_x, player_y, player_x + player_size, player_y + player_size)
    elements = canvas.find_overlapping(player_x + player_size / 2, player_y + player_size / 2,
                                       player_x + player_size / 2, player_y + player_size / 2)
    if player_x <= 0 or player_x + player_size >= __WIDTH or player_y <= 0 or player_y + player_size >= __HEIGHT:
        warp()

    for element in elements:
        if canvas.itemcget(element, 'fill') == 'red':
            messagebox.showinfo('Crash', 'End !')
            gameProgress = False

    window.update()
    time.sleep(0.02)

