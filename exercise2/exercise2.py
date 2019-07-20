import sys
import json
import datetime
import random
from functools import reduce

def format_filename():
    current_time = datetime.datetime.now()
    return ""+str(current_time.year)+"-"+str(current_time.month)+"-"+str(current_time.day)+"_"+str(current_time.hour)+"-"+str(current_time.minute)+"-"+str(current_time.second)

def write_to_JSON(data):
    file_name = "{}.json".format(format_filename())
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)
    print("The content was saved to a file called: {}\n".format(file_name))

def multiplication(numbers):
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

    for number in numbers:
        multi = int(number) * multi

    multiplication_data["Multiplication"] = multi
    print("Printing your JSON below:")
    print(json.dumps(multiplication_data, indent=4, sort_keys=True))
    write_to_JSON(multiplication_data)

def subtract(num):
    return int(num) - int(num)

def subtraction(numbers):
    sub = map(subtract, numbers)
    return sub

def ramdon_number(numbers):
    index = random.randint(0,(len(numbers)-1))
    print("Picking a random number from the list of your numbers. And the chosen one is: {}".format(numbers[index]))

def merge_sort(numbers):
    if len(numbers) > 1:
        middle = len(numbers) // 2  # divide array length in half and use the "//" operator to *floor* the result

        left_numbers = numbers[:middle]  # fill in left array
        right_numbers = numbers[middle:]  # fill in right array

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

def merge_sort_reversed(numbers):
    if len(numbers) > 1:
        middle = len(numbers) // 2  # divide array length in half and use the "//" operator to *floor* the result

        left_numbers = numbers[:middle]  # fill in left array
        right_numbers = numbers[middle:]  # fill in right array

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

def sorted_low_to_high(numbers):
    merge_sort(numbers)
    print(numbers)

def sorted_reverse(numbers):
    print(sorted(numbers,reverse=True))

def menu(numbers):
    numbers_selected = "The numbers you've selected are: {}".format(numbers)
    options = """
    
    1 - Multiply, show result and write to JSON file
    2 - Subtract
    3 - Show random number
    4 - Show sorted list (from lower to highest)
    5 - Show reverse sorted list (from highest to lower)\n"""
    while True:
        print(numbers_selected, options)
        chosen = input("Please, select one:")
        if chosen =='1': 
            multiplication(numbers)
        elif chosen == '2': 
            map(lambda x: print(x), numbers)
            print("\n")
        elif chosen == '3':
            ramdon_number(numbers)
        elif chosen == '4': 
            sorted_low_to_high(numbers)
        elif chosen == '5': 
            sorted_reverse(numbers)
        else: 
            print("Unknown Option Selected!")

if __name__ == "__main__":
    try:
        if (len(sys.argv) < 7):
            raise Exception("Arguments must have at least 6 numbers")
        if (len(sys.argv) > 7):
            raise Exception("Arguments can't be longer than 6 numbers")
    except Exception as e:
        print(e)
    else:
        menu(sys.argv[1:7])