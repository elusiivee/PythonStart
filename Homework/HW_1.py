from statistics import mean
import math


#1
name = input('Input your name: ')
print(name)
print('#######################')

#2
MyArray = []
for i in range(5):
    number = int(input('input your number: '))
    MyArray.append(number)
print('Max value',max(MyArray))
print('Min value',min(MyArray))
print('Avarage value',mean(MyArray))
print('#######################')

# 3
x = float(input('Input your first value x:'))
y = float(input('Input your first value y:'))
act = input('input your action (+,-,*,/)')

if act == '+':
    print(x + y)
elif act == '-':
    print(x - y)

elif act == '/':
    if y == 0:
        print('You can`t divide by 0')
    else:
        print(x / y)
elif act == '*':
    print(x * y)
print('#######################')
# 4
radius = float(input('Input your radius: '))
print(f'Diameter = {radius*2}')
print(f'Length = {radius*math.pi*2}')
print(f'Square = {((radius)**2)*math.pi}')
print('#######################')

# 5
p = int(input('initial amount invested: '))
r = 0.1
n = int(input('Amount of the years(10, 20 or 30): '))

print(f'Amount on deposit at the end of {n} year = {round(p*(1+r)**n, 2)}')
print('#######################')

# 6
cash = float(input('input your amount of money: '))
dollar_rate = 37
print('In hryvna it will be +',cash*dollar_rate)
print('#######################')

# 7
number=int(input('input your number: '))
print(number//100)
print((number//10)%10)
print(number%10)

