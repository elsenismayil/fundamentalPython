import pywhatkit
import pyautogui
import time

number = "write number"

pywhatkit.sendwhatmsg_instantly(number, "", wait_time=10)

time.sleep(3)

for i in range(100):
    pyautogui.write("write message")
    pyautogui.press("enter")
    time.sleep(0.2)   # 0.2 saniyə fasilə