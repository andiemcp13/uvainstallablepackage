import sys
sys.path.append('.')
import shared as sh
import pytest
xfail = pytest.mark.xfail

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_spacecopress_string():

    test_string = "This is     a    string"

    assert "This is a string" == sh.space_compress(test_string), "String <{}> not cleaned as expected".format(test_string)

@xfail
def test_spacecopress_string_fail():
    
    test_string = 0
    
    assert "This is a string" == sh.space_compress(test_string), "String <{}> not cleaned as expected".format(test_string)

@pytest.mark.skip(reason="No way of currently testing this")
def test_the_unknown():
    print("test unknown")



@pytest.mark.skipif(sys.platform == "windows", reason="Test does not run on my platform")
def test_onlyplatform():

    print(sys.platform)
    test_value = 2 
    assert 2 == test_value, "Wrong value"
