priorities = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    "(": 0
}


def split_by_tokens(expression: str) -> list[str]:
    """Разбивает строку на токены. Сложность O(N)."""
    tokens = []
    token = ""

    for c in expression:
        if c.isdigit() or c.isalpha() or c in "().":
            token += c
        else:
            if token != "":
                tokens.append(token)
                token = ""
            tokens.append(c)

    if token != "":
        tokens.append(token)

    return tokens


def get_postfix_notation(expression: str) -> list[str]:
    """Преобразует инфиксное выражение в постфиксное. Сложность O(N)."""
    notation, stack = [], []
    tokens = split_by_tokens(expression)

    for token in tokens:
        if token in "+-*/()^":
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
            elif priorities[token] <= priorities[stack[-1]]:
                top = stack.pop()
                notation.append(top)
                while stack and priorities[top] != priorities[token]:
                    top = stack.pop()
                    notation.append(top)
                stack.append(token)
            else:
                stack.append(token)
        else:
            notation.append(token)

    notation += stack

    return notation
