import os
from PIL import Image
import time

def getScreen():
    os.system('D:\\platform-tools\\adb.exe shell screencap -p /sdcard/1.png')
    os.system('D:\\platform-tools\\adb.exe pull /sdcard/1.png .')

def jump(distance):
    magicNum = 1.592  # 按压时间系数    magic power!!

    swipe_x1, swipe_y1, swipe_x2, swipe_y2 = 100, 100, 100, 100  # 按的坐标
    pressTime = distance * magicNum
    pressTime = int(pressTime)
    cmd = 'D:\\platform-tools\\adb.exe shell input swipe {} {} {} {} {}'.format(swipe_x1, swipe_y1, swipe_x2, swipe_y2, pressTime)
    os.system(cmd)
def FindChess(im):
    for y in range(310,h):
        for x in range(w):
            pixel = im.getpixel((x, y))
            #寻找独一无二的一个像素点
            if (pixel[0]==64) and(pixel[1]==50) and (pixel[2]==87):
                return x
            else:
                pass

def FindBoard(im,chessX):
    backColor = im.getpixel((100,100))

    for y in range(310,h):
        for x in range(w):


            if abs(chessX-x)<=50:
                continue
            #防止出现比chess还要低的board


            pixel = im.getpixel((x, y+5))

            colorRange = 20
            #背景色波动范围

            if(abs(pixel[0]-backColor[0])+abs(pixel[1]-backColor[1])+abs(pixel[2]-backColor[2]) <colorRange):
                #更新背景颜色
                backColor=im.getpixel((x,y))
            else:
                return x

if __name__ == '__main__':
    while True:
        time.sleep(2.5)
        #保证跳跃完毕 获得分数

        getScreen()
        im = Image.open("./1.png")
        w,h = im.size
        chess = FindChess(im)
        board = FindBoard(im,chess)
        if chess==None:
            #没找到chess
            break
        print("Chess",chess,"Board",board)
        distance = abs(chess-board)
        print("jump distance ",distance)
        jump(distance)