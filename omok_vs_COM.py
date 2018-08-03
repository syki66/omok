import turtle
import os
import time
import math
import random

#배경
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("오목 made by syki66")
wn.setup(1000,1000)

#장기판 셋업
border = turtle.Turtle()
border.speed(0)
border.color("black")
border.penup()
border.setposition(-400,-400)
border.hideturtle()
border.pensize(4)
border.lt(90)

#배열, 판정때문에 크게만듬
ffff = [[0]*22 for i in range(22)]

#세로줄
for i in range(17):
    border.penup()
    border.setposition(-400+(i*50),-400)
    border.pendown()
    border.fd(800)
    
#가로줄
border.rt(90)
for j in range(17):
    border.penup()
    border.setposition(-400,-400+(j*50))
    border.pendown()
    border.fd(800)

#판정
def logic(a,b):
    for p in range(5):
        #흑승리
        if ffff [a+p][b] == 1 and ffff [a-1+p][b] == 1 and ffff [a-2+p][b] == 1 and ffff[a-3+p][b] == 1 and ffff[a-4+p][b] == 1:
            return True
        if ffff [a][b+p] == 1 and ffff [a][b-1+p] == 1 and ffff [a][b-2+p] == 1 and ffff[a][b-3+p] == 1 and ffff[a][b-4+p] == 1 :
            return True
        if ffff [a+p][b+p] == 1 and ffff [a-1+p][b-1+p] == 1 and ffff [a-2+p][b-2+p] == 1 and ffff[a-3+p][b-3+p] == 1 and ffff[a-4+p][b-4+p] == 1:
            return True
        if ffff [a+p][b-p] == 1 and ffff [a-1+p][b+1-p] == 1 and ffff [a-2+p][b+2-p] == 1 and ffff[a-3+p][b+3-p] == 1 and ffff[a-4+p][b+4-p] == 1:
            return True


#키보드입력
def ClickSpace():
    for i in range(22):
        for j in range(22):
            ffff[i][j] = 0
    turtle.clearscreen()

    wn.bgcolor("yellow")
    border = turtle.Turtle()
    border.speed(0)
    border.color("black")
    border.penup()
    border.setposition(-400,-400)
    border.hideturtle()
    border.pensize(4)
    border.lt(90)

    for i in range(17):
        border.penup()
        border.setposition(-400+(i*50),-400)
        border.pendown()
        border.fd(800)
    
    border.rt(90)
    for j in range(17):
        border.penup()
        border.setposition(-400,-400+(j*50))
        border.pendown()
        border.fd(800)

    turtle.color("blue")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(150,-450)
    turtle.write("made by syki66", False, font=("Arial", 30, "bold"))

    m.onclick(aaa)

#누가만들었나
turtle.color("blue")
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.setposition(-20,-460)
turtle.write("오목 v1.0 made by syki66", False, font=("Arial", 30, "bold"))

def white_win():
    print("백 승")
    turtle.color("white")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(-350,170)
    turtle.write("백      승", False, font=("Arial", 145, "bold"))
    turtle.setposition(-440,0)
    turtle.color("red")
    turtle.write("재경기: 스페이스바", False, font=("Arial", 80, "bold"))
                
    for i in range(22):
        for j in range(22):
            ffff[i][j] = 3
    turtle.listen()
    turtle.onkey(ClickSpace, "space")

#기보
def setpos(x,y):
    if ffff[x][y] == 0:
        t3=turtle.Turtle()
        t3.penup()
        t3.speed(0)
        t3.setposition(50*x-400,y*50-400)
        t3.color("white")
        t3.shape("circle")
        t3.shapesize(2.5, 2.5)
        ffff[x][y] = 2
            #백승리
        for p in range(5):
            if ffff [x+p][y] == 2 and ffff [x-1+p][y] == 2 and ffff [x-2+p][y] == 2 and ffff[x-3+p][y] == 2 and ffff[x-4+p][y] == 2:
                white_win()
            if ffff [x][y+p] == 2 and ffff [x][y-1+p] == 2 and ffff [x][y-2+p] == 2 and ffff[x][y-3+p] == 2 and ffff[x][y-4+p] == 2 :
                white_win()
            if ffff [x+p][y+p] == 2 and ffff [x-1+p][y-1+p] == 2 and ffff [x-2+p][y-2+p] == 2 and ffff[x-3+p][y-3+p] == 2 and ffff[x-4+p][y-4+p] == 2:
                white_win()
            if ffff [x+p][y-p] == 2 and ffff [x-1+p][y+1-p] == 2 and ffff [x-2+p][y+2-p] == 2 and ffff[x-3+p][y+3-p] == 2 and ffff[x-4+p][y+4-p] == 2:
                white_win()
        
    #ffff
