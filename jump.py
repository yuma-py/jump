import tkinter as tk
from tkinter.constants import FALSE
from PIL import Image,ImageTk

X = 1000
Y = 160
z = 1
index = 0
car_x = X/2
car_y = Y-16
x,y,tama = 0,0,1
jflag = False
fflag = False
key_keep = ''
def key_down(e):
    global index 
    global car_x,car_y
    global z
    global x,y,tama
    global jflag,fflag
    global key_keep
    index = (index + 1) % 3
    key = e.keysym
    canvas.delete("IMG")

    if key == "Up" and jflag == False:
        car_y -= 1
        jflag = True
        fflag = False
    if key == "Left" or key_keep =="Left":
        z = 0
        car_x -= 8
        key_keep = "Left"
    if key == "Right" or key_keep =="Right":
        z = 1
        car_x += 8
        key_keep = "Right"
    if key == "Return" and tama == 1:
        tama = 0
        x = car_x + 8
        y = car_y - 8
        canvas.create_rectangle(x,y-8,x+8,y,fill="red",tag="IMG")
    canvas.create_image(car_x,car_y,image=img[z][index],tag="IMG")

def key_release(e):
    global key_keep
    if e.keysym == key_keep:
        key_keep = " "
    
def main_proc():
    global car_y #関数内で値を変更できるようにglobalにする
    global x,y,tama
    global jflag,fflag
    global car_x,car_y
    if jflag == True and car_y != Y-16:
        if fflag == False and car_y != Y-32:
            car_y -= 1
        else:
            fflag =True
            car_y = car_y + 1
    else:
        jflag = False
    if key_keep =="Left":
        car_x -= 8
    elif key_keep =="Right":
        car_x += 8
        
    canvas.delete("IMG")
    if(tama == 0):
        x = x + 48
        if x >= 1000:
            tama = 1
        canvas.create_rectangle(x,y-8,x+8,y,fill="red",tag="IMG")
    canvas.create_image(car_x,car_y,image=img[z][index],tag="IMG")
    root.after(50,main_proc)
    
root = tk.Tk()
root.title("Jump")
root.resizable(False,False)#Window（横、縦）の大きさを変更できない
canvas = tk.Canvas(root,width=X,height=Y,bg='skyblue')
canvas.pack()#canvasの大きさに合わせてWindowのサイズを決める

im =  Image.open("画像は自分で用意して.png")
img = [[0]*3 for _ in range(2)]
for i in range(1,3):
    for j in range(3):
        im_crop = im.crop((j*32, i*32, (j+1)*32, (i+1)*32))
        img[i-1][j] = ImageTk.PhotoImage(image=im_crop)
canvas.create_image(car_x,car_y,image=img[1][0],tag="IMG")

root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_release)
root.after(100,main_proc)#500ミリ秒後にmain_procを実行する、それまでは別のことをする
root.mainloop()
