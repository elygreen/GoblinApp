import sys
import time
import threading
import pyautogui as gui

import common_functions as cf
import coordinates as coords

def Run():
    # Setup getting to location
    time.sleep(5)
    cf.click_compass()
    cf.move_and_click((978, 397), 1, 5)       # entrance > s1
    cf.move_and_click((772, 293), 1, 5)       # s1 > s2
    cf.move_and_click((983, 424), 1, 5)       # s2 > s3
    cf.move_and_click((749, 374), 1, 3)       # s3 > s4
    # First AFK set
    cf.move_and_click((771, 291), 1, 3)       # s4 > afk
    cf.wait_aggro_timer()
    while True:
        # Second AFK Set
        cf.move_and_click((753, 135), 1, 5)   # afk > s5
        cf.move_and_click((524, 328), 1, 5)   # s5 > s2
        cf.move_and_click((983, 424), 1, 5)   # s2 > s3
        cf.move_and_click((749, 374), 1, 5)   # s3 > s4
        cf.move_and_click((771, 291), 1, 5)   # s4 > afk
        cf.wait_aggro_timer()