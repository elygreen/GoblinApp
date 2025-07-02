import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image

import common_functions as cf
import coordinates as coords

ARDY_KNIGHT_COORD = (567, 229)

HULL_COLOR = (255, 0, 154)

def take_screenshot():
    screenshot = gui.screenshot()
    screenshot.save("screenshot.png")
    return screenshot


def find_colored_hull(target_color, tolerance=0):
    screenshot = gui.screenshot()
    width, height = screenshot.size
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            if color_match(pixel_color, target_color, tolerance):
                print(f"Color found at: {x}, {y}")
                return x, y
    print(f"Color not found")
    return None


def color_match(given_color, target_color, tolerance):
    if tolerance == 0:
        return given_color == target_color
    r_diff = abs(given_color[0] - target_color[0])
    g_diff = abs(given_color[1] - target_color[1])
    b_diff = abs(given_color[2] - target_color[2])
    return (r_diff <= tolerance) and (g_diff <= tolerance) and (b_diff <= tolerance)

def Run():
    pass

if __name__ == "__main__":
    time.sleep(1.5)
    position = find_colored_hull(HULL_COLOR, 10)
    if position:
        gui.click(position)
    else:
        print("Not found")