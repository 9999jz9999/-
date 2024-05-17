# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import messagebox

# 創建主視窗
root = tk.Tk()
root.title("密碼")

# 創建並顯示題目標籤
question_label = tk.Label(root, text="請輸入密碼")
question_label.pack()

# 創建輸入框讓使用者輸入答案
answer_entry = tk.Entry(root)
answer_entry.pack()

# 定義檢查答案的函數
def check_answer():
    try:
        user_answer = int(answer_entry.get())
        correct_answer = 1234
        if user_answer == correct_answer:
            messagebox.showinfo("結果", "正確！")
        else:
            messagebox.showinfo("結果", "錯誤")
    except ValueError:
        messagebox.showerror("錯誤", "請輸數字")

# 創建按鈕讓使用者提交答案
submit_button = tk.Button(root, text="確定", command=check_answer)
submit_button.pack()

# 運行主循環
root.mainloop()

#______________________________________________________


import tkinter as tk
from tkinter import messagebox
import random

# 生成隨機數字
number1 = random.randint(1, 50)
number2 = random.randint(1, 50)



# 創建主視窗
root = tk.Tk()
root.title("簡易數學題目")

# 創建並顯示題目標籤
question_label = tk.Label(root, text= f"{number1} + {number2} = ?")
question_label.pack()

# 創建輸入框讓使用者輸入答案
answer_entry = tk.Entry(root)
answer_entry.pack()

# 定義檢查答案的函數
def check_answer():
    try:
        user_answer = int(answer_entry.get())
        correct_answer = number1 + number2
        if user_answer == correct_answer:
            messagebox.showinfo("結果", "正確！")
        else:
            messagebox.showinfo("結果", f"錯誤，正確答案是{correct_answer}")
    except ValueError:
        messagebox.showerror("錯誤", "請輸入數字！")

# 創建按鈕讓使用者提交答案
submit_button = tk.Button(root, text="提交答案", command=check_answer)
submit_button.pack()

# 運行主循環
root.mainloop()


#__________________________________________________

import tkinter as tk
from tkinter import messagebox
import random

# 生成隨機數字
number1 = random.randint(1, 50)
number2 = random.randint(1, 50)
#選取運算
operator = random.choice(["+", "-", "*", "/"])
#計算
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
# 創建主視窗
root = tk.Tk()
root.title("簡易數學題目")

# 創建並顯示題目標籤
question_label = tk.Label(root, text= f"{number1}{operator}{number2} = ?")
question_label.pack()

# 創建輸入框讓使用者輸入答案
answer_entry = tk.Entry(root)
answer_entry.pack()

# 定義檢查答案的函數
def check_answer():
    try:
        user_answer = int(answer_entry.get())
        correct_answer = result
        if user_answer == correct_answer:
            messagebox.showinfo("結果", "正確！")
        else:
            messagebox.showinfo("結果", f"錯誤，正確答案是{correct_answer}")
    except ValueError:
        messagebox.showerror("錯誤", "請輸入數字！")

# 創建按鈕讓使用者提交答案
submit_button = tk.Button(root, text="提交答案", command=check_answer)
submit_button.pack()

# 運行主循環
root.mainloop()