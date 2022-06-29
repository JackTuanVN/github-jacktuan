from email import message
import pyautogui as gui
import time

message = input("Enter the message: ")
numberValue = input("Enter the number: ")

time.sleep(4)

for i  in range(int(numberValue)):
    gui.typewrite(str(i+1) + ". " + message)
    gui.press('Enter')