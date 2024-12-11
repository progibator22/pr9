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
