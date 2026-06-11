import random
import os

score = 0
best_score = 0
hint_cost = 15

# загрузка рекорда
if os.path.exists("score.txt"):
    with open("score.txt", "r") as f:
        best_score = int(f.read())

def shop():
    global score, hint_cost
    print("\n🛒 МАГАЗИН:")
    print("1 - Купить подсказку (-1 попытка раскрывает диапазон) | 15 очков")
    print("0 - Выход")

    choice = input("Выбор: ")

    if choice == "1":
        if score >= hint_cost:
            score -= hint_cost
            print("💡 Подсказка куплена! В следующей игре будет помощь.")
            return True
        else:
            print("❌ Не хватает очков!")
    return False


while True:
    print("\n=== 🎮 УГАДАЙ ЧИСЛО ===")
    print("1 - Легко (1–5)")
    print("2 - Средне (1–10)")
    print("3 - Сложно (1–20)")
    print("4 - 🛒 Магазин")
    print("0 - Выход")

    print(f"⭐ Очки: {score}")
    print(f"🏆 Рекорд: {best_score}")

    choice = input("Выбери режим: ")

    if choice == "0":
        print("👋 Выход из игры")
        print("⭐ Финальные очки:", score)
        break

    if choice == "4":
        shop()
        continue

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
        continue

    print(f"\nУ тебя {attempts} попыток!")

    while attempts > 0:
        try:
            guess = int(input("Угадай число: "))

            if guess == secret:
                print("🎉 Победа!")
                gained = attempts * 10
                score += gained
                print(f"⭐ +{gained} очков")

                if score > best_score:
                    best_score = score
                    print("🏆 НОВЫЙ РЕКОРД!")

                    with open("score.txt", "w") as f:
                        f.write(str(best_score))

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

    print("\n🔁 Сыграть ещё?")
    again = input("да / нет: ")

    if again.lower() != "да":
        print("🏁 Игра завершена. Очки:", score)
        break