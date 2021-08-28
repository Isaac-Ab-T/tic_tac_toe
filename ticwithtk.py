import tkinter as tk
from tkinter.constants import *

Grid=[]
def check(Grid):
    global blank
    #columnwise
    for i in range(len(Grid)):
        if Grid[i].count(Grid[i][0])==len(Grid[i]) and Grid[i][0]!=blank:
            return("Stopped at Row ",i+1)
    #rowwise
    for i in range(len(Grid)):
        void=[]
        for j in range(len(Grid[i])):
            void.append(Grid[j][i])
        if void.count(void[0])==len(void) and void[0]!=blank:
            return("Stopped at Column ",i+1)
    #sideways left-right
    void=[]
    for i in range(len(Grid)):
        void.append(Grid[i][i])
    if void.count(void[0])==len(void) and void[0]!=blank:
        return("Stopped at Sideways Left to Right")
    #sideways right-left
    void=[]
    for i in range(len(Grid)):
        for j in range(len(Grid[i])):
            if i+j==len(Grid)-1:
                void.append(Grid[i][j])
    if void.count(void[0])==len(void) and void[0]!=blank:
        return("Stopped at Sideways Right to Left")
    #tie
    void=[]
    for i in range(len(Grid)):
        for j in range(len(Grid[i])):
            void.append(Grid[i][j])
    if void.count(blank)==0:
        return("Tie")
    
    return False


window=tk.Tk()

below=tk.Label(text='TIC TAC TOE',fg='red',bg='#F5FFFA',relief=tk.SUNKEN,master=window,height=2)
below_that=tk.Label(text='Player 1',fg='blue',bg='#F5FFFA',relief=tk.SUNKEN,master=window,height=2)
r1c1=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r1c2=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r1c3=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r2c1=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r2c2=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r2c3=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r3c1=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r3c2=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
r3c3=tk.Button(text='_',fg='black',bg='#F5FFFA',font=("Arial",25),master=window,height=2)
reset=tk.Button(text='RESET',fg='black',bg='#F5FFFA',master=window,height=2)
alpha_Grid=[[r1c1,r1c2,r1c3]
          ,[r2c1,r2c2,r2c3]
          ,[r3c1,r3c2,r3c3]
          ]
def assert2():
    global Grid
    #rechecks stored text 
    Grid=[[r1c1["text"],r1c2["text"],r1c3["text"]]
              ,[r2c1["text"],r2c2["text"],r2c3["text"]]
              ,[r3c1["text"],r3c2["text"],r3c3["text"]]
              ]
assert2()
def assert1():
    #converts text on window to that stored
    global Grid,alpha_Grid
    for i in range(len(alpha_Grid)):
        for j in range(len(alpha_Grid[i])):
            alpha_Grid[i][j]["text"]=Grid[i][j]
        
class Player():
    def __init__(self,number,symbol,color):
        self.symbol=symbol
        self.number=number
        self.color=color
        self.coords=[]
        print("Player ",self.number," has Symbol ",symbol)
    def add(self,cord):
        self.coords.append(cord)


blank="_"
game=True
p1=Player(1,"X","#FF0000")    
p2=Player(2,"O","#0000FF")
curr_p=p1
def handler(event):
    global Grid,alpha_Grid,curr_p
    row=int(event[1])
    col=int(event[3])
    #print(row,col)
    assert2()
    if alpha_Grid[row-1][col-1]["state"]=="disabled":
        return False
    if Grid[row-1][col-1]==blank:
        alpha_Grid[row-1][col-1]["bg"]=curr_p.color
        (alpha_Grid[row-1][col-1]).configure(fg="#FFFFFF")
        Grid[row-1][col-1]=curr_p.symbol
        print(Grid[row-1][col-1])
        alpha_Grid[row-1][col-1]["state"]="disabled"
        assert1()
    else:
        #print("Wrong Entry")
        return False
    if check(Grid)=='Tie':
        below_that["text"]="It is a Tie!"
        for i in alpha_Grid:
            for j in i:
                j["state"]="disabled"
        return True
    if check(Grid)!=False:
        #print(check(Grid))
        below_that["text"]="Player"+str(curr_p.number)+"has won !"
        for i in alpha_Grid:
            for j in i:
                j["state"]="disabled"
        return True
    if p1==curr_p:
        curr_p=p2
    elif p2==curr_p:
        curr_p=p1
    below_that["text"]="Player "+str(curr_p.number)
        
def reset1():
    global blank,alpha_Grid,Grid,below_that,curr_p
    curr_p=p1
    for i in range(len(alpha_Grid)):
        for j in range(len(alpha_Grid[i])):
            alpha_Grid[i][j]["text"]=blank
            alpha_Grid[i][j]["state"]="normal"
            alpha_Grid[i][j].configure(fg="black",bg="#F5FFFA")
    assert2()
    below_that["text"]="Player 1"
r1c1.grid(row=0,column=0)
r1c2.grid(row=0,column=1)
r1c3.grid(row=0,column=2)

r2c1.grid(row=1,column=0)
r2c2.grid(row=1,column=1)
r2c3.grid(row=1,column=2)

r3c1.grid(row=2,column=0)
r3c2.grid(row=2,column=1)
r3c3.grid(row=2,column=2)

below.grid(row=3,column=1)
below_that.grid(row=4,column=1)
reset.grid(row=5,column=1)
r1c1.bind('<Button-1>',lambda e:handler("r1c1"))
r1c2.bind('<Button-1>',lambda e:handler("r1c2"))
r1c3.bind('<Button-1>',lambda e:handler("r1c3"))
r2c1.bind('<Button-1>',lambda e:handler("r2c1"))
r2c2.bind('<Button-1>',lambda e:handler("r2c2"))
r2c3.bind('<Button-1>',lambda e:handler("r2c3"))
r3c1.bind('<Button-1>',lambda e:handler("r3c1"))
r3c2.bind('<Button-1>',lambda e:handler("r3c2"))
r3c3.bind('<Button-1>',lambda e:handler("r3c3"))
reset.bind('<Button-1>',lambda e:reset1())


window.mainloop()
