with open('./hw_10_test.txt','r', encoding='UTF-8') as f:
    value_list = []
    for i in f:
        value_list.append(i.split())

category_dict={}
def category(list:list):
    for item  in list:
        category = item[-1]
        value = round(float(item[-2].replace('$', '')),2)
        if category not in category_dict:
            category_dict[category] = value
        else:
            category_dict[category] += value
    return category_dict


print(value_list)


category(value_list)

for category, total in category_dict.items():
    print(f'{category}: ${total}')




