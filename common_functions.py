import sys
import time
import random
import threading
import pyautogui as gui
import tkinter as tk

import coordinates as coords

def angle_up():
    gui.moveTo(coords.middle_screen[0], coords.middle_screen[1], 1)
    gui.keyDown('up')
    time.sleep(3)
    gui.keyUp('up')

def click_compass():
    move_and_click(coords.compass, 1, 1)


def login():
    move_and_click(coords.play_now, 1, 10)
    move_and_click(coords.click_here_to_play, 1, 4)

def move_and_click(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = round(random.uniform(0.37, .61), 2)
    if wait == -1:
        wait = round(random.uniform(0.9, 1.3), 2)
    gui.moveTo(coordinate[0], coordinate[1], sec)
    gui.click()
    time.sleep(wait)

def move_and_rightclick(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = round(random.uniform(0.7, 1.1), 2)
    if wait == -1:
        wait = round(random.uniform(0.9, 1.3), 2)
    gui.moveTo(coordinate[0], coordinate[1], sec)
    gui.rightClick()
    time.sleep(wait)

def move_and_click_variable_coord(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = round(random.uniform(0.7, 1.1), 2)
    if wait == -1:
        wait = round(random.uniform(0.9, 1.3), 2)
    varied_coordinate_x = coordinate[0] + random.randint(-7, 7)
    varied_coordinate_y = coordinate[1] + random.randint(-7, 7)
    gui.moveTo(varied_coordinate_x, varied_coordinate_y, sec)
    gui.click()
    time.sleep(wait)


def move_and_rightclick_variable_coord(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = round(random.uniform(0.7, 1.1), 2)
    if wait == -1:
        wait = round(random.uniform(0.9, 1.3), 2)
    varied_coordinate_x = coordinate[0] + random.randint(-7, 7)
    varied_coordinate_y = coordinate[1] + random.randint(-7, 7)
    gui.moveTo(varied_coordinate_x, varied_coordinate_y, sec)
    gui.rightClick()
    time.sleep(wait)

def second_rng(lower=0.7, upper=1.1):
    return round(random.uniform(lower, upper), 2)

def wait_rng(lower=0.9, upper=1.3):
    return round(random.uniform(lower, upper), 2)

def print_mouse():
    while True:
        time.sleep(1)
        print(gui.position())

def print_mouse_tk():
    root = tk.Tk()
    root.overrideredirect(True)  # Removes title bar/borders
    root.attributes('-topmost', True)  # Stays on top
    root.attributes('-alpha', 0.7)  # Semi-transparent
    root.wm_attributes('-transparentcolor', 'black')  # Make background transparent
    root.geometry('200x30+100+100')
    label = tk.Label(root, text="Mouse: (0, 0)", fg='white', bg='black', font=('Arial', 12))
    label.pack()

    def update_mouse_position():
        # Get mouse position using pyautogui
        x, y = gui.position()
        # Update label text
        label.config(text=f"Mouse: ({x}, {y})")
        # Schedule next update (every 1000ms = 1 second to match your original timing)
        root.after(1000, update_mouse_position)

    # Start updating mouse position
    update_mouse_position()

    root.mainloop()


def scroll_in():
    click_compass()
    gui.moveTo((coords.middle_screen[0], coords.middle_screen[1]), 1, 1)
    scrollTime = time.monotonic() + 5
    while time.monotonic() < scrollTime:
        gui.scroll(100)


def scroll_out():
    click_compass()
    gui.moveTo((coords.middle_screen[0], coords.middle_screen[1]), 1, 1)
    scrollTime = time.monotonic() + 5
    while time.monotonic() < scrollTime:
        gui.scroll(-100)
    time.sleep(1)


def scroll_medium():
    move_and_click(coords.tab_settings, 1, 1)
    move_and_click(coords.tab_settings_zoom, 1, 1)
    move_and_click(coords.zoom_bar_middle, 1, 1)
    move_and_click(coords.tab_inventory, 1, 1)


def compass_scroll_in():
    gui.moveTo(coords.minimap_middle[0], coords.minimap_middle, 1)
    scrollTime = time.monotonic() + 5
    while time.monotonic() < scrollTime:
        gui.scroll(100)
    time.sleep(1)


def compass_scroll_out():
    gui.moveTo(coords.minimap_middle[0], coords.minimap_middle[1], 1)
    scrollTime = time.monotonic() + 5
    while time.monotonic() < scrollTime:
        gui.scroll(-100)
    time.sleep(1)


def wait_aggro_timer():
    wait_time = random.uniform(610, 630)
    time.sleep(wait_time)