import time
import pyautogui as gui
import random
import numpy as np

import common_functions as cf
import coordinates as coords

COIN_POUCH_MAX = 56
HULL_COLOR = (255, 0, 154)
HULL_COLOR_BANK = (0, 255, 29)
RUN_TIME = 5.0 * 60 * 60
TOLERANCE = 10

# Pixel coordinates of game screen when in full screen
S_LEFT = 368
S_TOP = 30
S_RIGHT = 1136
S_BOT = 540
GAME_SCREEN = (S_LEFT, S_TOP, S_RIGHT, S_BOT)

isZoomed = False


####################
###    SET UP    ###
####################
# Ardy Knight hull color set to HULL_COLOR
# Coin pouch slot 1, Coins slot 2
# Start in ardy bank
# This script requires 95+ thieving, as well as Ardy medium diary completed


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


def open_coin_pouch():
    cf.move_and_click(coords.inventory_slot[0], -1, -1, precision=3)
    for k in range(3):
        gui.click()
        time.sleep(random.uniform(.1, .27))


# Match two given colors based on the difference between their RGB values
# with a given level of tolerance
def color_match(given_color, target_color, tolerance):
    if tolerance == 0:
        return given_color == target_color
    r_diff = abs(given_color[0] - target_color[0])
    g_diff = abs(given_color[1] - target_color[1])
    b_diff = abs(given_color[2] - target_color[2])
    return (r_diff <= tolerance) and (g_diff <= tolerance) and (b_diff <= tolerance)


# Function to find knight based on tagged hull color using NPC Tagger
# If knight can't be found on current zoom, zoom to max distance and repeat until success
def find_knight():
    global isZoomed
    knight_position = find_colored_hull_center_fast_crop(HULL_COLOR, TOLERANCE, GAME_SCREEN)
    if not knight_position:
        cf.screen_scroll(coords.zoom_bar_max)
        isZoomed = False
        while not knight_position:
            time.sleep(1)
            knight_position = find_colored_hull_center_fast_crop(HULL_COLOR, TOLERANCE, GAME_SCREEN)
            time.sleep(2)
    else:
        cf.move_and_click(knight_position, random.uniform(.1, .27), random.uniform(.19, .37))
        cf.screen_scroll(coords.zoom_bar_4)
        isZoomed = True
        time.sleep(random.uniform(0.37, .99))


# Pickpocket knight loop for duration of max coin pouch allotment
# Zooms in, finds knight by hull color, then open the coin pouches
def pickpocket_loop():
    global isZoomed
    time.sleep(random.uniform(0.37, .99))
    # Only zoom in on loop if screen isn't already zoomed in
    if not isZoomed:
        cf.screen_scroll(coords.zoom_bar_4)
        isZoomed = True
    timer = time.monotonic()
    while time.monotonic() < timer + COIN_POUCH_MAX:
        time.sleep(random.uniform(0.03, 0.79))
        knight_position = find_colored_hull_center_fast_crop(HULL_COLOR, TOLERANCE, GAME_SCREEN)
        if knight_position:
            cf.move_and_click(knight_position, random.uniform(.1, .27), random.uniform(.19, .37))
            time.sleep(random.uniform(0.09, 0.29))
            gui.click()
        else:
            find_knight()
    # Open coin pouch
    open_coin_pouch()


def run():
    start_time = time.monotonic()
    while time.monotonic() < start_time + RUN_TIME:
        pickpocket_loop()
    time.sleep(3)
    cf.logout()