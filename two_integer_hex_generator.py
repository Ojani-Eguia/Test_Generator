'''
Test case hexadecimal generator
By Ojani Eguia

Geneates test cases for a given function, generating ranbom
hex values and computing the answer, displaying them in hex.

Currently only handles funciton with two integer input inputs.

Input: function_to_test, Function that will have test cases generated for
Input: digits, the number of digits that each generated input (and output) has
Input: number_of_tests, the number of test cases that will be generated
'''
#Imports
from fractions import gcd
from random import randint

def generate_tests(function_to_test, digits, number_of_tests):
    k = 0 #number of test cases that have been generated
    finished_results = []
    #set range for number to be generated
    hex_range = pow(16, digits) - 1
    #Generate results
    while k < number_of_tests:
        a = randint(0, hex_range)
        b = randint(0, hex_range)
        c = int(function_to_test(a, b))#Ensure result is an int
        finished_results = finished_results + [[str(hex(a))[2:], str(hex(b))[2:], str(hex(c))[2:]]]
        k = k+1
    #Print test cases using helper function
    print_tests(finished_results, digits)


#Helper function: Concatenates generated tests into single lines
#Adds digit fill as necessary, using rjust
def print_tests(test_suite, digit_fill):
    for test in test_suite:
        line_to_print = ''
        for number in test:
            line_to_print = line_to_print + '0x' + number.rjust(digit_fill, '0') + ' '
        print (line_to_print)
