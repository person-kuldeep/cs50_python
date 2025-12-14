import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError): # if test passes, ZeroDivisionError is raised 
        divide(1, 8)


