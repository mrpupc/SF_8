def game_core_v3(number: int = 1) -> int:
    """ Сначала устанавливаем среднее число из заданного диапазона, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    low = 1
    high = 100
    predict = (low + high) // 2

    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1
        else:
            high = predict - 1
        predict = (low + high) // 2
    # Ваш код заканчивается здесь

    return count
print(game_core_v3(70))