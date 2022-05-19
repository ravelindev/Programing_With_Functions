"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Smith") == "Smith; John"
    assert make_full_name("J", "SJ") == "SJ; J"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    """Verify that the extract_family_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("SJ; J") == "SJ"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    """Verify that the extract_given_name
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Smith; John") == "John"
    assert extract_given_name("SJ; J") == "J"
    #assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])