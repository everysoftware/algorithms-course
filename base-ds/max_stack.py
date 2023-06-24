class MaxStack:
    def __init__(self):
        self.st = []
        self.max_st = []

    def push(self, x):
        self.st.append(x)
        curr_max = x if not self.max_st or x > self.max_st[-1] else self.max_st[-1]
        self.max_st.append(curr_max)

    def pop(self):
        self.max_st.pop()
        return self.st.pop()

    def max(self):
        return self.max_st[-1]

