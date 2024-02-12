from base_ds.implementation import MaxStack


def max_stack_view() -> None:
    st = MaxStack()
    n = int(input())

    for _ in range(n):
        cmd = input().split()

        if cmd[0] == "push":
            st.push(int(cmd[1]))
        elif cmd[0] == "pop":
            st.pop()
        elif cmd[0] == "max":
            print(st.max())
