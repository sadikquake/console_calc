def is_valid(expr):
    exp = expr.strip().lower()
    valid_chars = '0123456789+-*/(). '
    for char in exp:
        if char not in valid_chars:
            return False
    return True

