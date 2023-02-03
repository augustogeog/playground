import numpy as np

def set_screen(height=16, width=22):
    # sets the screen's height and width
    screen = np.zeros((height,width), dtype=np.int16)

    # sets the walls
    screen[0] = 255
    screen[height - 1] = 255
    screen[:,0] = 255
    screen[:,width - 1] = 255

    return screen


def get_walls(screen):
    walls = np.where(screen == 255)
    walls = {(x,y) for x,y in zip(walls[0],walls[1])}
    return walls

def get_free_coordinates(screen):
    free_coordinates = np.where(screen == 0)
    free_coordinates = {(x,y) for x,y in zip(free_coordinates[0],free_coordinates[1])}
    return free_coordinates