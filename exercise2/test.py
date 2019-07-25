"""
This script will run all tests for our functions exercise2.py
"""
import pytest
import os
from exercise2 import subtract

@pytest.mark.parametrize("numbers_list", [(12, 122, 13, 4, 554, 96)])
def test_multiplication(numbers_list):
    """
    Unit test to assert result of multiplication
    """
    multi = 1
    for number in numbers_list:
        multi = int(number) * multi
    assert multi == 4048791552

@pytest.mark.parametrize("numbers_list", [(12, 122, 13, 4, 554, 96)])
def test_subtraction(numbers_list):
    """
    Unit test to assert result of subtracting all numbers in the list
    """
    assert subtract(numbers_list) == -777

@pytest.mark.parametrize("numbers_list", [(12, 122, 13, 4, 554, 96)])
def test_sorted_high_to_low(numbers_list):
    """
    Unit test to assert sorting from lower to higher
    """
    assert sorted(numbers_list) == [4, 12, 13, 96, 122, 554]

@pytest.mark.parametrize("numbers_list", [(12, 122, 13, 4, 554, 96)])
def test_sorted_low_to_high(numbers_list):
    """
    Unit test to assert sorting from higher to lower
    """
    assert sorted(numbers_list, reverse=True) == [554, 122, 96, 13, 12, 4]

if __name__ == "__main__":
    if not os.path.exists("test"):
        try:
            print("\033[1;33;40mCreating test directory...\033[0m")
            os.mkdir("test/")
        except Exception as error:
            raise Exception("Error creating build directory at: {}".format(buil_dir))
            print("\033[1;35;40mError creating dir: {}\033[0m".format(error))
    print("\033[1;32;40mRunning tests...\033[0m")
    pytest.main(["-v", "test.py", "--junitxml=test/results.xml"])
