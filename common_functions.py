import sys
import time
import random
import threading
import pyautogui as gui
import tkinter as tk
import numpy as np

import coordinates as coords


HULL_COLOR_PINK = (255, 9, 154)
HULL_COLOR_GREEN = (0, 255, 29)
# Coordinates of gamescreen on fullscreen Runelite application for my specific laptop,
# your coordinates will vary!
DEFAULT_GAME_SCREEN = (368, 30, 1136, 540)

def angle_up():
    gui.moveTo(coords.middle_screen[0], coords.middle_screen[1], 1)
    gui.keyDown('up')
    time.sleep(3)
    gui.keyUp('up')

def click_compass():
    move_and_click(coords.compass, 1, 1)


def login():
    move_and_click(coords.disconnected, -1, 2)
    move_and_click(coords.play_now, 1, 10)
    move_and_click(coords.click_here_to_play, 1, 4)


def logout():
    move_and_click((1329, 765), -1, -1)
    current_time = time.monotonic()
    while time.monotonic() < current_time + 10:
        move_and_click((1323, 670), -1, -1)
        time.sleep(1)


def move_and_click(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = random.uniform(0.17, .37)
    if wait == -1:
        wait = random.uniform(0.17, .37)
    gui.moveTo(coordinate[0], coordinate[1], sec)
    gui.click()
    time.sleep(wait)


def move_and_rightclick(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = random.uniform(0.7, 1.1)
    if wait == -1:
        wait = random.uniform(0.9, 1.3)
    gui.moveTo(coordinate[0], coordinate[1], sec)
    gui.rightClick()
    time.sleep(wait)


def move_and_click_variable_coord(coordinate, sec=1, wait=0):
    if sec == -1:
        sec = round(random.uniform(0.63, .77), 2)
    if wait == -1:
        wait = round(random.uniform(0.7, 1.0), 2)
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
    move_and_click(coords.tab_settings, -1, -1)
    move_and_click(coords.tab_settings_zoom, -1, -1)
    move_and_click(coords.zoom_bar_min, -1, -1)
    move_and_click(coords.tab_inventory, -1, -1)


def scroll_out():
    move_and_click(coords.tab_settings, -1, -1)
    move_and_click(coords.tab_settings_zoom, -1, -1)
    move_and_click(coords.zoom_bar_max, -1, -1)
    move_and_click(coords.tab_inventory, -1, -1)


def scroll_medium():
    move_and_click(coords.tab_settings, -1, -1)
    move_and_click(coords.tab_settings_zoom, -1, -1)
    move_and_click(coords.zoom_bar_middle, -1, -1)
    move_and_click(coords.tab_inventory, -1, -1)

def scroll_4():
    move_and_click(coords.tab_settings, -1, -1)
    move_and_click(coords.tab_settings_zoom, -1, -1)
    move_and_click(coords.zoom_bar_4, -1, -1)
    move_and_click(coords.tab_inventory, -1, -1)


def screen_scroll(zoom_bar_coords):
    move_and_click(coords.tab_settings, -1, -1)
    move_and_click(coords.tab_settings_zoom, -1, -1)
    move_and_click(zoom_bar_coords, -1, -1)
    move_and_click(coords.tab_inventory, -1, -1)


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


def take_screenshot():
    screenshot = gui.screenshot()
    screenshot.save("screenshot.png")
    return screenshot

def find_colored_hull_center(target_color, tolerance=0, search_area=None):
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