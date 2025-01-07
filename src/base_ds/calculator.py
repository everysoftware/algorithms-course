priority = {
    "(": 0,
    ")": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a**b,
}


# O(N)
def split_by_tokens(expression: str) -> list[str]:
    tokens = []
    token = ""

    for c in expression:
        if c.isdigit() or c in ".":
            token += c
        elif not c.isspace():
            if token:
                tokens.append(token)
                token = ""
            tokens.append(c)

    if token:
        tokens.append(token)

    return tokens


# O(N)
def get_postfix_notation(expression: str) -> str:
    notation: list[str] = []
    stack: list[str] = []
    tokens = split_by_tokens(expression)

    for token in tokens:
        if token in priority:
            # Открытие скобочного выражения.
            if not stack or token == "(":
                stack.append(token)
            # Закрытие скобочного выражения.
            elif token == ")":
                top = stack.pop()

                while top != "(":
                    notation.append(top)
                    top = stack.pop()
            # При очередной операции добавляем в результат, все операции из стека с большим или равным приоритетом.
            elif priority[token] <= priority[stack[-1]]:
                top = stack.pop()
                notation.append(top)

                while stack and priority[top] != priority[token]:
                    top = stack.pop()
                    notation.append(top)

                stack.append(token)
            else:
                stack.append(token)
        else:
            notation.append(token)

    notation += stack

    return " ".join(notation)


# O(N)
def evaluate_postfix(expression: str) -> float:
    stack: list[float] = []

    for token in expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)  # type: ignore[no-untyped-call]
            stack.append(result)
        else:
            stack.append(float(token))

    return stack[0] if stack else 0.0


# O(N)
def calculator(expression: str) -> tuple[str, float]:
    postfix_notation = get_postfix_notation(expression)
    result = evaluate_postfix(postfix_notation)

    return postfix_notation, result
