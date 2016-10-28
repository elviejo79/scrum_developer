import sys
from python_lab import nextInts
from hypothesis import given
from hypothesis import strategies as st


def test_nextInts():
    assert nextInts([1, 5, 7]) == [2, 6, 8]
    assert nextInts([5, 24, 12]) == [6, 25, 13]


@given(st.lists(st.integers(min_value=(-1 * sys.maxint-1), max_value=sys.maxint-1)))
def test_properties_nextInts(L):
    processed = nextInts(L)

    assert isinstance(processed, list)
    assert (len(L)) == len(processed)
    for num in processed:
        assert isinstance(num, int)

    for src, prs in zip(L, processed):
        assert (src+1) == prs
