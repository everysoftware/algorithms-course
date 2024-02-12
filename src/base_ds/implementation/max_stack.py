"""
https://stepik.org/lesson/41234/step/4?unit=19818

Стек — абстрактная структура данных, поддерживающая операции push и pop. Несложно реализовать стек так,
чтобы обе эти операции работали за константное время. В данной задаче ваша цель — расширить интерфейс стека так,
чтобы он дополнительно поддерживал операцию max и при этом чтобы время работы всех операций по-прежнему было
константным.

Формат входа. Первая строка содержит число запросов q. Каждая из
последующих q строк задаёт запрос в одном из следующих форматов: push v, pop, or max.

Формат выхода. Для каждого запроса max выведите (в отдельной
строке) текущий максимум на стеке.
"""


class MaxStack:
    stack: list[int]
    max_stack: list[int]

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.max_stack:
            self.max_stack.append(x)
            return

        self.max_stack.append(max(x, self.max()))

    def pop(self) -> int:
        self.max_stack.pop()

        return self.stack.pop()

    def max(self) -> int:
        return self.max_stack[-1]
