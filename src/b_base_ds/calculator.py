# O(n)
def calculator(expression: str) -> float:
    postfix_notation = get_postfix_notation(expression)
    result = evaluate_postfix(postfix_notation)
    return result


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


# O(n)
def get_postfix_notation(expression: str) -> str:
    notation: list[str] = []
    operations: list[str] = []
    tokens = split_by_tokens(expression)
    for i, token in enumerate(tokens):
        # Число.
        if token not in priority:
            notation.append(token)
        # Операция.
        else:
            # Открытие скобочного выражения.
            if token == "(":
                operations.append(token)
            # Закрытие скобочного выражения.
            elif token == ")":
                while operations and operations[-1] != "(":
                    notation.append(operations.pop())
                operations.pop()
            # Операция.
            else:
                # Унарный плюс или минус.
                if token in "+-" and (i == 0 or tokens[i - 1] in priority or tokens[i - 1] == "("):
                    notation.append("0")
                # Перенос операций с большим или равным приоритетом из стека в выходную строку.
                while operations and priority[operations[-1]] >= priority[token]:
                    notation.append(operations.pop())
                operations.append(token)
    # Перенос оставшихся операций из стека в выходную строку.
    notation += operations[::-1]
    return " ".join(notation)


# O(n)
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


# O(n)
def split_by_tokens(expression: str) -> list[str]:
    tokens = []
    token = ""
    for c in expression:
        if c.isdigit() or c == ".":
            token += c
        elif not c.isspace():
            if token:
                tokens.append(token)
                token = ""
            tokens.append(c)
    if token:
        tokens.append(token)
    return tokens
