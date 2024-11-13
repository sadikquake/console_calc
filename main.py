# Checking the correctness of the input expression
def is_valid(expr):
    exp = expr.strip().lower()
    valid_opers = '+-*/(). '
    for char in exp:
        if not char.isdigit() and char != '.' and char not in valid_opers and not char.isalpha():
            return False

        if exp[-1] in '+-*/':
            return False
    return True

# Splitting an input expression into an array of tokens
def tokenize(expr):
    if not is_valid(expr):
        return False

    tokens = []
    num = ''
    func = ''
    allow_funcs = ['sqrt', 'pow', 'sin', 'cos', 'tg', 'ctg']

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

    if func and func in allow_funcs:
        tokens.append(func)

    return tokens

# Convert expression to rpn form
def exp_to_rpn(expr):
    tokens = tokenize(expr)
    if not tokens:
        return False

    priorities = {'+': 1, '-': 1, '*': 2, '/': 2, 'sin': 3, 'cos': 3, 'tg': 3, 'ctg': 3, 'sqrt': 3, 'pow': 3}
    res = []
    funcs = []

    for tok in tokens:
        if tok.isdigit() or '.' in tok:
            res.append(tok)
        elif tok in priorities:
            while (funcs and funcs[-1] != '(' and priorities.get(tok, 0) <= priorities.get(funcs[-1], 0)):
                res.append(funcs.pop())
            funcs.append(tok)
        elif tok == '(':
            funcs.append(tok)
        elif tok == ')':
            while funcs and funcs[-1] != '(':
                res.append(funcs.pop())
            funcs.pop()
            if funcs and funcs[-1] in priorities and funcs[-1].isalpha():
                res.append(funcs.pop())

    while funcs:
        res.append(funcs.pop())

    return res