#3개막기
def ai3(a,b):
    for p in range(3):
        r= random.choice([-2,2])
        if ffff [a+p][b] == 1 and ffff [a-1+p][b] == 1 and ffff [a-2+p][b] == 1:            
            setpos(a+p-1+r,b)
            return True
        elif ffff [a][b+p] == 1 and ffff [a][b-1+p] == 1 and ffff [a][b-2+p] == 1:
            setpos(a,b+p-1+r)
            return True
        elif ffff [a+p][b+p] == 1 and ffff [a-1+p][b-1+p] == 1 and ffff [a-2+p][b-2+p] == 1:
            setpos(a+p-1+r,b+p-1+r)
            return True
        elif ffff [a+p][b-p] == 1 and ffff [a-1+p][b+1-p] == 1 and ffff [a-2+p][b+2-p] == 1:
            setpos(a+p-1+r,b-p+1-r)
            return True
#4개막기
def ai4(a,b):
    for p in range(4):
        r= random.choice([-2.5,2.5])
        if ffff [a+p][b] == 1 and ffff [a-1+p][b] == 1 and ffff [a-2+p][b] == 1 and ffff[a-3+p][b]==1:
            if ffff[int(a+p-1.5+r)][b] == 2:
                setpos(int(a+p-1.5-r),b)
            else:
                setpos(int(a+p-1.5+r),b)
            return True
        elif ffff [a][b+p] == 1 and ffff [a][b-1+p] == 1 and ffff [a][b-2+p] == 1 and ffff[a][b-3+p]:
            if ffff[a][int(b+p-1.5+r)] == 2:
                setpos(a,int(b+p-1.5-r))    
            else:
                setpos(a,int(b+p-1.5+r))
            return True
        elif ffff [a+p][b+p] == 1 and ffff [a-1+p][b-1+p] == 1 and ffff [a-2+p][b-2+p] == 1 and ffff[a-3+p][b-3+p]:
            if ffff[int(a+p-1.5+r)][int(b+p-1.5+r)] == 2:
                setpos(int(a+p-1.5-r),int(b+p-1.5-r))    
            else:
                setpos(int(a+p-1.5+r),int(b+p-1.5+r))
            return True
        elif ffff [a+p][b-p] == 1 and ffff [a-1+p][b+1-p] == 1 and ffff [a-2+p][b+2-p] == 1 and ffff[a-3+p][b+3-p]:
            if ffff[int(a+p-1.5+r)][int(b-p+1.5-r)] == 2:
                setpos(int(a+p-1.5-r),int(b-p+1.5+r))   
            else:
                setpos(int(a+p-1.5+r),int(b-p+1.5-r))
            return True
#2개막기
def ai2(a,b):
    for p in range(2):
        if ffff [a+p][b] == 1 and ffff [a-1+p][b] == 1 :
            if ffff[int(a+p-1.5+r)][b] == 2:
                setpos(int(a+p-1.5-r),b)
            else:
                setpos(int(a+p-1.5+r),b)
            return True
        elif ffff [a][b+p] == 1 and ffff [a][b-1+p] == 1:
            if ffff[a][int(b+p-1.5+r)] == 2:
                setpos(a,int(b+p-1.5-r))    
            else:
                setpos(a,int(b+p-1.5+r))
            return True
        elif ffff [a+p][b+p] == 1 and ffff [a-1+p][b-1+p] == 1:
            if ffff[int(a+p-1.5+r)][int(b+p-1.5+r)] == 2:
                setpos(int(a+p-1.5-r),int(b+p-1.5-r))    
            else:
                setpos(int(a+p-1.5+r),int(b+p-1.5+r))
            return True
        elif ffff [a+p][b-p] == 1 and ffff [a-1+p][b+1-p] == 1:
            if ffff[int(a+p-1.5+r)][int(b-p+1.5-r)] == 2:
                setpos(int(a+p-1.5-r),int(b-p+1.5+r))   
            else:
                setpos(int(a+p-1.5+r),int(b-p+1.5-r))
            return True
    

# vs COM 오목
def aaa(xclick,yclick):
    for i in range(17):
        for j in range(17):
            distance = math.sqrt(math.pow(xclick-(-400+(i*50)),2)+math.pow(yclick-(-400+(j*50)),2))
            if distance < 25 and ffff[i][j] == 0:
                a1=turtle.Turtle()
                a1.penup()
                a1.speed(0)
                a1.setposition(-400+(i*50),-400+(j*50))
                a1.shape("circle")
                a1.shapesize(2.5, 2.5)
                
                a1.color("black")
                ffff[i][j] = 1

                if ai4(i,j) == True:
                    pass
                elif ai3(i,j) == True:
                    pass
                
                #print(ffff)
                
                if logic(i,j) == True:
                    print("흑 승")
                    turtle.color("black")
                    turtle.hideturtle()
                    turtle.speed(0)
                    turtle.penup()
                    turtle.setposition(-350,-400)
                    turtle.write("흑      승", False, font=("Arial", 145, "bold"))
                    turtle.setposition(-440,0)
                    turtle.color("red")
                    turtle.write("재경기: 스페이스바", False, font=("Arial", 80, "bold"))
                    
                    for i in range(22):
                        for j in range(22):
                            ffff[i][j] = 1
                    turtle.listen()
                    turtle.onkey(ClickSpace, "space")      
            else :
                pass

m = turtle.Screen()
m.onclick(aaa)

#콘솔창 자동으로 안꺼지게
turtle.mainloop()
