import sys
import time
import threading
import pyautogui as gui
import random
from PIL import Image
import numpy as np

import common_functions as cf
import coordinates as coords

FOOD_COORD = (566, 180)

COIN_POUCH_MAX = 28
HULL_COLOR = (255, 0, 154)
HULL_COLOR_BANK = (0, 255, 29)
TIME_BETWEEN_EATS = 45
RUN_TIME = 5.5 * 60 * 60
TOLERANCE = 10

S_LEFT = 368
S_TOP = 30
S_RIGHT = 1136
S_BOT = 540
GAME_SCREEN = (S_LEFT, S_TOP, S_RIGHT, S_BOT)


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


def find_colored_hull_center_fast_crop(target_color, tolerance=0, search_area=None):
    # Crop screen then convert to numpy
    if search_area:
        left, top, right, bottom = search_area
        # Take screenshot of only the search area
        screenshot = gui.screenshot(region=(left, top, right-left, bottom-top))
        offset_x, offset_y = left, top
    else:
        screenshot = take_screenshot()
        offset_x, offset_y = 0, 0

    img_array = np.array(screenshot)
    # Boolean mask for matching pixels
    if tolerance == 0:
        mask = np.all(img_array == target_color, axis=2)
    else:
        # Vectorized tolerance check
        diff = np.abs(img_array - target_color)
        mask = np.all(diff <= tolerance, axis=2)

    # Find matching coordinates
    matching_coords = np.where(mask)

    if len(matching_coords[0]) == 0:
        return None

    # Calculate center of matching pixels
    center_y = int(np.mean(matching_coords[0]).item()) + offset_y
    center_x = int(np.mean(matching_coords[1]).item()) + offset_x

    return center_x, center_y


# For speed without numpy dependency:
# find_colored_hull_center_optimized = find_colored_hull_center_optimized_fast
# For region-based search:
# find_colored_hull_center_optimized = find_colored_hull_center_region_split


def color_match(given_color, target_color, tolerance):
    if tolerance == 0:
        return given_color == target_color
    r_diff = abs(given_color[0] - target_color[0])
    g_diff = abs(given_color[1] - target_color[1])
    b_diff = abs(given_color[2] - target_color[2])
    return (r_diff <= tolerance) and (g_diff <= tolerance) and (b_diff <= tolerance)


def find_knight():
    knight_position = find_colored_hull_center_fast_crop(HULL_COLOR, TOLERANCE, GAME_SCREEN)
    if not knight_position:
        cf.screen_scroll(coords.zoom_bar_max)
        while not knight_position:
            knight_position = find_colored_hull_center_fast_crop(HULL_COLOR, TOLERANCE, GAME_SCREEN)
            time.sleep(3)
    if knight_position:
        cf.move_and_click(knight_position, random.uniform(.1, .27), random.uniform(.19, .37))
        cf.screen_scroll(coords.zoom_bar_4)
        time.sleep(3)


def pickpocket_loop():
    time.sleep(3)
    cf.screen_scroll(coords.zoom_bar_4)
    num_food_left = 26
    # Slot 1 = coin pouch, Slot 2 = coins
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
                knight_position = find_colored_hull_center_fast_crop(HULL_COLOR, TOLERANCE, GAME_SCREEN)
                if knight_position:
                    cf.move_and_click(knight_position, random.uniform(.1, .27), random.uniform(.19, .37))
                else:
                    find_knight()
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


def bank_loop():
    time.sleep(2)
    cf.screen_scroll(coords.zoom_bar_max)
    bank_position = find_colored_hull_center_fast_crop(HULL_COLOR_BANK, TOLERANCE, GAME_SCREEN)
    if bank_position:
        print("found")
        gui.keyDown("shift")
        cf.move_and_click(bank_position, -1, 8)
        gui.keyUp("shift")
        cf.move_and_click(FOOD_COORD, -1, -1)
        gui.press("esc")
        for i in range(2):
            cf.move_and_click_variable_coord(coords.inventory_slot[i + 2], -1, -1)
        bank_position = find_colored_hull_center_fast_crop(HULL_COLOR_BANK, TOLERANCE, GAME_SCREEN)
        if bank_position:
            gui.keyDown("shift")
            cf.move_and_click(bank_position, -1, 2)
            gui.keyUp("shift")
            cf.move_and_click(FOOD_COORD, -1, -1)
            gui.press("esc")
            cf.move_and_click_variable_coord(coords.inventory_slot[0], -1, -1)
    else:
        print("no bank match")
    find_knight()


def run():
    start_time = time.monotonic()
    while time.monotonic() < start_time + 5.5 * 60 * 60:
        pickpocket_loop()
        bank_loop()