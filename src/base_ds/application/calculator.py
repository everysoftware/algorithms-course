"""
Задача: Реализовать алгоритм разбора арифметического выражения. Допустимые операции в выражении: "+", "-", "*", "/",
числовые литералы, круглые скобки для задания приоритетности.

Формат ввода
Входные данные: В качестве входа для алгоритма задана единственная строка - записанное арифметическое выражение.

Формат вывода
Результат: Результатом работы алгоритма является вычисленное значение входного выражения.
Помимо результата необходимо вывести запись исходного выражения в постфиксной записи (обратной польской записи).
"""

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


def split_by_tokens(expression: str) -> list[str]:
    """Разбивает строку на токены. Сложность O(N)."""
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


def get_postfix_notation(expression: str) -> str:
    """Преобразует инфиксное выражение в постфиксное. Сложность O(N)."""
    notation, stack = [], []
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


def evaluate_postfix(expression: str) -> float:
    """Вычисляет значение выражения, записанного в обратной польской нотации. Сложность O(N)."""
    stack = []

    for token in expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        else:
            stack.append(float(token))

    return stack[0] if stack else 0.0
