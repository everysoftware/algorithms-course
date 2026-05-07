from src.balanced_ds.bst.tree import BST

node_samples = [
    [],
    [(7, -1, -1)],
    [
        (4, 1, 2),
        (2, 3, 4),
        (6, 5, 6),
        (1, -1, -1),
        (3, -1, -1),
        (5, -1, -1),
        (7, -1, -1),
    ],
]


def get_bst_samples() -> list[BST[int, None]]:
    return [BST[int, None].from_array(sample) for sample in node_samples]


expected_dfs_inorder = zip(
    get_bst_samples(),
    [
        [],
        [7],
        [1, 2, 3, 4, 5, 6, 7],
    ],
    strict=False,
)

expected_dfs_preorder = zip(
    get_bst_samples(),
    [
        [],
        [7],
        [4, 2, 1, 3, 6, 5, 7],
    ],
    strict=False,
)

expected_dfs_postorder = zip(
    get_bst_samples(),
    [
        [],
        [7],
        [1, 3, 2, 5, 7, 6, 4],
    ],
    strict=False,
)
