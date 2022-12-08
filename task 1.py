# Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример:
# - при $d = 0.001, π = 3.141.$   
#  $10^{-1} ≤ d ≤10^{-10}$

import os
os.system('cls')

print('Задача № 1')

from math import pi
num = int(input('Введите число знаков после запятой в числе Пи '))
stroka = str(pi)
print(stroka[0:num+2])