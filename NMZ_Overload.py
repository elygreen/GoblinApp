import common_functions as cf
import coordinates as coords
import pyautogui as gui
import math
import random
import time

####################
### REQUIREMENTS ###
####################
# Entity Hider: OFF
# NPC Attack Option: Always Right Click
# Rock cake left click set to guzzle
# Quick prayer set to rapid flick
# NMZ settup correctly
# 1. Starting position: NMZ start square
# 2. Inventory Layout:
#   - First slot: Rock Cake
# LOTS OF MONEY IN COFFER

coord_Dom = (751, 236)
NMZ_start_to_NMZ_1 = (429, 305)
NUM_OVERLOADS = 6
POTION_DOSES = 4
NUM_ABSORBTIONS_PER_OVERLOAD = math.ceil((27 - 1 - NUM_OVERLOADS) / NUM_OVERLOADS)
NUM_INITIAL_ABSORPTIONS = 1

def Dom():
    time.sleep(2)
    cf.move_and_click(coord_Dom, 1, 3)
    # Select Previous: Customisable Rumble (hard)
    gui.write("4")
    time.sleep(2)
    gui.press("space")
    time.sleep(2)
    # Agree to pay 26,000 coins? Yes
    gui.write("1")
    time.sleep(2)
    gui.press("space")
    time.sleep(2)
    # Move from NMZ start to NMZ 1
    cf.move_and_click((438, 297), -1, 5)

def deposit_potions():
    # Right click Overload barrel
    cf.move_and_rightclick_variable_coord((661, 236), -1, -1)
    # Click store and press "Yes, please."
    cf.move_and_click((672, 326), -1, 2)
    gui.write("1")
    # Right click Absorbtion barrel
    cf.move_and_rightclick_variable_coord((707, 234), -1, -1)
    # Click store and press "Yes, please."
    cf.move_and_click((727, 312), -1, 2)
    gui.write("1")
    # Go back to NMZ 1
    cf.move_and_click_variable_coord((800, 386), -1, cf.wait_rng(2.1, 3.1))


def take_potions():
    # Character should be standing on NMZ 1
    # Right click Overload barrel, click take, take out 6 (24 doses) overloads
    cf.move_and_rightclick_variable_coord((661, 236), -1, -1)
    cf.move_and_click((646, 298), -1, 2.3)
    doses = NUM_OVERLOADS * 6
    gui.write(str(doses), interval=0.27)
    gui.press("enter")
    time.sleep(1.3)
    # Right click Absorbtion barrel, click take, take out full inv of absorbtions
    cf.move_and_rightclick_variable_coord((707, 234), -1, -1)
    cf.move_and_click((677, 296), -1, 2.1)
    gui.write("999999", interval=0.27)
    gui.press("enter")


def enter_nmz():
    # Character should be standing on NMZ 2
    # click drink potion
    cf.move_and_click((966, 295), -1, cf.wait_rng(2.3, 3.7))
    # click accept
    cf.move_and_click_variable_coord((967, 334), -1, 3)
    # run to right corner
    cf.move_and_click_variable_coord((1306, 62), -1, 3)


def Inside_NMZ():
    pot_cycletime = 25 #minutes
    OVERLOAD_DURATION = 60 * 5
    inv_slots = coords.inventory_slot.copy()
    overload_slots = inv_slots[1:(1 + NUM_OVERLOADS)]
    absorption_slots = inv_slots[(1+NUM_OVERLOADS) : (1+NUM_OVERLOADS + (28 - 1 - NUM_OVERLOADS))]
    first_slot = inv_slots[0]

    ### HELPER FUNCTIONS ###
    def spam_rockcake():
        cf.move_and_click(first_slot, -1, -1)
        for j in range(random.randrange(27, 37)):
            time.sleep(random.randrange(17, 43) / 100)
            gui.click()

    def rapid_heal_for_duration(duration):
        gui.moveTo(coords.quick_prayer[0], coords.quick_prayer[1], 1)
        while time.monotonic() < duration:
            gui.click()
            time.sleep(random.uniform(.15, .25))
            gui.click()
            time.sleep(random.uniform(19, 47))
    
    def spam_absorption():
        wait_time = time.monotonic() + 3.5
        while time.monotonic() < wait_time:
            gui.click()
            time.sleep(random.randrange(17, 43) / 100)

    ### START OF NMZ INSIDE CYCLE ###
    # DRINK 6 absorptions right off the bat
    for initial_absorptions in range(NUM_INITIAL_ABSORPTIONS):
        coord = absorption_slots.pop(0)
        gui.moveTo(coord[0], coord[1], 1)
        spam_absorption()

    # Repeat for as many overloads as we have
    for overloads in range(NUM_OVERLOADS):
        # Drink absorptions
        for absorptions in range(NUM_ABSORBTIONS_PER_OVERLOAD):
            if not absorption_slots:
                break
            current_absorption_coord = absorption_slots.pop(0)
            gui.moveTo(current_absorption_coord[0], current_absorption_coord[1], 1)
            spam_absorption()
        # Get current overload position
        current_overload_coord = overload_slots.pop(0)
        # Repeat for 4 doses of overload potion
        for i in range(POTION_DOSES):
            # Sip current overload
            cf.move_and_click_variable_coord(current_overload_coord, -1, -1)
            time.sleep(6)
            current_overload_cycle_end_time = time.monotonic() + (60 * 5)
            # Spam rockcake
            spam_rockcake()
            # Rapid heal for 5 minutes
            rapid_heal_for_duration(current_overload_cycle_end_time)



    


def run():
    time.sleep(3)
    cf.login()
    cf.screen_scroll(coords.zoom_bar_middle)
    cf.compass_scroll_out()
    cf.click_compass()
    cf.angle_up()
    Dom()
    deposit_potions()
    take_potions()
    enter_nmz()
    time.sleep(3)
    Inside_NMZ()


