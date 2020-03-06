import pytest
from calculator import add

def test_add():
    assert(add("") == 0)
    assert(add("1") == 1)
    assert(add("1,1") == 2)

def test_multiple_add():
    assert(add("1,2,3,4") == 10)

def test_newline_add():
    assert(add("1\n2,3") == 6) 

def test_multiple_delim():
    assert(add("//;\n1;2") == 3)

def test_negatives_add():
    with pytest.raises(Exception) as error:
        assert add("-1,-2,3,4")
        str(error.value) == "-numbers not allowed! -1, -2."

def test_ignore_add():
     assert(add("2+1001") == 2)

def test_anylength_delim():
    assert(add("//***\n1***2***3") == 6)

def test_diffAnylength_delim():
    assert(add("//[:D][%]\n1:D2%3") == 6)
    assert(add("//[***][%%%]\n1***2%%%3") == 6)
    assert(add("//[(-_-')][%]\n1(-_-')2%3") == 6)

def test_moreChar_delim():
    assert(add("//[*][%]\n1*2%+???++@aqw^^^\\^3") == 6)
 

