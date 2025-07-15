def hello_world():
  print("Hello World")

hello_world()


def greet(fname):
  print(fname)

greet("Anna")


def my_function(num):
  num = 5
  return num ** 2

print(my_function(5))



def add(a, b):
    return a + b
print(add(5, 5))



def greet_default(name="Гість"):
    print(f"Привіт, {name}!")
greet_default()



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))



def is_even(n):
    return n % 2 == 0
print(is_even(4))



def print_numbers(n):
    for int in range(1, n+1):
        print(int)
print_numbers(3)



def find_name(name, name_list):
    return name in name_list
print(find_name("Anna", ["Ivan", "Anna", "Petro"]))

print(find_name("Anna", ["Margo", "Ivan"]))



def max_of_three(a, b, c):
   print(a + b + c)

max_of_three(5, 6, 3)


def reverse_string(s):
    return s[::-1]
print(reverse_string("Словомабуть"))



def count_vowels(s):
    vowels = "аеиіоуюяєїАЕИІОУЮЯЄЇ"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Мова"))



def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0
print(average(1, 2, 3, 4))



def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_user_info(name="Ivan", age=30, wife="Anna")



def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()
outer()