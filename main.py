# Checking the correctness of the input expression
def is_valid(expr):
    exp = expr.strip().lower()
    valid_opers = '+-*/(). '
    for char in exp:
        if not char.isdigit() and char != '.' and char not in valid_opers and not char.isalpha():
            return False
    return True

# Splitting an input expression into an array of tokens
def tokenize(expr):
    tokens = []
    num = ''
    func = ''
    allow_funcs = ['srqt', 'pow', 'sin', 'cos', 'tg', 'ctg']

    i = 0
    while i < len(expr):
      char = expr[i]

      if char.isdigit() or char == '.':
          num += char

      elif char.isalpha():
          func += char

      else:
          if num:
              tokens.append(num)
              num = ''

          if func:
              if func in allow_funcs:
                  tokens.append(func)
              func = ''

          if char in '+-/*()':
              tokens.append(char)
      i += 1
    if num:
        tokens.append(num)

    return tokens