# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:46:21 2024

@author: kkjj1
"""

import cmath

def quadratic_formula(a, b, c):
    # 计算判别式
    discriminant = b**2 - 4*a*c
    
    # 判断判别式的值，确定解的类型
    if discriminant > 0:
        # 两个实根
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # 重根
        root = -b / (2*a)
        return root
    else:
        # 两个虚根
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# 输入系数
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))

# 解一元二次方程
solutions = quadratic_formula(a, b, c)

print("解为:", solutions)