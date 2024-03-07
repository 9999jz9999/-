# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:43:51 2024

@author: kkjj1
"""

import math

def calculate_circle_properties(radius):
    # 計算圓周長
    circumference = 2 * math.pi * radius
    
    # 計算圓面積
    area = math.pi * radius**2
    
    return circumference, area

def main():
    # 使用者輸入半徑
    radius = float(input("請輸入圓的半徑: "))
    
    # 計算圓周長和圓面積
    circumference, area = calculate_circle_properties(radius)
    
    # 輸出結果
    print(f"圓周長: {circumference:.2f}")
    print(f"圓面積: {area:.2f}")

if __name__ == "__main__":
    main()
