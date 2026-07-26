def calculate_calories(protein: float, fat: float, carbs: float) -> float:
    """
    Считает калории по формуле:
    калории = 4 * белки + 9 * жиры + 4 * углеводы
    Возвращает число.
    """
    return 4 * protein + 9 * fat + 4 * carbs


def get_float_input(prompt: str) -> float:
    """
    Просит пользователя ввести число. Если не число — просит снова.
    Использует try/except и цикл.
    Возвращает float.
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Значение не может быть отрицательным. Попробуйте ещё раз.")
                continue
            return value
        except ValueError:
            print("Это не число. Пожалуйста, введите корректное значение.")


if __name__ == "__main__":
    # Здесь только интерактивная часть: ничего не меняем в функциях
    print("Калькулятор калорий")
    p = get_float_input("Введите количество белков (г): ")
    f = get_float_input("Введите количество жиров (г): ")
    c = get_float_input("Введите количество углеводов (г): ")

    total = calculate_calories(p, f, c)
    print(f"Общая калорийность: {total:.1f} ккал")