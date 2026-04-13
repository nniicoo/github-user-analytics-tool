import tkinter as tk
from tkinter import messagebox

from api import fetch_user
from utils import process_user, analyze_users, plot_users

users_data = []

# 获取数据
def fetch_data():
    global users_data
    users_data = []

    names = entry.get().split(",")

    if not names:
        messagebox.showwarning("提示", "请输入用户名")
        return

    text.delete(1.0, tk.END)

    for name in names:
        name = name.strip()
        data = fetch_user(name)

        if data:
            user = process_user(data)
            users_data.append(user)

            text.insert(tk.END, f"{user['name']} - 粉丝: {user['followers']}\n")
        else:
            text.insert(tk.END, f"{name} 获取失败\n")

# 分析数据（排行榜）
def show_analysis():
    if not users_data:
        messagebox.showwarning("提示", "没有数据")
        return

    # 排序
    users_data.sort(key=lambda x: x["followers"], reverse=True)

    text.delete(1.0, tk.END)
    text.insert(tk.END, "===== 排行榜 =====\n")

    for i, u in enumerate(users_data):
        text.insert(tk.END, f"{i+1}. {u['name']} - {u['followers']}\n")

# 画图
def show_plot():
    if not users_data:
        messagebox.showwarning("提示", "没有数据")
        return

    plot_users(users_data)


# ======================
# GUI界面
# ======================
root = tk.Tk()
root.title("GitHub 用户分析工具")
root.geometry("500x400")

# 输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.insert(0, "octocat,torvalds")

# 按钮
btn1 = tk.Button(root, text="获取数据", command=fetch_data)
btn1.pack()

btn2 = tk.Button(root, text="生成排行榜", command=show_analysis)
btn2.pack()

btn3 = tk.Button(root, text="显示图表", command=show_plot)
btn3.pack()

# 文本框
text = tk.Text(root, height=15)
text.pack(pady=10)

# 启动
root.mainloop()