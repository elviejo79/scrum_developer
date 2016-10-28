from python_lab import first_zero_sum_list
from hypothesis import given, assume
from hypothesis import strategies as st


def test_first_zero_sum_list():
    assert first_zero_sum_list([-4, -2, 1, 2, 5, 0]) == [(-4, 2, 2)]

@given(st.lists(st.integers()))
def test_first_zero_sum_list_hypothesis(list):
    assume (len(list) >= 3)
    lenght = len(first_zero_sum_list(list))
    assert lenght == 3
    assert (sum(first_zero_sum_list(list)) == 0)


# We restrict the range of values we test against here because if you were to
# e.g. attempt to decode [[0, 2 ** 64]] then it would try to create a list of
# 2 ** 64 elements and that would be bad. So in this test we only try decoding
# serialized lists with the second element being from 0 to 10 inclusive.
# @given(st.lists(st.tuples(st.integers(), st.integers(0, 10))))
# def test_decoding_never_crashes_with_small_sizes(ls):
#    run_length_decode(ls)
