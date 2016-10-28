from python_lab import predict_expresion
from hypothesis import given
from hypothesis import strategies as st

def test_predict_expresion():
    assert predict_expresion(2,4,5);

@given(st.integers())
def test_predict_expresion2(x,y,z):
    assert (predict_expresion(x,y,z)%10080) --1