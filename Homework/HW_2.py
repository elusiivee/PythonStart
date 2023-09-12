# 1
value = int(input('Input your number: '))
if value < 20:
    print(f'{value} is less than 20')
elif value > 20:
    print(f'{value} is more than 20')
else:
    print(f'{value} is equals to 20')

# 2
value = int(input('Input your number: '))
if value == 0:
    print(f'{value} is equals to 0')
else:
    print(f'{value} isn`t equals to 0')

# 3
value = int(input('Введіть ваше число: '))
if value % 2 == 0:
    print('Парне')
else:
    print('Непарне')

#4
array = []

for i in range(3):
    value=int(input('Input your number'))
    array.append(value)

print(f'max value = {max(array)}')


#5
value = int(input('Введіть ваше число: '))

if value % 3 ==0 and value % 5 !=0:
    print('Число підходить')
else:
    print('Число не підходить')