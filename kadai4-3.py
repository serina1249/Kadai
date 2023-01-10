import tkinter as tk
import time

root = tk.Tk() #tkinterはウィンドウを作り、それを変数rootが指している
# root.やりたい操作()
root.geometry("600x600")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)
RADIUS_BALL = 10  # ボールの半径
class Cannon:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        #車の描画
        # 矩形(四角)の描画 id = Canvas.create_rectangle(x0, y0, x1, y1, option, ...)
        canvas.create_rectangle(45+self.x, 1.5+self.y, 67.5+self.x, 30+self.y, fill = self.color, outline = self.color, tag = "cannon") #上
        canvas.create_rectangle(18.75+self.x, 30+self.y, 93.75+self.x, 48.75+self.y, fill = self.color, outline = self.color, tag = "cannon") #(x0, y0, x1, y1, fill(塗りつぶし)) 左上の座標(x0, y0)と右下の座標(x1, y1)


class Ball:

    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.r = radius

    def draw(self):
        #球の描画
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, outline = self.color, tag = "ball")

    def move(self, hori, vart):
        self.x += hori
        self.y += vart
        canvas.move("ball", hori, vart)

    def flag(self):
        return self.y < 10

    def delete(self):
        canvas.delete("ball")

class Car:

    def __init__(self, x, y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self):
        #車の描画
        # 矩形(四角)の描画 id = Canvas.create_rectangle(x0, y0, x1, y1, option, ...)
        canvas.create_rectangle(25*self.size+self.x, 10*self.size+self.y, 50*self.size+self.x, 20*self.size+self.y, fill = self.color, outline = self.color, tag = "car") #上
        canvas.create_rectangle(12.5*self.size+self.x, 20*self.size+self.y, 62.5*self.size+self.x, 32.5*self.size+self.y, fill = self.color, outline = self.color, tag = ("car","body")) #(x0, y0, x1, y1, fill(塗りつぶし)) 左上の座標(x0, y0)と右下の座標(x1, y1)
        # 円の描画 id = C.create_oval(x0, y0, x1, y1, option, ...)
        canvas.create_oval(16.25*self.size+self.x, 32.5*self.size+self.y, 25*self.size+self.x, 41.25*self.size+self.y, fill = "Black", tag = "car") #左上の座標(x0, y0)と右下の座標(x1, y1) 左
        canvas.create_oval(50*self.size+self.x, 32.5*self.size+self.y, 58.75*self.size+self.x, 41.25*self.size+self.y, fill = "Black", tag = "car") #左上の座標(x0, y0)と右下の座標(x1, y1) 右

    def move(self, hori, vart):
        self.x += hori
        self.y += vart
        canvas.move("car", hori, vart)

    def left_flag(self):
        return self.x <= 10
    def right_flag(self):
        return self.x > 500

def key_event(e):
   key = e.keysym
   if key == "a":
       balls.append(Ball(307,430,"Black",RADIUS_BALL))

root.bind("<KeyPress>", key_event)

cannon = Cannon(250,500,"green")
cannon.draw()
car = Car(10,10,1,"blue")
car.draw()
hori = 10
vart = 0
balls = []
while True:
    delete_balls = []
    canvas.delete("ball")
    if(car.right_flag()):#xが一番右になったら
        hori = -10
    if(car.left_flag()):#xが一番左になったら
        hori = 10
    car.move(hori,vart)
    for i in range(len(balls)):
        balls[i].draw()
        balls[i].move(0,-10)
        if(balls[i].flag()):#yが10未満になったら
            balls[i].delete()
            delete_balls.append(i)
        if((car.x > 250 and car.x < 290) and balls[i].y < 100):#車に球が当たったら
            canvas.delete("car")
            car.x=10
            car.draw()
    for i in range(len(delete_balls)):
        balls.pop(delete_balls[i])
    
    time.sleep(0.05)
    root.update()

root.mainloop() #描画
