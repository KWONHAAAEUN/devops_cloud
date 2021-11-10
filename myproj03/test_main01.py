import pytest
from main01 import get_word_count
from main02 import get_counts
from main03 import get_number


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("우리는 파이썬을 즐겨요", 3),
        ("python Family", 2),
    ],
)
def test_get_word_count(sentence, expected):
    assert get_word_count(sentence) == expected


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("우리는 파이썬을 즐겨요", 10),
        ("python Family", 12),
    ],
)
def test_get_counts(sentence, expected):
    assert get_counts(sentence) == expected


@pytest.mark.parametrize(
    "sentence,expected",
    [
        (1234567, 1234000),
        (1234, 1000),
    ],
)
def test_get_number(sentence, expected):
    assert get_number(sentence) == expected
