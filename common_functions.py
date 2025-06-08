import sys
import time
import random
import threading
import pyautogui as gui
import tkinter as tk

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