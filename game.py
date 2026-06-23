import random

def play_game(score):
    print("\n=== 🎮 УГАДАЙ ЧИСЛО ===")
    print("1 - Легко (1–5)")
    print("2 - Средне (1–10)")
    print("3 - Сложно (1–20)")
    print("0 - Выход")

    choice = input("Выбери режим: ")

    if choice == "0":
        return score, False

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
        print("❌ Неверный выбор")
        return score, True

    print(f"У тебя {attempts} попыток!")

    while attempts > 0:
        try:
            guess = int(input("Угадай число: "))

            if guess == secret:
                print("🎉 Победа!")
                gained = attempts * 10
                score += gained
                print(f"⭐ +{gained} очков")
                break

            elif guess < secret:
                print("📉 Слишком маленькое число")
            else:
                print("📈 Слишком большое число")

            attempts -= 1
            print("Осталось попыток:", attempts)

        except ValueError:
            print("⚠ Введи число!")

    if attempts == 0:
        print("💀 Проигрыш! число было:", secret)

    return score, True