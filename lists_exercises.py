shopping_list: list[int] = ["хліб", "молоко", "яйця", "картопля", "фрукти"]

print(shopping_list)

shopping_list.append("кава")

print(shopping_list)



name = ["Марія", "Богдан", "Андрій", "Ярослав", "Марго"]

print("список:", name)

name.sort()

print("виведені імена у алфавітному порядку:", name)



cities = ['Київ', "Львів", 'Одеса', "Харків", 'Дніпро']

print("оригінальний список:", cities)

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