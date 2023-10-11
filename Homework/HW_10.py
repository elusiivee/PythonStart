

#1

def parser(numbers: str) -> list:
    numbers_list = [int(num) for num in numbers.split(' ')]
    return numbers_list

def is_arithmetic_sequence(numbers: list) -> bool:
    if len(numbers) >= 3:
        difference = numbers[-2] - numbers[-1]
        if numbers[-2] - numbers[-1] == difference and numbers[-3] - numbers[-2] == difference:
            return True
        else:
            return False
    else:
        return False

def is_geometric_sequence(numbers: list) -> bool:
    if len(numbers) >= 3:
        difference = numbers[-2] - numbers[-1]
        if numbers[-2] - numbers[-1] == difference and numbers[-3] - numbers[-2] != difference:
            return True
        else:
            return False
    else:
        return False

def next_arithmetic_item(numbers: list)-> str:
    difference = numbers[1] - numbers[0]
    next_number = numbers[-1] + difference
    return f'Next number is {next_number}\nThe row is looking now like: {numbers + [next_number]}'

def next_geometric_item(numbers: list) -> str:
    ratio = numbers[1] / numbers[0]
    next_number= numbers[-1] * ratio
    return f'Next number is {int(next_number)}\nThe row is looking now like: {numbers + [int(next_number)]}'


def get_item(numbers: list):

    if is_arithmetic_sequence(numbers):
        return next_arithmetic_item(numbers)

    if is_geometric_sequence(numbers):
        return next_geometric_item(numbers)

    return None



if __name__ == '__main__':
    numbers = input('Введіть послідовність чисел(мінімум 3), розділену пробілом: ')
    numbers = parser(numbers)
    next_item = get_item(numbers)
    if next_item is not None:
        print(f'Наступний член послідовності: {next_item}')
    else:
        print('Щось не так')
