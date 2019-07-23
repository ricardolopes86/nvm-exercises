# NVM Exercises

## Exercise 1:
Using AWS: 
1. Automate the creation of two Linux instances with MySQL;
2. Configure MySQL with one master and one slave with replication enabled between these two databases;
3. Create a data structure of your choice capturing name, address, phone number;
4. Create a script to insert 1000 entries of data into the DB;
5. Create a script which performs monitoring. Insert a record into the master and monitor on the slave. Alert if there is a replication deplay of more than 1s.

## Exercise 2:
Write a program in Python (or any other language) based on the following requirements:  

First, program must accept 6 consecutive numbers from command line arguments (each number is one argument).  
Second, program must present to the user the simple choice menu in standard output and operate accordingly in the background with the numbers the user entered previously:
* Perform subtraction and show output on screen comma separated;
* Perform multiplication and store result in a JSON file (i.e.  
```json
    {
      "InputNumber1": "x",
      "InputNumber2": "y",
      "InputNumber3": "a",
      "InputNumber4": "b",
      "InputNumber5": "c",
      "InputNumber6": "d",
      "Multiplication": "X"
    }
```
where: `x`, `y`, `a`, `b`, `c` and `d` are user line arguments and `X` is the multiplication result.)

* Pick randomly a numbers and show it on the screen;
* Print sorted (highest to lowest) array/list of numbers;
* Print sorted (lowest to highest) array/list of numbers.

Keep in mind that the program must respond appropriately upon possible human-errors. Also, the above choice menu must run forever on a loop until the user kills the program through SIGINIT or CTRL+C.

# How to Use

## Pre-requisites

## Step-by-step