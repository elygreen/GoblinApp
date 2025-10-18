import time
import pyautogui as gui
import random

import common_functions as cf
import coordinates as coords

DEFAULT_TOLERANCE = 5
BANK_BOTTOM_RIGHT_SLOT = (999, 453)
RUN_WAIT_TIME = 3.7
INVENTORY_COOK_TIME = 65

first_bank = True

####################
###    SET UP    ###
####################
# Start at sandstone mine
# Have empty inventory

grinder_to_rock_wait_time = 7.5

def start(needs_login):
    cf.start_script(need_login=needs_login, screen_scroll_value=1, need_click_compass=True, need_angle_up=True)


def mining_wait_time():
    return random.uniform(2.3, 3.0)


def mining_loop():
    rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    while rock_location is None:
        rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        time.sleep(2)
    cf.move_and_click(rock_location, -1, grinder_to_rock_wait_time)

    for i in range(6):
        rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        if rock_location:
            cf.move_and_click(rock_location, -1, mining_wait_time(), precision=2)

        rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_BLUE, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        if rock_location:
            cf.move_and_click(rock_location, -1, mining_wait_time(), precision=2)

        rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_ORANGE, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        if rock_location:
            cf.move_and_click(rock_location, -1, mining_wait_time(), precision=2)

        rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_TEAL, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        if rock_location:
            cf.move_and_click(rock_location, -1, mining_wait_time(), precision=2)


def grinder():
    grinder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    while grinder_location is None:
        grinder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        time.sleep(2)
    cf.move_and_click(grinder_location, -1, grinder_to_rock_wait_time)


def finish():
    cf.logout()


def run(needs_login, script_run_time):
    start(needs_login)
    start_time = time.monotonic()
    while time.monotonic() < start_time + script_run_time:
        mining_loop()
        grinder()
    finish()
