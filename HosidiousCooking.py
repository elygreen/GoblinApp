import time
import pyautogui as gui
import random

import common_functions as cf
import coordinates as coords

DEFAULT_TOLERANCE = 5
RUN_TIME = 4.5
BANK_BOTTOM_RIGHT_SLOT = (999, 453)
RUN_WAIT_TIME = 3.7
INVENTORY_COOK_TIME = 65

first_bank = True

####################
###    SET UP    ###
####################
# item you want to cook in bottom most right slot of first page of bank
# bank chest is green
# range is pink
# start in hosidious kitchen


def start():
    cf.login()
    cf.screen_scroll(coords.zoom_bar_2)
    cf.click_compass()
    cf.angle_up()


def first_time_banking():
    bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(bank_location, -1, RUN_WAIT_TIME)
    gui.write("9149", interval=0.27)
    cf.move_and_click(coords.bank_withdraw_quantity_all, -1, -1)
    cf.move_and_click(coords.bank_deposit_all, -1, -1)
    cf.move_and_click(BANK_BOTTOM_RIGHT_SLOT, -1, -1)
    gui.press("esc")


def cook():
    stove_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(stove_location, -1, RUN_WAIT_TIME)
    gui.write("1")
    time.sleep(INVENTORY_COOK_TIME + random.uniform(0.0, 2.0))


def bank():
    bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(bank_location, -1, RUN_WAIT_TIME)
    cf.move_and_click(coords.bank_deposit_all, -1, -1)
    cf.move_and_click(BANK_BOTTOM_RIGHT_SLOT, -1, -1)
    gui.press("esc")


def finish():
    cf.logout()


def run():
    start()
    first_time_banking()
    start_time = time.monotonic()
    while time.monotonic() < start_time + RUN_TIME * 60 * 60:
        cook()
        bank()
