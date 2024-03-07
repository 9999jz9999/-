# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:47:49 2024

@author: kkjj1
"""

# 讓使用者輸入一個整數
user_input = input("請輸入一個整數: ")

# 將使用者輸入轉換為整數
try:
    number = int(user_input)
    
    # 判斷是否為偶數
    if number % 2 == 0:
        print(f"{number} 是偶數。")
    else:
        print(f"{number} 不是偶數。")
except ValueError:
    print("請輸入有效的整數。")
