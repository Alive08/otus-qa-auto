def validate_number(value):
    "Проверка, может ли число быть каким-либо из размеров фигуры"

    if not (isinstance(value, (float, int)) and value > 0):
        raise ValueError(f'{value} must be a positive non-zero number')
    return True
