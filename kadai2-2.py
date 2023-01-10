import tkinter as tk

root = tk.Tk() #tkinterはウィンドウを作り、それを変数rootが指している
# root.やりたい操作()
root.geometry("700x600")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

class Car:

    def __init__(self, x, y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def original(self):
        #車の描画
        # 矩形(四角)の描画 id = Canvas.create_rectangle(x0, y0, x1, y1, option, ...)
        canvas.create_rectangle(25*self.size+self.x, 10*self.size+self.y, 50*self.size+self.x, 20*self.size+self.y, fill = self.color, outline = self.color, tag = "car") #上
        canvas.create_rectangle(12.5*self.size+self.x, 20*self.size+self.y, 62.5*self.size+self.x, 32.5*self.size+self.y, fill = self.color, outline = self.color, tag = "car") #(x0, y0, x1, y1, fill(塗りつぶし)) 左上の座標(x0, y0)と右下の座標(x1, y1)
        # 円の描画 id = C.create_oval(x0, y0, x1, y1, option, ...)
        canvas.create_oval(16.25*self.size+self.x, 32.5*self.size+self.y, 25*self.size+self.x, 41.25*self.size+self.y, fill = "Black", tag = "car") #左上の座標(x0, y0)と右下の座標(x1, y1) 左
        canvas.create_oval(50*self.size+self.x, 32.5*self.size+self.y, 58.75*self.size+self.x, 41.25*self.size+self.y, fill = "Black", tag = "car") #左上の座標(x0, y0)と右下の座標(x1, y1) 右


for i in range(10):
    for j in range(10):
        if (i+j) % 2 == 0:
            color = "red"
        else:
            color = "blue"
        car1 = Car(i*55,j*55,1,color)
        car1.original()

root.mainloop() #描画
