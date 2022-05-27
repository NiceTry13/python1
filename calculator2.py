# Калькулятор версия 2 с разными цветами

# Добавление библиотеки colorama
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK)
print(Back.GREEN)
# Переменная what  с запросом какую операцию делаем
what = input("Что делаем? (+, -): ")

print(Back.CYAN)

# Переменная а через input и преобразование во float для корректного сложения и вычитания
a = float( input("Введи первое число: "))
# Переменная b через input и преобразование во float для корректного сложения и вычитания
b = float( input("Введи второе число: "))

# условия для выполнения операци с пеобразованием переменной c в str для правильной конкатенации
print(Back.YELLOW)

if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана неверная операция")

input('Press ENTER to exit')