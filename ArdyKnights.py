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
TIME_BETWEEN_EATS = 10
RUN_TIME = 5.5 * 60 * 60
TOLERANCE = 10

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
    time.sleep(3)
    start_time = time.monotonic()
    for i in range(len(coords.inventory_slot)):
        loop_time = time.monotonic()
        while time.monotonic() < loop_time + TIME_BETWEEN_EATS:
            knight_position = find_colored_hull(HULL_COLOR, TOLERANCE)
            if knight_position:
                adjusted_position = (knight_position[0]+5, knight_position[1]+5)
                cf.move_and_click(adjusted_position, random.uniform(.1, .27), random.uniform(.19, .37))
        cf.move_and_click(coords.inventory_slot[i], -1, -1)
        # Make sure food is eaten if started in stun
        for k in range(6):
            gui.click()
            time.sleep(random.uniform(.1, .27))
