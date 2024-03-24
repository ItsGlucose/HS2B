import pyautogui
import time


Farming = True
pyautogui.FAILSAFE = False

time.sleep(5)


while True:
    if Farming:
        
        pyautogui.keyDown("w")
        pyautogui.mouseDown(button='left')
        
        for i in range(6):
            pyautogui.keyDown('a')
            time.sleep(44)
            pyautogui.keyUp('a')
            time.sleep(0.2)
            
            pyautogui.keyDown('d')
            time.sleep(44)
            pyautogui.keyUp('d')
            time.sleep(0.2)


        Farming = False

    else:
        
        pyautogui.press('t')
        pyautogui.typewrite("/warp garden", interval=0.03)
        pyautogui.press('enter')


        Farming = True

    
    time.sleep(0.2)
