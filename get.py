from pynput import keyboard
import pyautogui as pui
pui.FAILSAFE = False

def on_activate_1():
    print('1 active')
    pui.moveTo(0,0)

def on_activate_2():
    print('2 active')
    pui.moveTo(1919,0)

def on_activate_3():
    print('3 active')
    pui.moveTo(1919,1079)

def on_activate_4():
    print('4 active')
    pui.moveTo(0,1079)

with keyboard.GlobalHotKeys({
        '<f1>+1': on_activate_1,
        '<f1>+2': on_activate_2,
        '<f1>+3': on_activate_3,
        '<f1>+4': on_activate_4}) as h:
    h.join()