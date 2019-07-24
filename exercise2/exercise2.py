"""
Playing with numbers.
This awesome program will perform some operations to a list of numbers.
You should input *exactly* 6 numbers right after the command.
"""
import sys
import json
import datetime
import random
from functools import reduce
import operator
import pytest

def format_filename():
    """
    Just a simple method to format the filename for the JSON file that will be generated. It's based on the current date and time.
    """
    current_time = datetime.datetime.now()
    return ""+str(current_time.year)+"-"+str(current_time.month)+"-"+str(current_time.day)+"_"+str(current_time.hour)+"-"+str(current_time.minute)+"-"+str(current_time.second)

def write_to_json(data):
    """
    The method to write the JSON generated in the multiplication method.
    """
    file_name = "{}.json".format(format_filename())
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)
    print("The content was saved to a file called: {}\n".format(file_name))

@pytest.mark.parametrize("numbers_list",[(12,122,13,4,554,96)])
def test_multiplication(numbers_list):
    """
    Unit test to assert result of multiplication
    """
    multi = 1
    for number in numbers_list:
        multi = int(number) * multi
    assert multi == 4048791552

def multiplication(numbers_list):
    """
    Multiply the numbers in the array/list. Print them as JSON and write it to a file.
    """
    multi = 1
    multiplication_data = {
        "InputNumber1": numbers[0],
        "InputNumber2": numbers[1],
        "InputNumber3": numbers[2],
        "InputNumber4": numbers[3],
        "InputNumber5": numbers[4],
        "InputNumber6": numbers[5],
        "Multiplication": multi
    }

    for number in numbers_list:
        multi = int(number) * multi

    multiplication_data["Multiplication"] = multi
    print("Printing your JSON below:")
    print(json.dumps(multiplication_data, indent=4, sort_keys=True))
    write_to_json(multiplication_data)

@pytest.mark.parametrize("numbers_list",[(12,122,13,4,554,96)])
def test_subtraction(numbers_list):
    """
    Unit test to assert result of subtracting all numbers in the list
    """
    assert subtract(numbers_list) == -777

def subtract(num):
    """
    Will return the result of subtracting all the numbers in the array/list.
    """
    numbers_diff = reduce(operator.sub, num)
    return numbers_diff

def ramdon_number(numbers_list):
    """
    Pick a random number using the random module and the length of the array.
    """
    index = random.randint(0, (len(numbers_list)-1))
    print("Picking a random number from the list of your numbers. And the chosen one is: {}".format(numbers[index]))

def merge_sort(numbers_list):
    """
    Classic merge sort algorithm to sort an array/list.
    """
    if len(numbers_list) > 1:
        middle = len(numbers_list) // 2  # divide array length in half and use the "//" operator to *floor* the result

        left_numbers = numbers_list[:middle]  # fill in left array
        right_numbers = numbers_list[middle:]  # fill in right array

        merge_sort(left_numbers)  # Sorting the first half
        merge_sort(right_numbers)  # Sorting the second half

        left_index = 0
        right_index = 0
        current_index = 0

        # compare each index of the subnumberss adding the lowest value to the current_index
        while left_index < len(left_numbers) and right_index < len(right_numbers):
            if left_numbers[left_index] < right_numbers[right_index]:
                numbers[current_index] = left_numbers[left_index]
                left_index += 1
            else:
                numbers[current_index] = right_numbers[right_index]
                right_index += 1
            current_index += 1

        # copy remaining elements of left_numbers[] if any
        while left_index < len(left_numbers):
            numbers[current_index] = left_numbers[left_index]
            left_index += 1
            current_index += 1

        # copy remaining elements of right_numbers[] if any
        while right_index < len(right_numbers):
            numbers[current_index] = right_numbers[right_index]
            right_index += 1
            current_index += 1

@pytest.mark.parametrize("numbers_list",[(12,122,13,4,554,96)])
def test_sorted_high_to_low(numbers_list):
    """
    Unit test to assert sorting from lower to higher 
    """
    assert merge_sort(numbers_list) == [4,12,13,96,122,554]

def sorted_low_to_high(numbers_list):
    """
    Call a merge sort function to sort the list/array
    """
    merge_sort(numbers_list)
    print(numbers_list)

@pytest.mark.parametrize("numbers_list",[(12,122,13,4,554,96)])
def test_sorted_low_to_high(numbers_list):
    """
    Unit test to assert sorting from higher to lower 
    """
    assert sorted(numbers_list, reverse=True) == [554,122,96,13,12,4]

def sorted_reverse(numbers_list):
    """
    Using embedded sorted() function to reverse the array.
    """
    print(sorted(numbers_list, reverse=True))

def menu(numbers_list):
    """
    Shows menu after successfully validate the inputs
    """
    numbers_selected = "The numbers you've selected are: {}".format(numbers_list)
    options = """
    
    1 - Multiply, show result and write to JSON file
    2 - Subtract
    3 - Show random number
    4 - Show sorted list (from lower to highest)
    5 - Show reverse sorted list (from highest to lower)\n"""
    while True:
        print(numbers_selected, options)
        chosen = input("Please, select one:")
        if chosen == '1':
            multiplication(numbers_list)
        elif chosen == '2':
            result = subtract(numbers_list)
            print("The subtraction value is: {}".format(result))
        elif chosen == '3':
            ramdon_number(numbers_list)
        elif chosen == '4':
            sorted_low_to_high(numbers_list)
        elif chosen == '5':
            sorted_reverse(numbers_list)
        else:
            print("Unknown Option Selected!")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 7:
            raise Exception("Arguments must have at least 6 numbers")
        if len(sys.argv) > 7:
            raise Exception("Arguments can't be longer than 6 numbers")
    except Exception as error:
        print(error)
    else:
        numbers = []
        for x in range(len(sys.argv[1:7])):
            numbers.append(int(sys.argv[x+1]))
        menu(numbers)