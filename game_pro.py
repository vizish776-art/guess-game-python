import random

while True:
    print("\n=== ИГРА УГАДАЙ ЧИСЛО ===")
    print("1 - Легко (1–5)")
    print("2 - Средне (1–10)")
    print("3 - Сложно (1–20)")
    print("0 - Выход")

    choice = input("Выбери режим: ")

    if choice == "0":
        print("Выход из игры 👋")
        break

    if choice == "1":
        secret = random.randint(1, 5)
        attempts = 3
    elif choice == "2":
        secret = random.randint(1, 10)
        attempts = 3
    elif choice == "3":
        secret = random.randint(1, 20)
        attempts = 4
    else:
        print("Неверный выбор")
        continue

    print(f"У тебя {attempts} попыток!")

    while attempts > 0:
        guess = int(input("Угадай число: "))

        if guess == secret:
            print("Победа 🎉")
            break
        else:
            attempts -= 1
            print("Неверно 😄 осталось:", attempts)

    if attempts == 0:
        print("Проигрыш 😢 число было:", secret)