from python_lab import cartesian_product
from hypothesis import given
from hypothesis import strategies as st

def test_cartesian_product():
    result = cartesian_product(Xs=['A','B','C'], Ys=[1,2,4])
    if result == [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 5], ['C', 3]]:
        assert result
        
@given(Xs=st.lists(elements=st.characters(), min_size=3, max_size=3), Ys=st.lists(elements=st.integers(), min_size=3,max_size=3))
def test_cartesian_product_dinamic(Xs, Ys):
    assert isinstance(cartesian_product(Xs=Xs, Ys=Ys), list)