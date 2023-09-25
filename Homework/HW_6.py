import math

# 1

text = input('Your text: ')
count = 0
for i in text:
    if i == 'b':
        count += 1

print(count)

# 2

name = input('Input your name: ')

if name.istitle() and name.isalpha():
    print('ALl right')
else:
    print('error')

# 3

text = input('Input your text: ')

total = 0

for i in text:
    total = ord(
        i)  # можливо я не так зрозумів завдання але знайшов метод що повертає ціле число, що представляє символ Unicode.
print(total)

# 4
for i in range(10):
    print(round(math.pi, i + 1))

# 5
list_of_Sentences = input('input your text: ').split()
longest_word = ''
for i in list_of_Sentences:
    if len(i) > len(longest_word):
        longest_word = i
    else:
        continue
print(longest_word)

# 6                  #скоріше за все не правильна ногіка тому що слово наприклад tattattat не буде працювати
text = input("Input text: ")
word = ''
for i in text:
    if i not in word:
        word += i
    else:
        continue
print(word)

# 7


text = input('Input your text: ')

while '<' in text:
    start = text.find('<')
    end = text.find('>')
    text = text[:start] + text[end + 1:]

print(text)
