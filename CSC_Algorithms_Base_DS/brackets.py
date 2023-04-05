def brackets(s):
    opening_brackets = '([{'
    closing_brackets = ')]}'
    d = dict(zip(closing_brackets, opening_brackets))
    st = []
    for i, c in enumerate(s):
        if c in opening_brackets:
            st.append((c, i))
        elif c in closing_brackets and (not st or d[c] != st.pop()[0]):
            return i + 1
    return st[0][1] + 1 if st else -1


def brackets_improved(s):
    opening_brackets = '([{'
    closing_brackets = ')]}'
    d = dict(zip(closing_brackets, opening_brackets))
    st = []
    for i, c in enumerate(s):
        if c in opening_brackets:
            st.append(i)
        elif c in closing_brackets and (not st or d[c] != s[st.pop()]):
            return i + 1
    return st[0] + 1 if st else -1
