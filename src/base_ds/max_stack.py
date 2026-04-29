class MaxStack:
    stack: list[int]
    max_stack: list[int]

    def __init__(self) -> None:
        self.stack = []
        self.max_stack = []

    # O(1)
    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.max_stack:
            self.max_stack.append(x)
            return

        self.max_stack.append(max(x, self.max()))

    # O(1)
    def pop(self) -> int:
        self.max_stack.pop()

        return self.stack.pop()

    # O(1)
    def max(self) -> int:
        return self.max_stack[-1]
