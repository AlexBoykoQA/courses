
# Задание 3
# # Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
# # Рядом со словом укажите сколько раз оно встречалось в тексте

result = list()
with open('input.txt') as source:
    for line in source:
        result.append(line)

result.sort()
# print(result)

with open('output.txt', 'w') as destination:
    for item in result:
        print(item)
        destination.write(item + '\n')
