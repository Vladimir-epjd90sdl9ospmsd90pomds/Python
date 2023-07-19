# import math

# n=700
# m=int(input("Введите путь, время которого нужно рассчитать: "))
# # print((m+n-1)//n)
# print(math.ceil(m/n))

# a = int(input("Введите кол-во человек в первом классе:"))
# b = int(input("Введите кол-во человек во втором классе:"))
# c = int(input("Введите кол-во человек в третьем классе:"))
# print((a//2+a%2)+(b//2+b%2)+(c//2+c%2))

# i = int(input("Введите номер вагона от головы поезда:"))
# j = int(input("Введите номер вагона пассажира:"))
# if i==j:
#     print("Количество вагонов определить невозможно")
# else: print(f"Количество вагонов в поезде: {i+j-1}")

# y = int(input("Введите год:"))
# if y%4==0 and y%100!=0 or y%400==0:
#     print("Yes")
# else: print("No")

# n = 123
# n = str(n)
# res = int(n[0])+int(n[1])+int(n[2])
# print(res)

# n=123
# res = n%10+n%100//10+n//100
# print(res)

# n = 60
# x = int(n/6)
# y = int(4*x)
# print(f'{x}, {y}, {x}')

# n = 385916
# if n//100000+n%100000//10000+n%10000//1000 == n%10+n%100//10+n%1000//100:
#     print('yes')
# else: print('no')

# a=6
# b=3
# c=12

# if c%a==0 or c%b==0:
#     print('yes')
# else: print('no')

# n = 6
# res = 1
# while (n>0):
#     res *=n
#     n-=1
# print(res)

# n = int(input("Введите число:"))
# x1 = 1
# x2 = 2
# tick = 2
# temp = 0
# while x2<=n:
#     temp = x2
#     x2 = x1+x2
#     x1 = temp
#     tick +=1
# if x1 == n: 
#     print(tick)
# else: 
#     print("-1")

# from random import randint

# n = int(input("Введите количество арбузов: "))
# min_mass = ""
# max_mass = ""
# i = 0
# while i<n:
#     x = randint(1,15)
#     if i == 0:
#         min_mass, max_mass = x, x
#     else:
#         if x<min_mass: min_mass = x
#         if x>max_mass: max_mass = x
#     i +=1
#     print(x, end=" ")
# print(f'\n{min_mass}, {max_mass}')

# from random import randint

# n = int(input("Введите кол-во дней для исследования: "))
# count = 0
# res = 0
# for _ in range(n):
#     t = 0+randint(-3, 3)
#     print(t, end=",")
#     if t>0: count += 1
#     elif t<=0 and count>=res:
#         res = count
#         count = 0
#     else:
#         count = 0
# print(f'\n {res}')