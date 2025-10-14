import time
import random
import pyautogui as gui
import tkinter as tk
import numpy as np
import cv2

import coordinates as coords

HULL_COLOR_PINK = (255, 9, 154)
HULL_COLOR_GREEN = (0, 255, 29)
HULL_COLOR_BLUE = (19, 9, 255)
HULL_COLOR_TEAL = (9, 255, 194)
HULL_COLOR_ORANGE = (255, 130, 9)

# Coordinates of game screen on full screen Runelite application for my specific laptop,
# your coordinates will vary!
DEFAULT_GAME_SCREEN = (368, 30, 1136, 540)
DEFAULT_IMAGE_MATCH_THRESHOLD = .75

def angle_up():
    gui.moveTo(coords.middle_screen[0], coords.middle_screen[1], -1)
    gui.keyDown('up')
    time.sleep(3)
    gui.keyUp('up')

def click_compass():
    move_and_click(coords.compass, 1, -1)


def login():
    move_and_click(coords.disconnected, -1, -1)
    move_and_click(coords.play_now, 1, 8)
    move_and_click(coords.click_here_to_play, 1, 3)


def logout():
    move_and_click((1329, 765), -1, -1)
    current_time = time.monotonic()
    while time.monotonic() < current_time + 10:
        move_and_click((1323, 670), -1, -1)
        time.sleep(1)


def move_and_click(coordinate, sec=1, wait=0, click_type=0, precision=0):
    if sec == -1:
        sec = random.uniform(0.17, .37)
    if wait == -1:
        wait = random.uniform(0.17, .37)
    if wait == -2:
        wait = random.uniform(0.37, .57)
    offset_x = 0
    offset_y = 0
    if precision != 0:
        if precision == -1:
            precision = 5
        offset_x = random.randint(-precision, precision)
        offset_y = random.randint(-precision, precision)
    gui.moveTo(coordinate[0]+offset_x, coordinate[1]+offset_y, sec)
    if click_type == 0:
        gui.click()
    else:
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
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.7)
    root.wm_attributes('-transparentcolor', 'black')
    root.geometry('200x30+100+100')
    label = tk.Label(root, text="Mouse: (0, 0)", fg='white', bg='black', font=('Arial', 12))
    label.pack()

    def update_mouse_position():
        x, y = gui.position()
        label.config(text=f"Mouse: ({x}, {y})")
        root.after(1000, update_mouse_position)

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


def minimap_scroll(scroll_direction = 1):
    gui.moveTo(coords.MINIMAP_RIGHT_SIDE_COORD)
    start_time = time.monotonic()
    while time.monotonic() < start_time + 3:
        match scroll_direction:
            case -1:
                gui.scroll(-300)
            case _:
                gui.scroll(300)


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
        screenshot = gui.screenshot(region=(left, top, right-left, bottom-top))
        offset_x, offset_y = left, top
    else:
        screenshot = take_screenshot()
        offset_x, offset_y = 0, 0
    img_array = np.array(screenshot)

    if tolerance == 0:
        mask = np.all(img_array == target_color, axis=2)
    else:
        diff = np.abs(img_array - target_color)
        mask = np.all(diff <= tolerance, axis=2)

    # Find matching coordinates
    matching_coords = np.where(mask)

    if len(matching_coords[0]) == 0:
        return None

    center_y = int(np.mean(matching_coords[0]).item()) + offset_y
    center_x = int(np.mean(matching_coords[1]).item()) + offset_x

    return center_x, center_y


def find_first_colored_pixel(target_color, tolerance=0, search_area=None):
    if search_area:
        left, top, right, bottom = search_area
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
        diff = np.abs(img_array - target_color)
        mask = np.all(diff <= tolerance, axis=2)

    # Find matching coordinates
    matching_coords = np.where(mask)

    if len(matching_coords[0]) == 0:
        return None

    first_y = matching_coords[0][0] + offset_y
    first_x = matching_coords[1][0] + offset_x
    return first_x, first_y


def load_image_template(template_path):
    try:
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        if template is None:
            raise ValueError(f"Could not load template from {template_path}")
        return template
    except Exception as e:
        print(f"Error loading template: {e}")
        return None


def find_template_on_screen(template, search_area=None, threshold=DEFAULT_IMAGE_MATCH_THRESHOLD):
    try:
        if search_area:
            left, top, right, bottom = search_area
            screenshot = gui.screenshot(region=(left, top, right-left, bottom-top))
            offset_x, offset_y = left, top
        else:
            screenshot = take_screenshot()
            offset_x, offset_y = 0, 0
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            template_h, template_w = template.shape[:2]
            center_x = max_loc[0] + template_w // 2 + offset_x
            center_y = max_loc[1] + template_h // 2 + offset_y
            print(f"Found fallen trap at ({center_x}, {center_y}) with confidence {max_val:.3f}")
            return center_x, center_y
        else:
            print(f"No fallen trap found (best match: {max_val:.3f}, threshold: {threshold})")
            return None
    except Exception as e:
        print(f"Error in template matching: {e}")
        return None


def start_script(need_login=False, screen_scroll_value=3, need_click_compass=False, need_angle_up=True, scroll_minimap=0):
    if need_login:
        login()

    match screen_scroll_value:
        case 1:
            screen_scroll(coords.zoom_bar_1)
        case 2:
            screen_scroll(coords.zoom_bar_2)
        case 3:
            screen_scroll(coords.zoom_bar_middle)
        case 4:
            screen_scroll(coords.zoom_bar_4)
        case 5:
            screen_scroll(coords.zoom_bar_5)
        case _:
            pass

    if need_click_compass:
        click_compass()

    if need_angle_up:
        angle_up()

    if scroll_minimap != 0:
        minimap_scroll(scroll_minimap)