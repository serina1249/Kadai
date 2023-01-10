import tkinter as tk
import math
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

    def __init__(self, x, y, color,radius):
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
    
    def delete(self):
        canvas.delete("ball")
        
cannon = Cannon(250,500,"green")
cannon.draw()
ball = Ball(307,430,"Black",RADIUS_BALL)
ball.draw()


while True:
    if ball.y > 100:
        vart = -10
        ball.move(0,vart)
    if ball.y <= 100:
        ball.delete()
        ball.x,ball.y = 307,430
        ball.draw()
    time.sleep(0.05)
    root.update()
   
root.mainloop() #描画