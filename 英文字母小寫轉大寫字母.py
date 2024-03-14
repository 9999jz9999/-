# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:34:51 2024

@author: kkjj1
"""

# 建立字典
letter_dict = {chr(i): chr(i).upper() for i in range(97, 123)}

# 使用者輸入
user_input = input("請輸入小寫英文字母: ")

# 轉換並顯示結果
if user_input in letter_dict:
    print("大寫字母:", letter_dict[user_input])
else:
    print("無效的輸入")
