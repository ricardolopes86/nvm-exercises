import sys
import json
import datetime
from functools import reduce

def format_filename():
    current_time = datetime.datetime.now()
    return ""+str(current_time.year)+"-"+str(current_time.month)+"-"+str(current_time.day)+"_"+str(current_time.hour)+"-"+str(current_time.minute)+"-"+str(current_time.second)

def write_to_JSON(data):
    with open("{}.json".format(format_filename()), "w") as json_file:
        json.dump(data, json_file)

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
    write_to_JSON(multiplication_data)

def subtraction(numbers):
    return reduce(lambda x,y: x-y, numbers)

def ramdon_number(numbers):
    pass
def sorted_low_to_high(numbers):
    pass
def sorted_reverse(numbers):
    pass

def menu(numbers):
    print("The numbers you've selected are: {}".format(numbers))
    print("""
    1 - Multiply, show result and write to JSON file
    2 - Subtract, show result and write to JSON file
    3 - Show random number
    4 - Show sorted list (from lower to highest)
    5 - Show reverse sorted list (from highest to lower)""")
    chosen = raw_input("Please, select one:")
    if chosen =='1': 
        print "add" 
    elif chosen == '2': 
        print(subtraction(numbers))
    elif chosen == '3':
        print "find" 
    elif chosen == '4': 
        print("Show")
    elif chosen == '5': 
        print ("Show")
    else: 
        print "Unknown Option Selected!" 

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