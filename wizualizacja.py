from tkinter import *
import math
import sys
root = Tk()
root.title("Wizualizacja ruhu")
width = 1000
height = 500
radius = 42
mp = 0.002#meters per pixel = 0.002, centimeter per pixel = 0.2
group = LabelFrame(root, text="ruh", padx=5, pady=5)
tlabel = Label(group)
x1label = Label(group)
y1label = Label(group)
v1label = Label(group)
x2label = Label(group)
y2label = Label(group)
v2label = Label(group)
vsumlabel = Label(group)
c = Canvas(root, width=width, height=height)
axis = BooleanVar()
axis.set(True)
axcheck = Checkbutton(variable = axis, text="Zablokuj oś X")
fram = DoubleVar()
def updatePoints(x):
    #point = points[int(fram.get())]
    point= points[int(x)]
    if int(x) > 0:
        ppoint = points[int(x)-1]
    else:
        ppoint = point
        ppoint[0] = 0.0001 
    print(point)
    t = float(point[0])
    tlabel.config(text = "Czas"+str(t))
    x1 = float(point[1])
    
    if axis.get():
        y1 = float(point[2])
        v1 = math.sqrt(math.pow(x1-float(ppoint[1]),2)+math.pow(y1-float(ppoint[2]),2))*mp/t-float(ppoint[0])
    else:
        y1 = 250.0
        v1 = (x1-float(ppoint[1]))*mp/(t-float(ppoint[0]))
    x1label.config(text = "Krążek 1 x="+str(x1))
    y1label.config(text = "Krążek 1 y="+str(y1))
    v1label.config(text = "Krążek 1 V="+str(v1))
    
    c.coords("circ1",0,0,radius,radius)
    c.move("circ1", x1, y1)
    c.itemconfig("circ1", fill="yellow")

    if len(point) > 4:
        x2 = float(point[4])
        
        if axis.get():
            y2 = float(point[5])
            v2 = math.sqrt(math.pow(x2-float(ppoint[4]),2)+math.pow(y2-float(ppoint[5]),2))*mp/t-float(ppoint[3])
        else:
            y2 = 250.0
            v2 = (x2-float(ppoint[4]))*mp/(t-float(ppoint[0]))
            
        x2label.config(text = "Krążek 2 x="+str(x2))
        y2label.config(text = "Krążek 2 y="+str(y2))
        
        v2label.config(text = "Krążek 2 V="+str(v2))
        vsumlabel.config(text="Suma prędkości: "+str(v1+v2))
        c.coords("circ2",0,0,radius,radius)
        c.move("circ2", x2, y2)
        c.itemconfig("circ2", fill="red")

if sys.argv[1][0] == "/":
    filepath = sys.argv[1] 
else:
    filepath = "./"+sys.argv[1]
points = []
with open(filepath) as f:
    line = f.readline()
    while line:
        
        point = f.readline().split()
        points.append(point)
        line = f.readline()
#for i in range(len(points)):
#    if points[i] == []:
#        points[i] = ['0', '0', '0', '0', '0','0']
points.remove([])
print(points)

scale = Scale( root, variable = fram, length=width, orient=HORIZONTAL, to=len(points)-1,command=updatePoints)


group.pack(padx=10, pady=10)
tlabel.grid(row=0, column=0,columnspan=3)
x1label.grid(row=1, column=0)
y1label.grid(row=1,column=1)
x2label.grid(row=2, column=0)
y2label.grid(row=2,column=1)
v1label.grid(row=1, column=2)
v2label.grid(row=2, column=2)
vsumlabel.grid(row = 3, column = 0, columnspan = 3)
c.pack()
scale.pack(anchor=CENTER)
axcheck.pack(anchor=CENTER)
circ1 = c.create_oval(0,0,radius,radius, tags = "circ1",fill="yellow")
if len(points[0])>3:
    
    circ2 = c.create_oval(20,20,radius-20,radius-20, tags="circ2", fill="blue")
    

updatePoints(0)
root.mainloop()
