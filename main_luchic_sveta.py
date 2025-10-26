#
def start_game():
    print("Цель: Найти Лучик света")
    print("Готов в путь?")
    choice = input("Введите 'Да' или 'Нет': ").strip().lower()

    if choice == "нет":
        print("Игра закончилась.")
        return
    elif choice == "да":
        first_choice()
    else:
        print("Неправильный ввод. Попробуйте снова.")
        start_game()


def first_choice():
    print("\nВы оказались на развилке. Куда пойдете?")
    print("1. Тропа тьмы")
    print("2. Река Искр")
    print("3. Рассказать добрую историю")
    choice = input("Выберите номер: ").strip()

    if choice == "1":
        print("Вы попали в тупик. Проигрыш.")
    elif choice == "2":
        print("Река Искр. Чтобы продолжить, нужно разгадать загадку.")
        print("Отгадка: Время")
        answer = input("Ваш ответ: ").strip().lower()
        if answer == "время":
            print("Правильно! Вы можете продолжить путь.")
            second_choice()
        else:
            print("Неправильный ответ. Проигрыш.")
    elif choice == "3":
        print("Вы рассказали добрую историю. Продолжайте путь.")
        second_choice()
    else:
        print("Неправильный ввод. Попробуйте снова.")
        first_choice()


def second_choice():
    print("\nВы вошли в Пещеру Кристаллов. Куда пойдете?")
    print("1. Влево")
    print("2. Вправо")
    print("3. В шкафу")
    choice = input("Выберите номер: ").strip()

    if choice == "1":
        print("Тупик. Проигрыш.")
    elif choice == "2":
        print("Под кроватью. УРА! Лучик найден!")
    elif choice == "3":
        print("В шкафу ничего нет. Попробуйте снова.")
        second_choice()
    else:
        print("Неправильный ввод. Попробуйте снова.")
        second_choice()


if __name__ == "__main__":
    start_game()
