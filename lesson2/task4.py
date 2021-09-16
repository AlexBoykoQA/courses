#Создайте словарь характеристик продукта с ключами «title» (значение типа данных str), «price» (значение численного типа данных), «ingredients» (значение – список строк).

thisdict = {
  "title": "BMW",
  "price": 100500,
  "ingredients": ["x1", "x2", "x3"]
}

# 1. Добавьте еще одну пару ключ-значение - «description»: какой-то текст
thisdict["description"] = "super car"
print(thisdict)

# 2. Увеличьте цену на 100.
thisdict["price"] += 100
print(thisdict)

# 3. Добавьте в список ингредиентов еще один ингредиент.
thisdict["ingredients"].append("x4")
print(thisdict)

# 4. Выведите на экран количество ингредиентов продукта.
print(len(thisdict["ingredients"]))

# 5. Удалите из словаря значение с ключом «description»
thisdict.pop("description")
print(thisdict)
