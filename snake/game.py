from avatars import Snake, Fruits
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random
from environment import set_screen, get_walls, get_free_coordinates
import keyboard




# INSTANTIATING SCREEN, WALLS, SNAKE, BODY, POINTS, BESIDES GETTING FREE COORDINATES TO ADD THE FRUIT
height = 16
width = 22
screen = set_screen(height=height, width=width)
walls = get_walls(screen)
snake = Snake()
body = []
points = 0 
screen[snake.position[0], snake.position[1]] = 125
free_coordinates = get_free_coordinates(screen=screen)
fruit = Fruits(free_coordinates=free_coordinates)


# GENERATING A MATPLOTLIB FIGURE WHICH WILL BE USED TO DISPLAY THE GAME
fig, ax = plt.subplots()
ax.set_xlim(0,width-1)
ax.set_ylim(0,height-1)

### I need to implement 'for rounds in range(3):' to create rounds. 
### However, I need to figure out how matplotlib will handle it


# GAME
while snake.state == 'alive':

    screen = set_screen(height=16, width=22)
    walls = get_walls(screen)

    if points > 0:
        snake.grow(points=points)
        for coordinates in snake.body_position:
            screen[coordinates[0], coordinates[1]] = 125
    
    keyboard.on_press_key('up', snake.change_orientation)
    keyboard.on_press_key('down', snake.change_orientation)
    keyboard.on_press_key('left', snake.change_orientation)
    keyboard.on_press_key('right', snake.change_orientation)

    snake.change_position()
    snake.check_if_dies(walls=walls)
    screen[snake.position[0], snake.position[1]] = 125

    axim = ax.imshow(X=screen)

    free_coordinates = get_free_coordinates(screen=screen)

    if fruit.state == 'eaten':
        fruit.spawns(free_coordinates=free_coordinates)
        fruit.state = 'not eaten'
        points += 1

    screen[fruit.position[0], fruit.position[1]] = 200

    fruit.gets_eaten(snake_position=snake.position)

    if snake.state == 'dead':
        plt.title('Snake is Dead')
#            axim.set_array(screen) # prepare the new image
#            fig.canvas.draw() # draw the image
        plt.pause(1) # slow down the "animation

    else:
        axim.set_array(screen) # prepare the new image
        fig.canvas.draw() # draw the image
        plt.pause(1) # slow down the "animation"

fig.show()
#plt.show(block=True)            