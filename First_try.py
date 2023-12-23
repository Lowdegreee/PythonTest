import random

def get_user_choice():
    choices = ["камінь", "ножиці", "папір"]
    while True:
        user_choice = input("Виберіть камінь, ножиці або папір: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Будь ласка, введіть коректний варіант: камінь, ножиці або папір.")

def get_computer_choice():
    choices = ["камінь", "ножиці", "папір"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")

    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
         (user_choice == "ножиці" and computer_choice == "папір") or \
         (user_choice == "папір" and computer_choice == "камінь"):
        return "Ви перемогли!"
    else:
        return "Комп'ютер переміг."

def main():
    print("Гра 'Камінь-ножиці-папір'")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
