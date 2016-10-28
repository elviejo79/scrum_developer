from python_lab import minutes_in_weeks
from hypothesis import given
from hypothesis import strategies as st


def test_minutest_in_weeks():
    assert minutes_in_weeks(1) == 10080
    assert minutes_in_weeks(2) == 20160

@given(st.integers())
def test_minutest_in_weeks(mins):
    assert (minutes_in_weeks(1)%10080) == 0


# We restrict the range of values we test against here because if you were to
# e.g. attempt to decode [[0, 2 ** 64]] then it would try to create a list of
# 2 ** 64 elements and that would be bad. So in this test we only try decoding
# serialized lists with the second element being from 0 to 10 inclusive.
# @given(st.lists(st.tuples(st.integers(), st.integers(0, 10))))
# def test_decoding_never_crashes_with_small_sizes(ls):
#    run_length_decode(ls)
