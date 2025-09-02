import sys
import time
import threading
import pyautogui as gui
import random

import ArdyAgilityCourse
import ArdyKnightsWithFood
import ArdyKnightsNoFood
import BrimhavenAgility
import FishStall
import GrayChins
import HosidiousCooking
import KarambwanFishing
import NMZ
import SandCrabCave
import common_functions as cf

NEEDS_LOGIN = False

if __name__ == '__main__':
    time.sleep(2)
    if NEEDS_LOGIN:
        cf.login()
    #cf.print_mouse_tk()
    #HosidiousCooking.run()
    GrayChins.run()
    #KarambwanFishing.run()
    #ArdyAgilityCourse.run()
    #BrimhavenAgility.run()
    #NMZ.run()
    #SandCrabCave.Run()
    #ArdyKnights3.run()
    #ArdyKnightsNoFood.run()
    #FishStall.Run()