import os
from game import play_game
from shop import shop

score = 0
best_score = 0

if os.path.exists("score.txt"):
    with open("score.txt", "r") as f:
        best_score = int(f.read())

while True:
    print("\n====================")
    print("🎮 ГЛАВНОЕ МЕНЮ")
    print("====================")
    print("1 - Играть")
    print("2 - Магазин")
    print("0 - Выход")
    print(f"⭐ Очки: {score}")
    print(f"🏆 Рекорд: {best_score}")

    choice = input("Выбор: ")

    if choice == "0":
        print("👋 Выход из игры")
        break

    elif choice == "1":
        score, continue_game = play_game(score)

        if score > best_score:
            best_score = score
            print("🏆 НОВЫЙ РЕКОРД!")

            with open("score.txt", "w") as f:
                f.write(str(best_score))

        if not continue_game:
            break

    elif choice == "2":
        score = shop(score)

    else:
        print("❌ Неверный выбор")