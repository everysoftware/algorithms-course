from typing import Callable

import art


def menu_factory(topic: str, tasks: list[tuple[str, Callable[[], None]]]):
    def menu():
        print(art.text2art(topic))

        for i, option in enumerate(tasks):
            print(f"#{i + 1}. {option[0]}")
        print()

        option_number = int(input("Enter the number of the task: "))

        if 1 <= option_number <= len(tasks):
            tasks[option_number - 1][1]()
        else:
            print("Unknown task. Exiting...")

    return menu
