import tkinter as tk

root = tk.Tk() #tkinterはウィンドウを作り、それを変数rootが指している
# root.やりたい操作()
root.geometry("600x400")

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

# 矩形(四角)の描画 id = Canvas.create_rectangle(x0, y0, x1, y1, option, ...)
canvas.create_rectangle(50, 80, 350, 230, fill = "Black") #(x0, y0, x1, y1, fill(塗りつぶし)) 左上の座標(x0, y0)と右下の座標(x1, y1)

root.mainloop() #描画
