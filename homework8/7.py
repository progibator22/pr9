import random

def generate_ticket():
    return [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

def get_user_choice(ticket):
    user_choices = []
    for row in ticket:
        while True:
            try:
                choice = int(input(f"Choose a number from {row}: "))
                if choice in row and choice not in user_choices:
                    user_choices.append(choice)
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
    return user_choices

def get_random_choice(ticket):
    return [random.choice(row) for row in ticket]

def main():
    ticket = generate_ticket()
    user_choices = get_user_choice(ticket)
    random_choices = get_random_choice(ticket)
    matches = set(user_choices) & set(random_choices)
    print(f"Your choices: {user_choices}")
    print(f"Random choices: {random_choices}")
    print(f"Matches: {matches}")
    print(f"Number of matches: {len(matches)}")

if __name__ == "__main__":
    main()
