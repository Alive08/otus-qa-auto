def validate_number(value):
    if not (isinstance(value, (float, int)) and value > 0):
        raise ValueError(f'{value} should be a positive non-zero number')
    return True
