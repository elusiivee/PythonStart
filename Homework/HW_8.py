# 1
def concatination(text: str, num1: int, num2: int):
    return text + (str(num1 + num2))


print(concatination('I am', 10, 9))


# 2
def square(h: int, w: int):
    print('*' * w)
    for i in range(h - 2):
        print('*' + ' ' * (w - 2) + '*')
    print('*' * w)


print(square(6, 5))

# 3

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def num_indicate(num_list: list, value: int):
    if value in num_list:
        return num_list.index(value)
    else:
        return -1


print('Value index: ', num_indicate(num_list, 4))


# 4


def word_amount(text: str):
    return len(text.split())


print('Amount of words: ', word_amount('I am hungry. I wont eat apple'))

ste1 = input()

res = set(ste1)
print(res)
