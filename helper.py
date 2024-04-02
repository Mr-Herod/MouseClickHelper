import pyautogui as ag
import time

click_pos = []
waiting_time = 3600 

def init():
    ag.PAUSE = 1  # 每次gui操作 间隔1s

def moveAndClick(pos,click = True):
    ag.moveTo(pos[0],pos[1],duration=1)
    if click:
        ag.click()

def addClick(click_pos):   
    pos_in = input("请输入想要点击的坐标（x,y）：").replace("，",",").replace("(","").replace(")","").replace("（","").replace("）","")
    x = int(pos_in.split(",")[0])
    y = int(pos_in.split(",")[1])
    click_pos.append((x,y))
    print("当前记录的点击坐标：",click_pos)
    return click_pos

def preView(pos_list): 
    print("当前设置的等待时间：",waiting_time,"s")
    for pos in pos_list:
        moveAndClick(pos,False)

def showPos(): 
    try: 
        while True: 
            print("当前坐标(按 Ctrl + c 结束显示)：",ag.position())
            time.sleep(1)
    except:
         return

def setWatingTime():
    t = int(input("请输入等待时间(S),如\"1小时\"输入 3600 即可:"))
    waiting_time = t
    return waiting_time

def doWait(click_pos,waiting_time):
    time_left = waiting_time
    while time_left > 0:
        print("剩余时间：",time_left,"s")
        time.sleep(3)
        time_left -= 3

    for pos in click_pos:
        moveAndClick(pos,True)

def showMenu():
    print("********************************") 
    print("*       1.显示当前坐标          *")
    print("*       2.添加点击操作          *")
    print("*       3.设置等待时间          *")
    print("*       4.预览点击区域          *")
    print("*       5.开始运行              *")
    print("*       6.退出                  *")
    print("********************************")

if __name__ == "__main__":
    init()
    while True:
        try:
            showMenu()
            op = int(input()) 
            if op == 1: 
                    showPos()  
            elif op == 2:
                    click_pos = addClick(click_pos)  
            elif op == 3:
                    waiting_time = setWatingTime()
            elif op == 4:
                    preView(click_pos)
            elif op == 5:
                    doWait(click_pos,waiting_time)
            elif op == 6:
                    print("拜拜")
                    time.sleep(3)
                    exit(0)
            else:
                print("输入错误。。。请重试")
        except Exception as e:
            print("程序错误：", str(e))
            time.sleep(5)
            continue