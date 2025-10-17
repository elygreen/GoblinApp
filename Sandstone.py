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

grinder_to_rock_wait_time = 10

def start(needs_login):
    cf.start_script(need_login=needs_login, screen_scroll_value=1, need_click_compass=True, need_angle_up=True)


def mining_wait_time():
    return random.uniform(2.5, 3.2)

def mining_loop():
    rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(rock_location, -1, grinder_to_rock_wait_time)
    for i in range (6):
        rock_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        cf.move_and_click(rock_location, -1, mining_wait_time())
        


def grinder():
    grinder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(grinder_location, -1, grinder_to_rock_wait_time)


def finish():
    cf.logout()


def run(needs_login, script_run_time):
    start(needs_login)
    start_time = time.monotonic()
    while time.monotonic() < start_time + script_run_time:
        mining_loop()
        grinder()
