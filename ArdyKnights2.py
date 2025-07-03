import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image

import common_functions as cf
import coordinates as coords

ARDY_KNIGHT_COORD = (567, 229)
FOOD_COORD = (566, 180)

COIN_POUCH_MAX = 28
HULL_COLOR = (255, 0, 154)
HULL_COLOR_BANK = (0, 255, 29)
TIME_BETWEEN_EATS = 40
RUN_TIME = 5.5 * 60 * 60
TOLERANCE = 10

S_LEFT = 368
S_TOP = 30
S_RIGHT = 1136
S_BOT = 540

####################
###    SET UP    ###
####################
# Ardy Knight hull color set to HULL_COLOR
# Coin pouch slot 1
# Coins slot 2
# rest of inventory set to food
# start in ardy bank



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
                return x, y
    return None


def find_colored_hull_center_optimized(target_color, tolerance=0, search_area=None):
    screenshot = gui.screenshot()
    if search_area:
        left, top, right, bottom = search_area
        screenshot = screenshot.crop((left, top, right, bottom))
        offset_x, offset_y = left, top
    else:
        offset_x, offset_y = 0, 0
    width, height = screenshot.size
    matching_pixels = []
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            if color_match(pixel_color, target_color, tolerance):
                matching_pixels.append((x + offset_x, y + offset_y))
    if not matching_pixels:
        return None
    
    sum_x = sum(pixel[0] for pixel in matching_pixels)
    sum_y = sum(pixel[1] for pixel in matching_pixels)
    center_x = sum_x // len(matching_pixels)
    center_y = sum_y // len(matching_pixels)
    return center_x, center_y


def color_match(given_color, target_color, tolerance):
    if tolerance == 0:
        return given_color == target_color
    r_diff = abs(given_color[0] - target_color[0])
    g_diff = abs(given_color[1] - target_color[1])
    b_diff = abs(given_color[2] - target_color[2])
    return (r_diff <= tolerance) and (g_diff <= tolerance) and (b_diff <= tolerance)


def Pickpocket_Loop():
    time.sleep(3)
    cf.scroll_4()
    start_time = time.monotonic()
    search_area = (S_LEFT, S_TOP, S_RIGHT, S_BOT)
    num_food_left = 26
    current_food_slot = 2
    # FOOD REMAINING LOOP
    while num_food_left > 0:
        food_eating_timer = time.monotonic()
        # FOOD EATING LOOP
        while time.monotonic() < food_eating_timer + TIME_BETWEEN_EATS:
            coin_pouch_timer = time.monotonic()
            # COINPOUCH LOOP
            while time.monotonic() < coin_pouch_timer + COIN_POUCH_MAX * 2:
                 time.sleep(random.uniform(0.05, 0.15))
                 knight_position = find_colored_hull_center_optimized(HULL_COLOR, TOLERANCE, search_area)
                 if knight_position:
                     cf.move_and_click(knight_position, random.uniform(.1, .27), random.uniform(.19, .37))
            # Open coin pouch
            cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, -1)
            for k in range(4):
                gui.click()
                time.sleep(random.uniform(.1, .27))
        cf.move_and_click(coords.inventory_slot[current_food_slot], -1, -1)
        # Make sure food is eaten if started in stun
        for k in range(4):
            gui.click()
            time.sleep(random.uniform(.1, .27))
        num_food_left -= 1
        current_food_slot += 1


def Bank_Loop():
    time.sleep(2)
    cf.scroll_out()
    bank_position = find_colored_hull(HULL_COLOR_BANK, TOLERANCE)
    if bank_position:
        print("found")
        gui.keyDown("shift")
        cf.move_and_click(bank_position, -1, 5)
        gui.keyUp("shift")
        cf.move_and_click(FOOD_COORD, -1, -1)
        gui.press("esc")
        for i in range(6):
            cf.move_and_click_variable_coord(coords.inventory_slot[i+2], -1, -1)
        bank_position = find_colored_hull(HULL_COLOR_BANK, TOLERANCE)
        bank_position[0] = bank_position[0] + 5
        bank_position[1] = bank_position[1] + 5
        if bank_position:
            gui.keyDown("shift")
            cf.move_and_click(bank_position, -1, 2.5)
            gui.keyUp("shift")
            cf.move_and_click(FOOD_COORD, -1, -1)
            gui.press("esc")
            cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, -1)
    else:
        print("no match")
    knight_position = find_colored_hull_center_optimized(HULL_COLOR, TOLERANCE)
    while not knight_position:
        knight_position = find_colored_hull_center_optimized(HULL_COLOR, TOLERANCE)
        time.sleep(3)
    if knight_position:
        cf.move_and_click(knight_position, random.uniform(.1, .27), random.uniform(.19, .37))
        time.sleep(3)
        

def Run():
    start_time = time.monotonic()
    while time.monotonic() < start_time + 5 * 60 * 60:
        Pickpocket_Loop()
        Bank_Loop()

