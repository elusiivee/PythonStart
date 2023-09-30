# #1
# my_dict = {}
# text = input('input your text: ')
# count=1
# for i in text.split():
#     if i in my_dict:
#         my_dict.update({i: count+1})
#         count+=1
#     else:
#         my_dict.update({i: count})
#
# print(my_dict)

# #2
# translations = {
#     'hello': 'привіт',
#     'goodbye': 'до побачення',
#     'cat': 'кіт',
#     'dog': 'собака'
# }
#
# word = input('Input your word: ')
#
# if word in translations.keys():
#     print(translations.get(word))
# elif word in translations.values():
#     for key, val in translations.items():
#         if val == word:
#             print(key)
# else:
#     print('none')

# # 3
# my_dict = {}
# while True:
#
#     act = input('Input your action (add / delete / get / stop): ')
#
#
#     if act == 'add':
#         name = input('Input the name of your contact: ')
#         phone = input('Input the phone number: ')
#         my_dict[name] = phone
#         print(my_dict)
#         print(' ')
#     elif act == 'delete':
#         name = input('Input the name of your contact: ')
#         if name in my_dict.keys():
#             my_dict.pop(name)
#             print(my_dict)
#             print(' ')
#         else:
#             print('There is any contact with this name:')
#             print(' ')
#     elif act == 'get':
#         name = input('Input the name of your contact: ')
#         if name in my_dict.keys():
#             print(f'{name}`s phone number is {my_dict.get(name)}')
#             print(' ')
#         else:
#             print('There is any contact with this name')
#     if act == 'stop':
#         break  # Exit the loop when 'stop' is entered


# #4
# my_list = {'UAH to USD': 0.027, 'USD to UAH': 36.97}         # набагато легше булоб використати бібліотеку currencies
#
# currency = input('Input your currency (UAH / USD): ')
# amount = float(input('Input your amount of money (9999.99): '))
# money = 0
# if currency == 'UAH':
#     money= amount * my_list.get('UAH to USD')
#     print(money)
# elif currency == 'USD':
#     money = amount * my_list.get('USD to UAH')
#     print(money)
# else:
#     print('Unavailable currency')