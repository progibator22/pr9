a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
start = min(a, b)
end = max(a, b)

squares = [x**2 for x in range(start + 1, end)]
print("Список квадратов чисел между a и b:", squares)
