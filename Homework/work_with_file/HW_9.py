with open('./hw_10_test.txt','r', encoding='UTF-8') as f:
    value_list = []
    for i in f:
        value_list.append(i.split())

category_dict={}
names={}
speciic_name={}
def category(list:list):
    for item  in list:
        categorys = item[-1]
        value = float(item[-2].replace('$', ''))
        if categorys not in category_dict:
            category_dict[categorys] = value   #чому воно не округляється
        else:
            category_dict[categorys] += value
    return category_dict

def expenses_each_name():
    with open('hw_10_test.txt', 'r', encoding='UTF-8') as file:
        for item in file:
            name_part= item.split()
            name = "".join(name_part[1])
            value_str = name_part[-2]  # Assuming the value is the third-to-last element
            value = float(value_str.replace('$', ''))
            if name not in names:
                names[name]=value
            else:
                names[name]+=value
    return names

def get_spec_name(spec_name:str):
    with open('hw_10_test.txt', 'r', encoding='UTF-8') as file:
        for item in file:
            name_part= item.split()
            name = "".join(name_part[1])
            value_str = name_part[-2]  # Assuming the value is the third-to-last element
            value = float(value_str.replace('$', ''))
            if spec_name not in names:
                return 'No person'
            else:
                return f'Count of purchase: {file.read().count(spec_name)}. Total price: {round(names.get(spec_name),2)}'
    return names



category(value_list)
expenses_each_name()
print('Category_____________')

for category, amount in category_dict.items():
    print(f'{category}: ${round(amount,2)}')

print('Name_____________')
for name, amount in names.items():
    print(f'{name}: ${round(amount,2)}')

spec_name=input('Input name(Bob/Mary/Aleksa/Maria/Jack): ')

print(get_spec_name(spec_name))





