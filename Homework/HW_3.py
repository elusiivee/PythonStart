# 1

room_number = int(input('Room number: '))

entrance_number = ((room_number - 1) // 36) + 1
floor_number = (room_number - 1) % 36 // 4 + 1
room_number_on_floor = ((room_number - 1) % 4) + 1
if room_number >= 1 and room_number <= 144:
    print(f'entrance: {entrance_number}, floor: {floor_number}, number on the floor: {room_number_on_floor}')
else:
    print('there is no such room ')
# 2

year = int(input('Year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('leap year')
else:
    print('Not a leap year')

# 3

a = int(input('a side: '))
b = int(input('b side: '))
c = int(input('c side: '))

if a + b > c and b + c > a and c + a > b:
    print('the triangle exists')
else:
    print('the triangle doesn`t exists')

# 1 additional
print('Registration')
password = input('input your password: ')
print('Login')
re_password = input('input your password on more time: ')

if password == re_password:
    print('Доступ дозволено')
else:
    print('Доступ заборонено')

# 2

sum = int(input('input your purchase amount'))

if sum > 1000:
    print(sum - sum * 0.1)
else:
    print('You have a discount and your sum is: ', sum)

# 3 рік береться і провіряється з 2 завдання

month = int(input('input your month'))

if month in [1, 4, 6, 9, 11]:
    print(30)
elif month == 2:
    print(30)
else:
    print(31)

# 4
rate = int(input('Please rate from 1 to 5'))

if rate == 1:
    print('Жахливо')
elif rate == 2:
    print('Погано')
elif rate == 3:
    print('Задовільно')
elif rate == 4:
    print('Добре')
elif rate == 5:
    print('Відмінно')
else:
    print('false input')

# 5
height = float(input('Your height in m: '))
weight = float(input('Your weight in kg: '))

iwb = weight / height ** 2
print(iwb)
if iwb <= 18.5:
    print('the weight is not enough')
elif 18.5 < iwb < 24.9:
    print('the weight is ok')
elif 25.0 < iwb < 29.9:
    print('You are overweight')
elif iwb > 30:
    print('you are very overweight')
