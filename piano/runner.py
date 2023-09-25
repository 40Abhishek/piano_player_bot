import pyautogui
from keyboard import press,is_pressed
from time import sleep
'''
start match corner-X:  450 Y:   86 RGB: ( 56,  61, 114)
click at -120
480,110

X:  548 Y:  245 RGB: (169, 222, 255)

X:  620 Y:  256 RGB: (160, 214, 255)

X:  684 Y:  268 RGB: (  1,   1,   1)

starter --x: 485 Y:  361
'''
def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click(x,y)


def starter():
    while True:
        if pyautogui.pixel(480,360)[0]==1 or pyautogui.pixel(480,360)[1]==2:
            click(480,360)
        elif pyautogui.pixel(548,360)[0]==1 or pyautogui.pixel(548,360)[1]==2:
            click(548,360)
        elif pyautogui.pixel(620,360)[0]==1 or pyautogui.pixel(620,360)[1]==2:
            click(620,360)
        elif pyautogui.pixel(684,360)[0]==1 or pyautogui.pixel(684,360)[1]==2:
            click(684,360)
        else:
            print('failed')


def main():
    starter()


if __name__=='__main__':
    main()
