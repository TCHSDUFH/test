import tkinter as tk
from tkinter import colorchooser

def choose_color():
    # 打开颜色选择器
    color_code = colorchooser.askcolor(title="选择颜色")
    if color_code[1]:  # 如果选择了颜色
        color_display.config(bg=color_code[1])  # 更新显示框的背景颜色
        color_label.config(text=color_code[1])  # 显示选中的颜色代码
    print(color_code[0])
    colo = list(color_code[0])
    e = []
    for i in colo:
        a = i / 255.0
        e.append(a)
    print(e)

# 创建主窗口
root = tk.Tk()
root.title("颜色选择器")

# 创建按钮以选择颜色
choose_color_btn = tk.Button(root, text="选择颜色", command=choose_color)
choose_color_btn.pack(pady=20)

# 创建显示选中颜色的标签
color_display = tk.Frame(root, width=100, height=100)
color_display.pack(pady=20)

color_label = tk.Label(root, text="")
color_label.pack(pady=10)

# 运行主循环
root.mainloop()
