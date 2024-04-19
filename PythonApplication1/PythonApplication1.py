from tkinter import *
from tkinter import font
from random import choice
from random import *
from time import *
image_screen = False
image_components = list()
raam = Tk()
raam.geometry("1920x1080")
raam.title("Tahvel")
tahvel = Canvas(raam, width=1920, height=880, background="gray")
tahvel.pack()

def eestiLipp():
    tahvel.create_line(0, 130, 600, 130, width=100, fill="blue")
    tahvel.create_line(0, 230, 600, 230, width=100, fill="black")
    tahvel.create_line(0, 330, 600, 330, width=100, fill="white")
   

def undefLipp():
    tahvel.create_line(0, 530, 600, 530, width=100, fill="blue")
    tahvel.create_line(0, 630, 600, 630, width=100, fill="yellow")
    tahvel.create_line(0, 730, 600, 730, width=100, fill="blue")

    tahvel.create_polygon(0, 478, 0, 780, 250,630,fill = "black")
def unefSquare():
    koeff = 0
    for i in range(1,8):
        koeff += 20 / (i * 0.28)
        tahvel.create_polygon((800 + koeff , 0+  koeff), (1200 -   koeff, 0 +   koeff), (1200 -   koeff, 400 -   koeff), (800 +   koeff, 400 -   koeff),fill = "red")
        tahvel.create_oval(800 +  koeff,0 +  koeff,  1200 - koeff,400 - koeff,   fill="yellow")

def shaxmat():
    koeff1 = 1
    color_perm = True
    for i in range(0,8):
        for j in range(0,8):
            tahvel.create_polygon(800 + j * 100, 100 + koeff1, 900 +  j * 100, 100 + koeff1, 900 + j * 100,0 + koeff1, 800+  j * 100, 0 + koeff1,fill = "white" if color_perm else 'black')
            color_perm = False if color_perm else True
        koeff1 += 100
        color_perm = False if color_perm else True

def choice1():
    global image_screen
    if image_screen:
        tahvel.delete('all')

    image_screen = True
    for key, value in radiobuttons_num_func.items():
        if key == var.get():
            value()


def random_krugi():
    colors = ["red","blue","purple","gray","black","white","yellow","green"]
    for i in range(0,150):
       
        tahvel.create_oval(0 + 2 * i, 0 + 2 * i, 600 - 2 * i, 600 - 2 * i, fill=choice(colors))

def dota_lipp():

    lst = rand_sharp(1260, 1280, 300)
    lst2 = rand_sharp(955, 980, 0, True, 300)
    lst3 = rand_sharp(1280,980, 300, False, 280, True)
    print(lst3)

    #tahvel.create_polygon(980, 0, 1280, 0, 1280, 300, 980, 300, fill = "#B12F15")
    tahvel.create_polygon(980, 0,        990,5 , 1000,0, 1040, 6, 1045, 0, 1065, 8, 1070, 0   , 1120, 4, 1125, 0, 1170, 7, 1180, 0, 1220, 5, 1230, 0, 1250, 0, 1255, 5, 1260, 0   , 1280, 0, [i for i in lst], 1280, 300, [i for i in lst3] , 980, 300,[i for i in lst2] ,fill = "#B12F15")
    tahvel.create_polygon(1000, 30, 1020, 25, 1260, 200, 1250, 260,1200, 260, fill = "black")
    tahvel.create_polygon(1200, 30, 1230,45, 1225, 80, 1160, 45, fill = "black")
    tahvel.create_polygon(1015, 190, 1000, 250, 1050, 270,1080, 245,  fill = "black")

    
    
def rand_sharp(min_x, max_x, max_y, perm = False, min_y = None, perm2 = False):
    
    return_list = list()
    x = 0 
    move_y = 0
    y = 0
    if perm2:
        print(123)
        distantion = min_x
        while distantion > max_x:
            distantion -= randint(35,40) if distantion == 0 else 0
            y = randint(min_y, max_y)
            move_x = randint(35,40)
            if distantion - move_x < max_x:
                print(123)
                break
            x = randint(distantion - move_x, distantion)
            
            distantion -= move_x
            return_list.append(x)
            return_list.append(y)
            print(distantion)
            return_list.append(distantion)
            return_list.append(max_y)
    if perm:
        distantion = min_y
        while distantion > max_y:
            distantion -= randint(35,40) if distantion == 0 else 0
            x = randint(min_x, max_x)
            move_y = randint(35,40)
            if distantion - move_y < max_y:
       
                break
            y = randint(distantion - move_y, distantion)
            
            distantion -= move_y
            return_list.append(x)
            return_list.append(y)
            return_list.append(max_x)
            return_list.append(distantion)
    elif not perm and not perm2:
        distantion = 1
        while distantion < max_y:
            distantion += randint(35,40) if distantion == 0 else 0
            x = randint(min_x, max_x)
            move_y = randint(35,40)

            y = randint(distantion, distantion + move_y)
            if distantion + move_y > max_y:
                break
            distantion += move_y
            return_list.append(x)
            return_list.append(y)
            return_list.append(max_x)
            return_list.append(distantion)
    
        
    return return_list

s_frame = Frame(raam, width=200, height = 200)
show_another = False
var = IntVar()
radiobuttons = list()
radiobuttons_config = ['1','2','3','4', '5', '6']
radiobuttons_num_func = {1:eestiLipp, 2:undefLipp, 3:unefSquare, 4:shaxmat, 5:random_krugi, 6:dota_lipp}
for index,i in enumerate(radiobuttons_config):
    rad = radiobuttons.append(Radiobutton(s_frame, text=i, variable=var, value = index + 1, command = choice1))

s_frame.pack()
for rad in radiobuttons:
    rad.pack()

raam.mainloop()
