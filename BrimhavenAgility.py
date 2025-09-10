import time
import pyautogui as gui
import random

import common_functions as cf
import coordinates as coords

DEFAULT_TOLERANCE = 5
RUN_TIME = 5.4


def start():
    cf.start_script(need_login=True, screen_scroll_value=3, need_click_compass=True, need_angle_up=True)
    time.sleep(3)


def enter_arena():
    # Find entrance npc by colored hull tag
    captain_izzy_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if not captain_izzy_location:
        cf.screen_scroll(coords.zoom_bar_max)
        while not captain_izzy_location:
            captain_izzy_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK,
                                                                DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
            time.sleep(3)
    cf.move_and_click(captain_izzy_location, -1, 3)
    # 90 second wait period to enter mandated by game
    time.sleep(90)
    ladder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    if not ladder_location:
        cf.screen_scroll(coords.zoom_bar_max)
        while not ladder_location:
            ladder_location = cf.find_colored_hull_center(cf.HULL_COLOR_GREEN,
                                                          DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
            time.sleep(3)
    cf.move_and_click(ladder_location, -1, 3)
    cf.screen_scroll(coords.zoom_bar_1)
    time.sleep(2)


def get_to_obstacle():
    obstacle_location = cf.find_colored_hull_center(cf.HULL_COLOR_PINK, DEFAULT_TOLERANCE, cf.DEFAULT_GAME_SCREEN)
    cf.move_and_click(obstacle_location, -1, 8)
    cf.move_and_click([720, 450], -1, 8)
    cf.move_and_click([587, 332], -1, 5)
    cf.screen_scroll(coords.zoom_bar_5)
    gui.press("/")


def auto_click():
    time.sleep(1.5)
    cf.move_and_click((989, 360), -1, -1)
    time_start = time.monotonic()
    while time.monotonic() < time_start + RUN_TIME * 60 * 60:
        time.sleep(random.uniform(0.27, 0.47))
        gui.click()


def finish():
    gui.press("/")
    cf.logout()


def run():
    start()
    enter_arena()
    get_to_obstacle()
    auto_click()
    finish()
