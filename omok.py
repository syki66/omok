import turtle
import os
import time
import math

#배경
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("omok 1.0.3")
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
checkArray = [[0]*22 for i in range(22)]

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
def isBlackWin(a,b):
    for i in range(5):
        #흑승리
        if checkArray [a+i][b] == 1 and checkArray [a-1+i][b] == 1 and checkArray [a-2+i][b] == 1 and checkArray[a-3+i][b] == 1 and checkArray[a-4+i][b] == 1:
            return True
        if checkArray [a][b+i] == 1 and checkArray [a][b-1+i] == 1 and checkArray [a][b-2+i] == 1 and checkArray[a][b-3+i] == 1 and checkArray[a][b-4+i] == 1 :
            return True
        if checkArray [a+i][b+i] == 1 and checkArray [a-1+i][b-1+i] == 1 and checkArray [a-2+i][b-2+i] == 1 and checkArray[a-3+i][b-3+i] == 1 and checkArray[a-4+i][b-4+i] == 1:
            return True
        if checkArray [a+i][b-i] == 1 and checkArray [a-1+i][b+1-i] == 1 and checkArray [a-2+i][b+2-i] == 1 and checkArray[a-3+i][b+3-i] == 1 and checkArray[a-4+i][b+4-i] == 1:
            return True
        #백승리
        if checkArray [a+i][b] == 2 and checkArray [a-1+i][b] == 2 and checkArray [a-2+i][b] == 2 and checkArray[a-3+i][b] == 2 and checkArray[a-4+i][b] == 2:
            return False
        if checkArray [a][b+i] == 2 and checkArray [a][b-1+i] == 2 and checkArray [a][b-2+i] == 2 and checkArray[a][b-3+i] == 2 and checkArray[a][b-4+i] == 2 :
            return False
        if checkArray [a+i][b+i] == 2 and checkArray [a-1+i][b-1+i] == 2 and checkArray [a-2+i][b-2+i] == 2 and checkArray[a-3+i][b-3+i] == 2 and checkArray[a-4+i][b-4+i] == 2:
            return False
        if checkArray [a+i][b-i] == 2 and checkArray [a-1+i][b+1-i] == 2 and checkArray [a-2+i][b+2-i] == 2 and checkArray[a-3+i][b+3-i] == 2 and checkArray[a-4+i][b+4-i] == 2:
            return False

#키보드입력
def spaceClicked():
    for i in range(22):
        for j in range(22):
            checkArray[i][j] = 0
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

    m.onclick(run_omok)



#2인용 오목
count = 0
def run_omok(xClick,yClick):
    global count
    
    for i in range(17):
        for j in range(17):
            distance = math.sqrt(math.pow(xClick-(-400+(i*50)),2)+math.pow(yClick-(-400+(j*50)),2))
            if distance < 25 and checkArray[i][j] == 0:
                a1=turtle.Turtle()
                a1.penup()
                a1.speed(0)
                a1.setposition(-400+(i*50),-400+(j*50))
                a1.shape("circle")
                a1.shapesize(2.5, 2.5)
                
                if count % 2 == 1:
                    a1.color("white")
                    checkArray[i][j] = 2
                else:
                    a1.color("black")
                    checkArray[i][j] = 1
                                
                #print(checkArray)
                if isBlackWin(i,j) == True:
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
                    count = -1
                    for i in range(22):
                        for j in range(22):
                            checkArray[i][j] = 1
                    turtle.listen()
                    turtle.onkey(spaceClicked, "space")
                                               
                elif isBlackWin(i,j) == False:
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
                    count = -1
                    for i in range(22):
                        for j in range(22):
                            checkArray[i][j] = 1
                    turtle.listen()
                    turtle.onkey(spaceClicked, "space")
                
                count += 1
                print(count)
            
                
            else :
                pass

m = turtle.Screen()
m.onclick(run_omok)

#콘솔창 자동으로 안꺼지게
turtle.mainloop()
