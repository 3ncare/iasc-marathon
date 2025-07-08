shopping_list: list[int] = ["хліб", "молоко", "яйця", "картопля", "фрукти"]

print(shopping_list)

shopping_list.append("кава")

print(shopping_list)



name = ["Марія", "Богдан", "Андрій", "Ярослав", "Марго"]

print(name)

name.sort()

print(name)



cities = ['Київ', "Львів", 'Одеса', "Харків", 'Дніпро']

print("список:", cities)

cities[1] = "Чернівці"

print("новий список:", cities)
print("перше місто:", cities[0])
print("останнє місто:", cities[-1])



cars = ['Тойота', 'БМВ', 'Бугатти']

cars.sort()

print(cars)

cars = ['Тойота', 'БМВ', 'Бугатти']

cars.reverse()

print(cars)

cars = ['Тойота', 'БМВ', 'Бугатти']

cars.remove("БМВ")

print(cars)