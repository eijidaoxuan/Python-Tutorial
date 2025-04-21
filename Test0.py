from .Test import square
import pytest

def test_positive():
    assert square(10) == 100
    assert square(5) == 25

def test_zero():
    assert square(0) == 0  

def test_negative():
    assert square(-10) == 100
    assert square(-5) == 25

def test_combined():            #Test for all numbers from -100 to 100
    for _ in range(-100, 101):  
        assert square(_) == _ * _

def test_decimal():
    assert square(2.5) == 6.25
    assert square(-2.5) == 6.25
    assert square(0.05) == pytest.approx(0.002, abs=1e-3)      #True=0.0025     abs = tolerance different(0,05 or 1e-3 = 1*10^(-3) = 0,001)

def test_string():
    with pytest.raises(TypeError):
        square("something")
        square("123")
