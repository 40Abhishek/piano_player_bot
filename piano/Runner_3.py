import pyautogui
from keyboard import press,is_pressed
from time import sleep
'''
timer:
mins, secs=divmod(t,60)
time.sleep(1)
t+=1
now=mins,secs

import pyautogui
pyautogui.displayMousePosition()

START:
X:    0 Y:  570 
X:  264 Y:  570
X:  264 Y:  684

LOBBY:
X:    0 Y:   63
X:    0 Y:  114
X:  253 Y:  113
X:  251 Y:   63

region=(36,616,200,85)
'''
'''
EXIT:
1. exit(l bottom)
2. continue(right bottom)(30 sec)
3. continue(r bottom)(10 sec)
4. lobby(r bottom)
5. start
'''
def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.PAUSE=0.2
    pyautogui.click(x,y)

def starter():
    while 1:
        sleep(5)
        if pyautogui.locateOnScreen('start_button.png',region=(0,570,264,120),confidence=0.6)!= None:
            #X:  136 Y:  615 
            click(136,615)
            print('found start')
            sleep(1)
            return


def lobby():
    print('entering lobby')
    #sleep(40)
    sleep(40)
    while 1:
        if pyautogui.locateOnScreen('killed.png',region=(0,63,253,60),confidence=0.7)!= None:
            #sleep(50)
            print('sleeping')
            sleep(50)
            #X:  282 Y:  327
            click(282,327)
            print('jumped')
            break
    sleep(2)
    #moving down
    #X: 1167 Y:  458
    pyautogui.moveTo(1167,458)
    pyautogui.drag(0,100,0.7,button='left')
    sleep(0.03)
    #press('w')
    #controller X:  218 Y:  460
    pyautogui.moveTo(218,460)
    pyautogui.drag(0,-400,25,button='left')      
    while 1:
        #change for fast landing
        #sleep(70)
        sleep(0.07)
        print('finding emot')
        #X: 1257 Y:  602
        #X: 1016 Y:   68
        if pyautogui.locateOnScreen('landed.png',region=(1016,65,70,70),confidence=0.4)!= None:
            print('landed')
            sleep(5)
            click(1207,602)
            print('now prone')
            #sleep(30)
            sleep(30)
            return

def find():
    #playzone image checker
    #moving up
    #X: 1167 Y:  458
    pyautogui.moveTo(1167,458)
    pyautogui.drag(0,-100,0.7,button='left')
    valu=0
    while 1:
        #moving left
        #X: 1167 Y:  458
        pyautogui.moveTo(1167,458)
        pyautogui.drag(-150,0,0.7,button='left')
        #X:  545 Y:   67
        #X:  811 Y:   67
        #X:  681 Y:  140
        if pyautogui.locateOnScreen('playzone.png',region=(545,67,270,70),confidence=0.4)!= None:
            return True
        elif valu==8:
            return True
        sleep(2)
        valu+=1

def check():
    while True:
        if pyautogui.locateOnScreen('playzone.png',region=(603,71,100,40),confidence=0.5)== None:
            return False
        sleep(2)

        
def move():
    #move towards playzone(crouch)
    click(270,150)
    #X: 1130 Y:  223(sprint)
    click(675,613)
    #move until playzone disapear
    while True:
        sleep(5)
        if check()==False:
            #sprint
            click(675,613)
            click(270,150)
            return

def death():
    #check if things on screen are not there
    print('checking death')
    valu=0
    while 1:
        #X:  136 Y:  100
        if pyautogui.locateOnScreen('dead1.png',region=(136,100,200,50),confidence=0.4)!= None:
            sleep(5)
            #first button X:  989 Y:  634
            click(989,634)
            print('exit')
            for i in range(2):
                sleep(10)
                #X: 1138 Y:  635 
                click(1138,635)
                print('continue/lobby')
                return 1
        elif valu==3:
            return
                
        else:
            valu+=1
            sleep(1)

def run():
    pass

def color():
    #0= red,1=green,2=blue
    #if pyautogui.pixel('coordinates')[0]=='':
    pass

def momentum():
    count=1
    while True:
        if count==1:
            #4.30 min(270 sec)
            sleep(270)
            #X: 270 Y:  150 crouch click
            #jump X: 1249 Y:  496
            click(1250,500)
            if find()==True:
                move()
                count+=1
            if death()==1:
                return
            
        elif count==2:
            print('initiating zone II')
            #140
            sleep(1)
            click(1102,613)
            if find()==True:
                move()
                count+=1
            if death()==1:
                return
            
            
        elif count==3:
            print('initiating zone III')
            #90
            sleep(1)
            click(1102,613)
            if find()==True:
                move()
                count+=1
            if death()==1:
                return

        elif count==4:
            print('initiating zone IV')
            #not set
            sleep(1)
            click(1102,613)
            if find()==True:
                move()
                count+=1
            if death()==1:
                return

        elif count==5:
            print('initiating zone V')
            #not set
            sleep(1)
            click(1102,613)
            if find()==True:
                move()
                count+=1
            if death()==1:
                return

        elif count==6:
            print('initiating zone VI')
            #not set
            sleep(1)
            click(1102,613)
            if find()==True:
                move()
                count+=1
            if death()==1:
                return
            
        elif count==7:
            print('initiating zone VII')
            #not set
            sleep(1)
            click(1102,613)
            while True:
                if death()==1:
                    return
                sleep(10)
                
def game():
    while 1:
        starter()
        lobby()
        momentum()
        print()
        sleep(3)


if __name__=='__main__':
    game()
