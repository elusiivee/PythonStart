import random

# #1
# for i in range(1,101):
#     if i%7==0:
#         print(i)

# #2
# sum = 0
# count = 0
# for i in range(1,100):
#     if i %2 != 0:
#         sum +=i
#         count +=1
#
# print(f'Sume: {sum}')
# print(f'Count: {count}')

# # 3
#
# i = 1
# while i < 200:
#     count = 0
#     print('\n')
#     while count < 5:
#         print(i, end=' ')
#         count += 1
#         i += 1
# print('\n')

# # 4
#
# n = int(input('input number: '))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print(factorial)

# # 5                я трішки змінив умову, щоб не тільки на 5 таблицю виводити
#
# a = int(input('Input factor: '))
#
# for i in range(1, 11):
#     print(f'{i} * {a} = {i * a}')

# # 6
#
# width = int(input('Input width: '))
# hight = int(input('Input hidth: '))
#
# print('*' * width)
# for i in range(hight + 1):
#     print('*', end='')
#     print(' ' * (width-2),end='')
#     print('*')
# print('*' * width)

# # 7
# l = [0, 5, 2, 4, 7, 1, 3, 19]
# summ = 0
# for i in l:
#     if i % 2 != 0:
#         summ += i
# print(summ)

# #8
# l1=[]
# l2=[]
# for i in range(4):
#     l1.append(random.randint(1,10))
# l2= l1 + [item*2 for item in l1]
# print(l1)
# print(l2)

# #9
# l1=[]
# for i in range(12):
#     l1.append(random.randint(3000,4000))
# print(round(sum(l1)/12,2))

# # 10
# matrix=[[1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]]
#
# print(matrix)
# sum = 0
# for i in matrix:
#     for j in i:
#         sum+=j
#
# print(sum)

# #11
# l=[]
#
# for i in range(random.randint(5,10)):
#     l.append(random.randint(1,10))
# print('Original: ',l)
# print('Reversed: ',l[::-1])

#12


# #13
#
# width = int(input('Input width: '))
# if width % 2 == 0:
#     print("Ширина повинна бути непарним числом.")
# else:
#     for i in reversed(range(1,width+1,2)):
#         skip = (width-i)//2
#         print(' '* skip + '*'*i)
#     for i in range(1,width+1,2):
#         skip = (width-i)//2
#         print(' '* skip + '*'*i)