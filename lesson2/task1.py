#(Подсказка: ищите как это сделать с помощью методов строк)
# 1. Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)
x = "t e.st"
print(x.isdigit())

# 2. Посчитайте сколько у вас пробелов в строке.
print(x.count(' '))

# 3. Посчитайте сколько у вас символов точки '.' в строке.
print(x.count('.'))

# 4. Создайте строку "Homework". Преобразуйте её в строку длиной 100 символов, посередине которой исходное слово,
# а с обоих сторон строка заполнена пробелами. Выведите её на экран. Убедитесь, что у вас 100 символов (посчитайте длину).

y = "Homework"
y = y.center(100," ")
print(y)
print(len(y))

# 5. Сделайте первые буквы слов строки большими (upper case).
z = "some text"
print(z.title())

# 6. Определите заканчивается ли ваша строка подстрокой “ing”.
a = "testing"
print(a.endswith("ing"))

# 7. Определите индекс первого вхождения символа “a” в вашей строке
b = "cases"
print(b.index("a"))

# 8. Разбейте строку на список подстрок по символу пробела.
c = "functional testing"
print(c.split())

# 9. Пусть у вас строка имеет пробельные символы. Найдите метод, который удаляет пробельные символы вначале и в конце, но не посередине.
d = "  test 1223  "
print(d.strip())