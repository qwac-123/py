#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *

pygame.init()# 初始化pygame
XXX=pygame.display.list_modes()
size=width,height =1024,768# 设置窗口大小
speed=[2,1]
bg=(255,255,255)
fullscreen=False

cellwidth=width//12
minicellwidth=cellwidth//4
uparrowwidth=2*minicellwidth
uparrowheight=minicellwidth
leftarrowwidth=minicellwidth
leftarrowheight=2*minicellwidth
buttonwidth=7*minicellwidth
minicellheight=2*minicellwidth
startx=width/2-10*minicellwidth
starty=height/2-10*minicellwidth

topminix=startx+5.5*minicellwidth
topminiy=starty
bottomminix=topminix
bottomminiy=starty+19*minicellwidth

leftminix=startx
leftminiy=starty+5.5*minicellwidth
rightminix=startx+19*minicellwidth
rightminiy=starty

toparrowstartx=startx+cellwidth
toparrowstarty=starty+3*minicellwidth
toparrowendx=toparrowstartx+6*uparrowwidth
toparrowendy=toparrowstarty+uparrowheight

leftarrowstartx=startx+3*minicellwidth
leftarrowstarty=starty+cellwidth
leftarrowendx=leftarrowstartx+leftarrowwidth
leftarrowendy=leftarrowstarty+6*leftarrowheight


finishx=height-1*cellwidth
finishy=height-2*cellwidth


clock=pygame.time.Clock()

screen=pygame.display.set_mode(size)# 显示窗口
pygame.display.set_caption('礼法')# 游戏标题

# 准备图片
red=pygame.image.load('red.png')
orange=pygame.image.load('orange.png')
green=pygame.image.load('green.png')
blue=pygame.image.load('blue.png')
purple=pygame.image.load('purple.png')
minired=pygame.image.load('minired.png')
miniorange=pygame.image.load('miniorange.png')
minigreen=pygame.image.load('minigreen.png')
miniblue=pygame.image.load('miniblue.png')
minipurple=pygame.image.load('minipurple.png')
uparrow=pygame.image.load('uparrow.png')
downarrow=pygame.image.load('downarrow.png')
leftarrow=pygame.image.load('leftarrow.png')
rightarrow=pygame.image.load('rightarrow.png')
finish=pygame.image.load('finish.png')
restart=pygame.image.load('restart.png')



uparrow=pygame.transform.scale(uparrow, (2*minicellwidth, minicellwidth))
downarrow=pygame.transform.scale(downarrow, (2*minicellwidth, minicellwidth))
leftarrow=pygame.transform.scale(leftarrow, (minicellwidth, 2*minicellwidth))
rightarrow=pygame.transform.scale(rightarrow, (minicellwidth, 2*minicellwidth))


pics=[red,orange,green, blue, purple, minired, miniorange, minigreen, miniblue, minipurple]
for i in range(5):
    pics[i]=pygame.transform.scale(pics[i], (cellwidth, cellwidth))
    
for i in range(5,10):
    pics[i]=pygame.transform.scale(pics[i], (minicellwidth, minicellwidth))

#red=pygame.transform.scale(red, (cellwidth, cellwidth))

#position=turtle.get_rect()# 获取矩形区域

#初始化数组
matrix = [[9 for i in range(9)] for j in range(9)]#用9避开重复的0
oldmatrix=[[9 for i in range(9)] for j in range(9)]#用9避开重复的0
#deck=['red']*9+['orange']*9+['green']*9+['blue']*9+['purple']*9
deck=[0]*9+[1]*9+[2]*9+[3]*9+[4]*9



#洗牌
def new_game():
    '洗牌'
    random.shuffle(deck)
    matrix[0][3:6]=deck[0:3]
    matrix[1][3:6]=deck[3:6]
    matrix[2][3:6]=deck[6:9]
    matrix[3]=deck[9:18]
    matrix[4]=deck[18:27]
    matrix[5]=deck[27:36]
    matrix[6][3:6]=deck[36:39]
    matrix[7][3:6]=deck[39:42]
    matrix[8][3:6]=deck[42:45]
    oldmatrix=list(matrix)


#判断输赢
def iswin(difficulty,count):
    '判断输赢'
    a=matrix[3][3]
    d=difficulty
    c=count
    #print(d-c)
    win=True
    for i in range(3,6):
        for j in range(3,6):
            #print(matrix[i][j])
            if a!=matrix[i][j]:
                win=False
    if win and d-c>=0:
        return True
    elif d-c<=0:
        return False

           


difficulty=19#30
count=0
condition=None

