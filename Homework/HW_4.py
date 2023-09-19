# 1
num_list = list(map(int, input('Input Four-digit number: ')))
a = sum(num_list[:2])
b = sum(num_list[-2:])

if a == b:
    print('Щасливий квиток')
else:
    print('Не щасливий квиток')

# 2

palindrom = list(map(int, input('Input Six-digit number: ')))

if palindrom == list(reversed(palindrom)):
    print('Це є паліндром')
else:
    print('Це не є паліндром')

# 3
x = int(input('Enter the coordinate x: '))
y = int(input('Enter the coordinate y: '))
radius = 4
if x ** 2 + y ** 2 <= radius ** 2:
    print('Точка знаходиться в колі')
else:
    print('Точка не знаходиться в колі')
