import art

from src.balanced_ds.views.is_bst import task_is_bst, task_is_general_bst
from src.balanced_ds.views.rope import task_rope
from src.balanced_ds.views.segment_tree import task_segment_tree
from src.balanced_ds.views.traversal import task_traversal

tasks = [
    ("Traversal", task_traversal),
    ("BST property check", task_is_bst),
    ("General BST property check", task_is_general_bst),
    ("Segment tree", task_segment_tree),
    ("Rope", task_rope),
]


def menu() -> None:
    print(art.text2art("Search Trees"))
    print("Tasks:")

    for i, option in enumerate(tasks):
        print(f"#{i + 1}. {option[0]}")

    option_number = int(input("Enter task number: "))

    if 1 <= option_number <= len(tasks):
        print("Enter the task data: ")
        tasks[option_number - 1][1]()
    else:
        print("Unknown option")
