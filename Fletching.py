import time
import pyautogui as gui
import random

import common_functions as cf
import coordinates as coords

####################
###    SET UP    ###
####################
# Knife in inventory in slot 1
# Next to highlighted bank
# Logs in bottom right of bank

DEFAULT_TOLERANCE = 5
FLETCHING_UI_SLOT = 3
log_slot = (996, 452)

def start(needs_login):
    pass
    #cf.start_script(need_login=needs_login, screen_scroll_value=5, need_click_compass=True, need_angle_up=True)


def bank():
    bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    while not bank_location:
        print("searching for fishing spot")
        time.sleep(3)
        bank_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(bank_location, -1, -1)
    cf.move_and_click(coords.inventory_slot[random.randint(2, 23)], -1, -1)
    cf.move_and_click(log_slot, -1, -1, precision=3)
    gui.press("esc")


def fletching_loop():
    knife_slot = coords.inventory_slot[0]
    log_to_fletch_slot = coords.inventory_slot[random.randint(2, 23)]
    cf.move_and_click(knife_slot, -1, -2, precision=2)
    cf.move_and_click(log_to_fletch_slot, -1, -2, precision=2)
    time.sleep(.9)
    gui.press(str(FLETCHING_UI_SLOT))
    time.sleep(random.uniform(50, 53))

def finish():
    cf.logout()


def run(needs_login, script_run_time):
    start(needs_login)
    start_time = time.monotonic()
    while start_time < time.monotonic() + script_run_time:
        bank()
        fletching_loop()
    finish()
