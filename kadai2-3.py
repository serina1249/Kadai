import tkinter as tk

root = tk.Tk() #tkinterはウィンドウを作り、それを変数rootが指している
# root.やりたい操作()
root.geometry("700x600")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

class Car:

    def __init__(self, x, y,size,color,i,j):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.i = i
        self.j = j

    def original(self):
        #車の描画
        # 矩形(四角)の描画 id = Canvas.create_rectangle(x0, y0, x1, y1, option, ...)
        canvas.create_rectangle(25*self.size+self.x, 10*self.size+self.y, 50*self.size+self.x, 20*self.size+self.y, fill = self.color, outline = self.color, tag = "car"+str(self.i)+str(self.j)) #上
        canvas.create_rectangle(12.5*self.size+self.x, 20*self.size+self.y, 62.5*self.size+self.x, 32.5*self.size+self.y, fill = self.color, outline = self.color, tag = "car"+str(self.i)+str(self.j)) #(x0, y0, x1, y1, fill(塗りつぶし)) 左上の座標(x0, y0)と右下の座標(x1, y1)
        # 円の描画 id = C.create_oval(x0, y0, x1, y1, option, ...)
        canvas.create_oval(16.25*self.size+self.x, 32.5*self.size+self.y, 25*self.size+self.x, 41.25*self.size+self.y, fill = "Black", tag = "car"+str(self.i)+str(self.j)) #左上の座標(x0, y0)と右下の座標(x1, y1) 左
        canvas.create_oval(50*self.size+self.x, 32.5*self.size+self.y, 58.75*self.size+self.x, 41.25*self.size+self.y, fill = "Black", tag = "car"+str(self.i)+str(self.j)) #左上の座標(x0, y0)と右下の座標(x1, y1) 右

    def delete(self,i,j):
        canvas.delete("car"+str(i)+str(j))

for i in range(10):
    for j in range(10):
        if (i+j) % 2 == 0:
            color = "red"
        else:
            color = "blue"
        car1 = Car(i*55,j*55,1,color,i,j)
        car1.original()

#キーボードから0～99の数値を入力させ，10の位の値を行の番号，1の位の値を列の番号とする．
#入力が0～99以外の数値や文字列の場合は，エラーメッセージを表示して，再入力する
def keyboard():
    var = input()
    if var.isdigit(): #.isdigit()で数値かどうかを判定
        if int(var) >= 0 and int(var) < 10:
            line = 0#行
            column = var[-1]#列
            return line,column
        elif int(var) >= 10 and int(var) < 100:
            line = var[-2]#行
            column = var[-1]#列
            return line,column
        else:
            print("もう一度入力してください")
            return keyboard()
    else:
        print("もう一度入力してください")
        return keyboard()


line,column = keyboard()
intline = int(line)
intcolumn = int(column)
"""
for i in range(10):
    for j in range(10):
        if i == intline and j == intcolumn:
            canvas.create_rectangle(i*55 + 60-50,j*55+45-50,i*55 + 65,j*55+45, fill="White",outline = "white",width = 3, tag="rect")
"""
for i in range(10):
    for j in range(10):
        if i == intline and j == intcolumn:
            car1.delete(i,j)
root.mainloop() #描画
