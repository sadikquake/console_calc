def is_valid(expr):
    valid_chars = '0123456789+-*/(). '
    for char in expr:
        if char not in valid_chars:
            return False
    return True

expr = '2*2 + 3 / 4 * 7@'

if(is_valid(expr)):
    print('Ok')
else:
    print('NOT')