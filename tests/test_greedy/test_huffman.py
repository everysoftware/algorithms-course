import pytest

from src.j_greedy.huffman import (
    huffman_decode,
    huffman_encode,
    huffman_tree,
)


# O(n)
def is_prefix_code(tree: dict[str, str]) -> bool:
    codes = list(tree.values())
    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            # Если один код является префиксом другого, то это не префиксный код.
            if codes[i].startswith(codes[j]) or codes[j].startswith(codes[i]):
                return False
    return True


@pytest.mark.parametrize(
    "tree, expected",
    [
        ({"a": "0"}, True),
        ({"a": "0", "b": "1"}, True),
        ({"a": "00", "b": "01", "c": "1"}, True),
        ({"a": "00", "b": "01", "c": "10", "d": "11"}, True),
        ({"a": "000", "b": "001", "c": "01", "d": "10", "e": "11"}, True),
        ({"a": "00", "b": "00"}, False),  # 'a' и 'b' имеют одинаковые коды.
        ({"a": "0", "b": "01"}, False),  # 'a' является префиксом 'b'.
    ],
)
def test_is_prefix_code(tree: dict[str, str], expected: bool) -> None:
    assert is_prefix_code(tree) == expected


@pytest.mark.parametrize(
    "string",
    ["a", "ab", "abc", "aabbcc", "aabbccdd", "aabbccddeeff", "hello world", "aaaaaabbcccddddeeeee"],
)
def test_huffman_tree(string: str) -> None:
    tree = huffman_tree(string)
    assert is_prefix_code(tree)


@pytest.mark.parametrize(
    "string",
    ["a", "ab", "abc", "aabbcc", "aabbccdd", "aabbccddeeff", "hello world", "aaaaaabbcccddddeeeee"],
)
def test_huffman_encode_decode(string: str) -> None:
    encoded, tree = huffman_encode(string)

    assert len(encoded) <= 8 * len(string)
    assert all(char in "01" for char in encoded)

    decode_tree = {v: k for k, v in tree.items()}
    assert huffman_decode(encoded, decode_tree) == string