screen.blit(finish, (width//2+int(minicellwidth), height//2))
                
while True:#死循环确保窗口一直显示
    
    difficulty=19#30
    count=0
    #condition=None
    new_game()


    fontObj2 = pygame.font.SysFont("SimHei", 20)
    textCount = fontObj2.render('还有%d步' % (difficulty-count), False,(0, 0, 0))

    fontObj1 = pygame.font.SysFont("SimHei", cellwidth)
    textWin = fontObj1.render('你赢了！', False,(0, 0, 0))
    #再来吗？

    textLose = fontObj1.render('你输了！', False,(0, 0, 0))

    #textRectObj2 = textCount.get_rect()
    #textRectObj2.center = (cellwidth, cellwidth)


    while condition==True:  # True赢了，False输了，None在进行中
        #screen.blit(textWin, (width//2-int(cellwidth*1.5), height//2-cellwidth*2))
        screen.blit(textLose, (width//2-int(cellwidth*1.5), height//2-cellwidth))
        screen.blit(restart, (width//2-int(cellwidth*1.5), height//2))
        screen.blit(finish, (width//2+int(minicellwidth), height//2))
        
        pygame.display.flip()
        clock.tick(200)
        for event in pygame.event.get():  # 遍历所有事件
            if event.type==pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()


    while condition==False:  # True赢了，False输了，None在进行中
        #screen.blit(textLose, (width//2-int(cellwidth*1.5), height//2-cellwidth//2))
        screen.blit(textLose, (width//2-int(cellwidth*1.5), height//2-cellwidth))
        screen.blit(restart, (width//2-int(cellwidth*1.5), height//2))
        screen.blit(finish, (width//2+int(minicellwidth), height//2))
        pygame.display.flip()
        clock.tick(200)
        for event in pygame.event.get():  # 遍历所有事件
            if event.type==pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()





        
    while condition==None:  # None说明在进行中，
        
        for event in pygame.event.get():  # 遍历所有事件
            if event.type==pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
                
            if event.type==MOUSEBUTTONDOWN:
                if event.button == 1:#1是左键单击
                    #event.pos[0]点下时鼠标的横坐标，[1]是纵坐标
                    
                    if toparrowstartx<event.pos[0]<toparrowendx and toparrowstarty<event.pos[1]<toparrowendy:
                        #鼠标在上面横条的上下按键位置
                        count+=1
                        #print('点了%d' % count)
                        j=int((event.pos[0]-toparrowstartx)//uparrowwidth+2) # j是矩阵的列，pos[0]是鼠标的横坐标，到+2是因为左上角是空的
                        
                        if j%2==0:
                            #向上卷
                            print('向上卷',j/2,event.pos[0],toparrowendx)
                            j=j//2+2
                            a=matrix[0][j]
                            for i in range(0,8):
                                matrix[i][j]=matrix[i+1][j]

                            matrix[8][j]=a
                            #screen.blit(turtle,[toparrowstartx,toparrowstarty])

                            
                        else: #(event.pos[0]-toparrowx)//minicellwidth%2==1:
                            #向下卷
                            #j-=1#朝左回去一格，和向上卷是同一列
                            j=j//2+2
                            print('向下卷',j/2,event.pos[0],toparrowendx)
                            a=matrix[8][j]
                            for i in range(8,0,-1):
                                matrix[i][j]=matrix[i-1][j]

                            matrix[0][j]=a

                    elif leftarrowstartx<event.pos[0]<leftarrowendx and leftarrowstarty<event.pos[1]<leftarrowendy:
                        #鼠标在左边竖条的上下按键位置
                        count+=1
                        i=int((event.pos[1]-leftarrowstarty)//leftarrowheight+2) # j是矩阵的行，+2是因为左上角是空的
                        if i%2==0 :
                            #向左卷
                            print('向左卷',i/2,event.pos[1],leftarrowendy)
                            i=i//2+2
                            a=matrix[i].pop(0)
                            matrix[i].append(a)
                        else:#if (event.pos[1]-leftarrowstarty)//minicellwidth%2==1:
                            #向右卷
                            i-=1#朝上回去一格，和向左卷是同一列
                            i=i//2+2
                            print('向右卷',i/2,event.pos[1],leftarrowendy)
                                                    
                            a=matrix[i].pop()
                            matrix[i].insert(0, a)
                    #print(iswin(difficulty,count))
                    textCount = fontObj2.render('还有%d步' % (difficulty-count), False,(0, 0, 0))
                    
                        
            if event.type==KEYDOWN:
                if event.key==K_F11:  # 按下F11切换全屏窗口模式
                    fullscreen=not fullscreen

                    if fullscreen:
                        screen=pygame.display.set_mode((1024,768),FULLSCREEN | HWSURFACE)
                        
                    else:
                        screen=pygame.display.set_mode(size)
                
        


        screen.fill(bg)

        for i in range(9):
            for j in range(9):
                a=matrix[i][j]
                if a<9:
                    #a=9是四个角落空着的地方
                    if i<3 or i>5 or j<3 or j>5:
                        #是mini
                        if i < 3:
                            #是mini
                            x=startx+5.5*minicellwidth+(j-3)*4*minicellwidth
                            y=starty+i*minicellwidth
                            screen.blit(pics[a+5],[x,y])
                            
                        if i > 5:
                            #是mini
                            x=startx+5.5*minicellwidth+(j-3)*4*minicellwidth
                            y=starty+4*minicellwidth+3*cellwidth+(i-6)*minicellwidth+minicellwidth#多加一个是放方向键的
                            screen.blit(pics[a+5],[x,y])

                            
                        if j < 3:
                            #是mini
                            x=startx+j*minicellwidth
                            y=starty+5.5*minicellwidth+(i-3)*4*minicellwidth
                            screen.blit(pics[a+5],[x,y])

                        if j > 5:
                            #是mini
                            x=startx+4*minicellwidth+3*cellwidth+(j-6)*minicellwidth+minicellwidth#多加一个是放方向键的
                            y=starty+5.5*minicellwidth+(i-3)*4*minicellwidth
                            screen.blit(pics[a+5],[x,y])
                    else:
                        #是中间的大图
                        x=startx+4*minicellwidth+(j-3)*cellwidth
                        y=starty+4*minicellwidth+(i-3)*cellwidth
                        screen.blit(pics[a],[x,y])

        
        for i in range(3):
            for j in range(2):
                screen.blit(uparrow,[toparrowstartx+i*cellwidth,toparrowstarty+j*(minicellwidth+3*cellwidth)])
                
        for i in range(3):
            for j in range(2):
                screen.blit(downarrow,[toparrowstartx+2*minicellwidth+i*cellwidth,toparrowstarty+j*(minicellwidth+3*cellwidth)])

        for i in range(3):
            for j in range(2):
                screen.blit(leftarrow,[leftarrowstartx+j*(minicellwidth+3*cellwidth),leftarrowstarty+i*cellwidth])
                
        for i in range(3):
            for j in range(2):
                screen.blit(rightarrow,[leftarrowstartx+j*(minicellwidth+3*cellwidth),leftarrowstarty++2*minicellwidth+i*cellwidth])


                      

        
        #screen.blit(red,[toparrowstartx,toparrowstarty])
        #screen.blit(turtle,[15,15])放在这里可以长期显示，放在中间不显示
        condition=iswin(difficulty,count)
        screen.blit(textCount, (cellwidth, cellwidth))
        screen.blit(finish, (finishx, finishy))
        pygame.display.flip()
        clock.tick(200)

    



'''

        
    if condition==True:
        screen.blit(textWin, (width//2-int(cellwidth*1.5), height//2-cellwidth//2))
    elif condition==False :
        screen.blit(textLose, (width//2-int(cellwidth*1.5), height//2-cellwidth//2))
    else:
        pass





    #手动写入
    matrix[3][0]=1
    matrix[4][0]=0
    matrix[5][0]=3
    matrix[3][1]=1
    matrix[4][1]=1
    matrix[5][1]=3
    matrix[3][2]=1
    matrix[4][2]=4
    matrix[5][2]=0
    matrix[0][3]=3
    matrix[1][3]=0
    matrix[2][3]=0
    matrix[3][3]=4
    matrix[4][3]=1
    matrix[5][3]=0
    matrix[6][3]=2
    matrix[7][3]=1
    matrix[8][3]=1
    matrix[0][4]=2
    matrix[1][4]=3
    matrix[2][4]=1
    matrix[3][4]=2
    matrix[4][4]=1
    matrix[5][4]=3
    matrix[6][4]=2
    matrix[7][4]=3
    matrix[8][4]=2
    matrix[0][5]=4
    matrix[1][5]=4
    matrix[2][5]=3
    matrix[3][5]=2
    matrix[4][5]=2
    matrix[5][5]=4
    matrix[6][5]=0
    matrix[7][5]=0
    matrix[8][5]=0
    matrix[3][6]=4
    matrix[4][6]=4
    matrix[5][6]=3
    matrix[3][7]=0
    matrix[4][7]=4
    matrix[5][7]=2
    matrix[3][8]=2
    matrix[4][8]=4
    matrix[5][8]=3

'''
