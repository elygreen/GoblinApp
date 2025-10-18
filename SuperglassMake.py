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
# Legends Guild Bank
# Stand in between the two bank chests
# Bank marked pink
# Runepouch w/ Astrals & Fires, Air staff equipped
# BANK WITHDRAW X SET TO 18
# bottom right bank slot = seaweed
# sand to the left of seaweed
# deposit lock the runepouch in first slot
# bank withdraw set to 1


grinder_to_rock_wait_time = 7.5
coords_seaweed = (997, 454)
coords_sand = (927, 452)
coords_superglass_make = (1302, 503)
coords_pickup_glass = (753, 336)
pickup_time = 25


def bank_wait_time():
    return random.uniform(.27, .37)

def bank():
    bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    while bank_location is None:
        bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
        time.sleep(2)
    cf.move_and_click(bank_location, -1, -1)


def start(needs_login):
    cf.start_script(need_login=needs_login, screen_scroll_value=5, need_click_compass=True, need_angle_up=True)
    cf.move_and_click(coords.tab_magic)


# Superglass loop
def superglass_make():
    bank()
    cf.move_and_click(coords.bank_deposit_all, -1, -1, precision=2)
    for i in range(3):
        cf.move_and_click(coords_seaweed, -1, -1, precision=2)
    gui.keyDown("shift")
    cf.move_and_click(coords_sand, -1, -1, precision=2)
    gui.keyUp("shift")
    gui.press("esc")
    cf.move_and_click(coords_superglass_make, -1, -1, precision=1)


def glass_loop():
    for i in range(5):
        superglass_make()
    bank()
    cf.move_and_click(coords.bank_deposit_all, -1, -1, precision=2)
    gui.press("esc")
    spam_click_start_Time = time.monotonic()
    while time.monotonic() < spam_click_start_Time + pickup_time:
        gui.click()
        sleep_time = random.uniform(.27, .47)
        time.sleep(sleep_time)


def finish():
    cf.logout()


def run(needs_login, script_run_time):
    start(needs_login)
    start_time = time.monotonic()
    while time.monotonic() < start_time + script_run_time:
        glass_loop()
