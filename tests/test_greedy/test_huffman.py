import pytest

from greedy import (
    huffman_tree,
    huffman_encode,
    is_prefix_code,
    huffman_decode,
)


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
def test_is_prefix_code(tree: dict[str, str], expected: bool):
    assert is_prefix_code(tree) == expected


@pytest.mark.parametrize(
    "string",
    ["a", "ab", "abc", "aabbcc", "aabbccdd", "aabbccddeeff", "hello world"],
)
def test_huffman_tree(string: str):
    tree = huffman_tree(string)
    assert is_prefix_code(tree)


@pytest.mark.parametrize(
    "string", ["a", "ab", "abc", "aabbcc", "aabbccdd", "aabbccddeeff", "hello world"]
)
def test_huffman_encode_decode(string: str):
    tree = huffman_tree(string)
    encoded = huffman_encode(string, tree)

    assert len(encoded) <= 8 * len(string)
    assert all(char in "01" for char in encoded)

    decode_tree = {v: k for k, v in tree.items()}
    assert huffman_decode(encoded, decode_tree) == string
