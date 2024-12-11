numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input == "end":
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Пожалуйста, введите корректное число или 'end'.")

print("Список введенных чисел:", numbers)

if numbers:
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    print("Список после замены минимального и максимального элементов:", numbers)
