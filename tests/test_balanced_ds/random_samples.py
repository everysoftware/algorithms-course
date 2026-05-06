import random
import string
from typing import Any, TypeVar

from src.balanced_ds.avl.tree import AVLTree
from src.balanced_ds.bst.tree import BST
from src.balanced_ds.rope import Rope
from src.balanced_ds.segment_tree import IntSegmentTree

T = TypeVar("T", bound=BST[Any, Any])


def generate_bst(size: int, tree_type: type[T]) -> T:
    keys = [random.randint(1, 100) for _ in range(size)]

    return tree_type.from_keys(keys).check_correctness()


key_number = random.randint(10, 20)
tree_number = 5

keys_samples = [[random.randint(1, 100) for _ in range(key_number)] for _ in range(tree_number)]


def get_random_bst_samples() -> list[BST[int, None]]:
    return [generate_bst(key_number, BST[int, None]) for _ in range(tree_number)]


def get_random_avl_samples() -> list[AVLTree[int, None]]:
    return [generate_bst(key_number, AVLTree[int, None]) for _ in range(tree_number)]


def get_random_segment_tree_samples() -> list[IntSegmentTree]:
    return [generate_bst(key_number, IntSegmentTree) for _ in range(tree_number)]


def get_random_rope_samples() -> list[Rope]:
    return [Rope.from_string("".join(random.choices(string.ascii_lowercase, k=key_number))) for _ in range(tree_number)]
