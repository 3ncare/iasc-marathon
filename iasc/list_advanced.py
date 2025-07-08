students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]

max_index = 0
for i in range(1, len(grades)):
    if grades[i] > grades[max_index]:
        max_index = i
top_student = students[max_index]

passed_students = []
for i in range(len(grades)):
    if grades[i] > 60:
        passed_students.append(students[i])

failed_count = 0
for grade in grades:
    if grade < 60:
        failed_count += 1

print(f"студент з найвищою оцінкою: {top_student}")
print(f"студенти з оцінкою менше 60: {passed_students}")
print(f"кількість студентів, які не склали: {failed_count}")



logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]

unique_types = []
for log in logs:
    if log not in unique_types:
        unique_types.append(log)

counts = []
for log_type in unique_types:
    count = logs.count(log_type)
    counts.append([log_type, count])

total_logs = len(logs)
error_count = logs.count("error")
error_percent = (error_count / total_logs) * 100

print("Кількість кожного типу:")
for item in counts:
    print(f"{item[0]}: {item[1]}")
print(f"\nВідсоток повідомлень 'error': {error_percent:.1f}%")




expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]

max_day = ""
max_value = -1
for day in expenses:
    if day[1] > max_value:
        max_value = day[1]
        max_day = day[0]

total = 0
for day in expenses:
    total += day[1]

over_100 = []
for day in expenses:
    if day[1] > 100:
        over_100.append(day[0])

print(f"найбільші витрати: {max_day}")
print(f"загальні витрати: {total}")
print(f"дні з витратами з більше 100: {', '.join(over_100)}")


products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]

total = 0
for product in products:
    total += product[1] * product[2]

most_expensive_name = products[0][0]
most_expensive_price = products[0][2]
for i in range(1, len(products)):
    if products[i][2] > most_expensive_price:
        most_expensive_price = products[i][2]
        most_expensive_name = products[i][0]

product_strings = []
for product in products:
    name = product[0]
    total_price = product[1] * product[2]
    product_strings.append(f"{name} - {total_price} грн")

print(f"сума чеку: {total} грн")
print(f"найдорожчий товар: {most_expensive_name} ({most_expensive_price} грн за одиницю)")
print("сума товарів в чеку:")
for item in product_strings:
    print(item)



squares = [x**2 for x in range(1, 31) 
           if x % 2 == 0 
           and x % 4 != 0 
           and x not in [10, 14, 18]]

print(f'числа: {[x for x in range(1,31) if x%2==0 and x%4!=0 and x not in [10,14,18]]}')