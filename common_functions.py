import sys
import time
import random
import threading
import pyautogui as gui

import coordinates as coords


def click_compass():
    move_and_click(coords.compass, 1, 1)


def move_and_click(coordinate, sec=1, wait=0):
    gui.moveTo(coordinate[0], coordinate[1], sec)
    gui.click()
    time.sleep(wait)


def print_mouse():
    while True:
        time.sleep(1)
        print(gui.position())


def scroll_out():
    click_compass()
    gui.moveTo(coords.middle_screen[0], coords.middle_screen[1], 1, 1)
    scrollTime = time.monotonic() + 5
    while time.monotonic() < scrollTime:
        gui.scroll(-100)
    time.sleep(1)


def scroll_in():
    click_compass()
    gui.moveTo(coords.middle_screen[0], coords.middle_screen[1], 1, 1)
    scrollTime = time.monotonic() + 5
    while time.monotonic() < scrollTime:
        gui.scroll(100)

def wait_aggro_timer():
    wait_time = random.uniform(610, 630)
    time.sleep(wait_time)