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

greater_than_previous = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print("Элементы списка, которые больше предыдущего:", greater_than_previous)
