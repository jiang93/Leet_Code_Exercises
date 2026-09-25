import pytest 

# Test case for an expected division by zero exception 
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    # print(e.value)
    assert "division by zero" in str(e.value)

# Test the same logic/ function with different inputs and expected outputs
test_values = [(2, 3, 6), (1, 99, 99), (0, 10, 0), (-3, 5, -15), (-1, -9, 9)]

@pytest.mark.math
@pytest.mark.parametrize("a, b, result", test_values)
def test_multiplication(a, b, result):
    assert a * b == result

