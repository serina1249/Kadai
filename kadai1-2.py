import tkinter as tk

root = tk.Tk() #tkinterはウィンドウを作り、それを変数rootが指している
# root.やりたい操作()
root.geometry("600x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

# 矩形(四角)の描画 id = Canvas.create_rectangle(x0, y0, x1, y1, option, ...)
canvas.create_rectangle(100, 40, 200, 80, fill = "Black") #上
canvas.create_rectangle(50, 80, 250, 130, fill = "Black") #(x0, y0, x1, y1, fill(塗りつぶし)) 左上の座標(x0, y0)と右下の座標(x1, y1)

# 円の描画 id = C.create_oval(x0, y0, x1, y1, option, ...)
canvas.create_oval(65, 130, 100, 165, fill = "Black") #左上の座標(x0, y0)と右下の座標(x1, y1) 左
canvas.create_oval(200, 130, 235, 165, fill = "Black") #左上の座標(x0, y0)と右下の座標(x1, y1) 右

#　文字の描画 id = Canvas.create_text(x, y, option, ...)
canvas.create_text(150, 200, text = "Sumire Sakai", font=("HG丸ｺﾞｼｯｸM-PRO",24))

root.mainloop() #描画
