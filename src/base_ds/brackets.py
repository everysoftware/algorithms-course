# O(n)
def brackets(s: str) -> int | None:
    open_brackets, close_brackets = "([{", ")]}"
    d = dict(zip(open_brackets, close_brackets))
    stack = []
    for i, c in enumerate(s):
        if c in open_brackets:
            stack.append(i)
        elif c in close_brackets:
            if stack and c == d[s[stack[-1]]]:
                stack.pop()
            else:
                return i + 1
    result = (stack.pop() + 1) if stack else None
    return result
