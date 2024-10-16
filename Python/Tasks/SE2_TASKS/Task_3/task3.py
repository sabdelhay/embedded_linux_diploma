#!/usr/bin/python3

import pyautogui
import time

def open_vscode():
    pyautogui.press('win')
    time.sleep(2)

    pyautogui.write('Visual Studio Code')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)

def install_extensions(ext_name):
    pyautogui.hotkey('ctrl', 'shift', 'p')
    pyautogui.write('Install Extensions')
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(5)
    pyautogui.write(ext_name)
    pyautogui.press('enter')                                    
    time.sleep(10)
    
    try:
        install_btn = pyautogui.locateOnScreen('install_btn.png', confidence=0.9)
        if install_btn:
            button_x = install_btn.left + install_btn.width // 2
            button_y = install_btn.top + install_btn.height // 2

            pyautogui.click(button_x, button_y)
            print(f"Installing {ext_name}...")
            time.sleep(10)
        else:
            print(f"Install button not found for {ext_name}, or the extension is already installed.")
    except:
        print(f"Couldn't find install button for {ext_name}. Skipping.")

    time.sleep(15)