import math

#
# # 1
#
# text = input('Your text: ')
#
# print(text.count('b'))
#
# # 2
#
# name = input('Input your name: ')
#
# if name.istitle() and name.isalpha():
#     print('ALl right')
# else:
#     print('error')
#
# # 3
#
# text = input('Input your text: ')
#
# total = 0
#
# for i in text:
#     total += ord(
#         i)  # можливо я не так зрозумів завдання але знайшов метод що повертає ціле число, що представляє символ Unicode.
# print(total)
#
# # 4
# for i in range(10):
#     print(round(math.pi, i + 1))
#
# # 5
# list_of_Sentences = input('input your text: ').split()
# max(list_of_Sentences, key=len)
#
# # 6                  #скоріше за все не правильна ногіка тому що слово наприклад tattattat не буде працювати
# text = input("Input text: ")
# word = ''
# for i in text:
#     if i not in word:
#         word += i
#     else:
#         continue
# print(word)
#
# # 7
#
#
# text = input('Input your text: ')
#
# while '<' in text:
#     start = text.find('<')
#     end = text.find('>')
#     text = text[:start] + text[end + 1:]
#
# print(text)


# add

DEPOSIT_AMOUNT = 100000
ANNUAL_INTEREST_RATE = 15
TAX_RATE = 19.5
DEPOSIT_MONTHS = 72
YEAR = int(DEPOSIT_MONTHS / 12)
AMOUT_OF_MONEY = 0

print('The total amount of profit for each year:')
for i in range(1, YEAR + 1):
    AMOUT_OF_MONEY = DEPOSIT_AMOUNT * (1 + ANNUAL_INTEREST_RATE*0.01) ** i
    print(f'Year {i}: {round(AMOUT_OF_MONEY, 2)}')


print('The total amount of profit for each month:')
for i in range(DEPOSIT_MONTHS):
    monthly_money = (DEPOSIT_AMOUNT* ANNUAL_INTEREST_RATE/12)/100
    print(f"Місяць {i+1}: ${monthly_money:.2f}")



