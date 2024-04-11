# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples

num_samples = int(1e7)  # 這裡可以調整抽樣數量
pi_estimate = monte_carlo_pi(num_samples)
print("單位圓面積的估計值:", pi_estimate)

#___________________________________________________________

import numpy as np

def monte_carlo_integration(func, a, b, num_samples):
    total = 0
    for _ in range(num_samples):
        x = np.random.uniform(a, b)
        total += func(x)
    integral = (b - a) * total / num_samples
    return integral

def function(x):
    return np.sin(x) * np.exp(x)

a = 0  # 積分下限
b = 2 * np.pi  # 積分上限
num_samples = int(1e6)  # 抽樣數量，可以調整
integral_estimate = monte_carlo_integration(function, a, b, num_samples)
print("積分的估計值:", integral_estimate)

#____________________________________________________________

import numpy as np

def monte_carlo_cone_surface_area(num_samples):
    inside_cone = 0
    for _ in range(num_samples):
        # 在圓錐內部隨機選擇一個點 (x, y, z)
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        z = np.random.uniform(0, 1)  # 圓錐高度為1

        # 檢查點是否在單位圓內且在圓錐內部
        if x**2 + y**2 <= 1 and z <= np.sqrt(x**2 + y**2):
            inside_cone += 1

    # 計算蒙地卡羅估計值
    volume_unit_sphere = np.pi
    volume_cone = volume_unit_sphere * inside_cone / num_samples
    base_area_unit_circle = np.pi
    radius_cone = np.sqrt(2)  # 圓錐的半徑為根號2
    surface_area_cone = np.pi * radius_cone + volume_cone

    return surface_area_cone

num_samples = int(1e7)  # 可以調整抽樣數量
surface_area_estimate = monte_carlo_cone_surface_area(num_samples)
print("圓錐表面積的估計值:", surface_area_estimate)
