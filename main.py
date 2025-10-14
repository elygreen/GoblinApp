import sys
import time
import threading
import pyautogui as gui
import random

import ArdyAgilityCourse
import ArdyKnightsNoFood
import BrimhavenAgility
import Fletching
import GrayChins
import HosidiousCooking
import KarambwanFishing
import NMZ
import SandCrabCave
import common_functions as cf

#TODO: Update NMZ, NMZ.py, SandCrabCave.py

needs_login = False
script_run_time = 5.1


def auto_alch():
    while True:
        gui.click()
        sleep_time = random.uniform(.37, .57)
        time.sleep(sleep_time)


if __name__ == '__main__':
    time.sleep(2)
    script_total_run_time = script_run_time * 60 * 60
    #cf.print_mouse_tk(needs_login, script_run_time)
    #HosidiousCooking.run(needs_login, script_run_time)
    #GrayChins.run(needs_login, script_run_time)
    #KarambwanFishing.run(needs_login, script_run_time)
    #ArdyAgilityCourse.run(needs_login, script_run_time)
    #BrimhavenAgility.run(needs_login, script_run_time)
    #NMZ.run(needs_login, script_run_time)
    #SandCrabCave.Run(needs_login, script_run_time)
    #ArdyKnightsNoFood.run(needs_login, script_run_time)
    auto_alch()
