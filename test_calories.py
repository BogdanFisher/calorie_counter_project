from calories import calculate_calories


def test_calculate_calories_example():
    # 10 г белка, 5 г жира, 20 г углеводов
    # 4*10 + 9*5 + 4*20 = 40 + 45 + 80 = 165
    assert calculate_calories(10, 5, 20) == 165.0


def test_calculate_calories_zero():
    assert calculate_calories(0, 0, 0) == 0.0


def test_calculate_calories_floats():
    # Проверяем, что работает и с дробными числами
    result = calculate_calories(2.5, 1.5, 3.0)
    expected = 4*2.5 + 9*1.5 + 4*3.0  # 10 + 13.5 + 12 = 35.5
    assert abs(result - expected) < 1e-6