import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random




de

def set_screen(height=16, width=22):
    # sets the screen's height and width
    screen = np.zeros((height,width), dtype=np.int16)

    # sets the walls
    screen[0] = 255
    screen[height - 1] = 255
    screen[:,0] = 255
    screen[:,width - 1] = 255
    return screen

def fruit_spawn():
    fruit = {}
    fruit['x'] = np.random.randint(1,15, dtype=np.int16)
    fruit['y'] = np.random.randint(1,21, dtype=np.int16)
    fruit['color'] = 200    
    return fruit
    

fig, ax = plt.subplots()
ax.set_xlim(0,21)
ax.set_ylim(0,15)
# sets the first axis image object









xs = [7,8,9,9,10,11,12]
ys = [9,9,9,8,8,8,8]

for x,y in zip(xs,ys):
    
    screen = set_screen(height=16, width=22)
    axim = ax.imshow(X=screen)

    snake = np.array([x,y,130], np.int32)
    screen[snake[0], snake[1]] = snake[2]
    
    fruit = fruit_spawn()

    screen[fruit['x'], fruit['x']] = fruit['color']
#    M=yourfunction() # updates your image
    axim.set_array(screen) # prepare the new image
    fig.canvas.draw() # draw the image
    plt.pause(0.9) # slow down the "animation"
    fig.show()





