import pytest 

"""
# Test case for an expected division by zero exception 
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    # print(e.value)
    assert "division by zero" in str(e.value)
"""
"""
# Test the same logic/ function with different inputs and expected outputs
test_values = [(2, 3, 6), (1, 99, 99), (0, 10, 0), (-3, 5, -15), (-1, -9, 9)]
@pytest.mark.parametrize("a, b, result", test_values)
def test_multiplication(a, b, result):
    assert a * b == result
"""

# python module => a .py file containing python code
"""
    import module_name
    module_name.function_name()
"""
"""
    from module_name import function_name
    function_name()
"""

# package => a directory that groups related modules 
# my_package/
# ├── __init__.py (from . import module_name, from .module_one import function_name, empty)
# ├── module_one.py
# └── module_two.py
"""
    # only if the module_name is imported inside the dunder init.py file
    import my_package
    my_package.module_name.function_name()
"""
""" 
    # only if the function_name is imported inside the dunder init.py file
    import my_package
    my_package.function_name()
"""
"""
    import my_package.module_name
    my_package.module_name.function_name()
"""
"""
    from my_package import module_name
    module_name.function_name()
"""
"""
    from my_package.module_name import function_name
    function_name()
"""

# unit test classes

# pytest writes test cases as functions instead of class. naming convention for test module and function starts with test_ prefix. 
# this naming convetion can be changed in the configuration.
# test case with exceptions => pytest.raises 
# parameterization(unique input for same test case and unique expected outputs) => @pytest.mark.parametrize("test function parameter names", test value)