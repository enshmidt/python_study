import pytest
from Lecture_04.Lecture_4_Testing_homework.continued_fraction_task import (
    continued_fraction,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [([239, 30], [7, 1, 29]), ([449, 15], [29, 1, 14]), ([-5, 0], []), ([5, -1], [-5])],
)
def test_continued_fraction(test_input, expected):
    assert continued_fraction(*test_input) == expected
