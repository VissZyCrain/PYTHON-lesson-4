# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# 24
# 2 2 2 3

import os
os.system('cls')

print('Задача № 2')

num = int(input("Введите число N: "))
i = 2
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")