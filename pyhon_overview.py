import io
from random import shuffle
from random import randint
from pprint import pprint  # pretty print

# A module is any .py file
# A package is a collection (directory) of (related) modules which also contains an _init__.py file (can be empty)
# A library is a collection of (related) packages
# (A framework is a collection of (kind of related) libraries to help build an app)
# from path-to-the-python-file import function-or-variable-from-that-file
from module1 import module1
from my_packages.module2 import module2
from my_packages.module3 import module3
from my_packages.sub_packages.module4 import module4
from my_packages.sub_packages.module5 import module5

import unittest
from create_titles import create_titles

# Iterables
# An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
# Sequential iterables: lists, tuples, and strings
# Non-sequential iterables: dictionaries and sets

# simple bank account class
class Account:
    def __init__(self) -> None:
        self._owner = ""
        self._balance = 0.0

    def __init__(self, o: str, b: float) -> None:
        self._owner= o
        self._balance = b

    def __str__(self) -> str:
        return f"name is {self._owner}, balance is {self._balance}"

    def deposit(self, d: float) -> None:
        self._balance += d
        print(f"{d} deposited, new balance is {self._balance}")

    def withdraw(self, w: float) -> None:
        self._balance -= w
        print(f"{w} withdrawn, new balance is {self._balance}")

# create class that inherits from unittest.TestCase
class MyUnitTests(unittest.TestCase):
    # we normally number the tests that are going to be called
    def test1(self):
        test_data = "the frog prince"
        expected_result = "The Frog Prince"
        result = create_titles(test_data)
        self.assertEqual(result, expected_result)

    def test2(self):
        test_data = "humpty dumpty sat on the wall"
        expected_result = "Humpty Dumpty Sat On The Wall"
        result = create_titles(test_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    """ will end program if y=unit test run
    print("\n---unit testing")
    unittest.main()
    """

    """ don't want to ask for user input all the time
    print("\n---try except")
    while True:
        try:
            val = int(input("Input an integer: "))
        except ValueError:
            # raise TypeError("please input an int")
            print("please input an int")
        else:
            print(f"integer {val} accepted")
            break
        finally:
            print("I always get printed")
    """

    print("\n---oop")
    joe = Account("joe", 101.11)
    print(joe)
    joe.deposit(10)
    print(joe)
    joe.withdraw(50)
    print(joe)

    print("\n---modules, packages and libs")
    module1() 
    module2()
    module3()
    module4()
    module5()

    print("\n---logical operators: and, or, not")
    print(f"True and False = {True and False}")
    print(f"True or False = {True or False}")
    print(f"True and not False = {True and not False}")

    print("\n---string literal")
    my_money = 50
    my_spend = 15 * 1.03
    print(f"I have ${my_money-my_spend} left")
    
    ls_test_1 = [2,3,4,5,6,7] 

    # loops
    print("\n---for loop")
    for item in ls_test_1:
        print(f"{item}")
    print("\n---for loop with enumerate")
    for idx, item in enumerate(ls_test_1):
        print(f"{idx}: {item}")
    ls_long_1 = []
    print("\n---for loop with range")
    for i in range(0, 50):
        # print(f"{i}", end=" ")
        ls_long_1.append(i)
    
    # printing with unpacking
    print(
        *ls_long_1, sep=" ", end="\n"
    )  # astrix unpacks the list iterable into a new list iterable without formatting
    print("\n---unpacking a list into specific variables then the remaining into *rest")
    first, second, *rest = ls_long_1 # unpacking into variables and a list iterable
    print(f"first={first}, second={second}, rest={rest}")
    
    print("\n---tuple unpacking")
    list_of_tups_1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for idx, (x, y) in enumerate(list_of_tups_1):
        print(f"{idx}: {x} {y}")
    
    print("\n---tuple packing via zip (opposite of enumerate)")
    tuple_1 = (1, 2, 3, 4, 5, 6)
    tuple_2 = (11, 12, 13, 14, 15, 16, 17, 18)
    print(list(zip(tuple_1, tuple_2)))
    
    print("\n---reference and value copying")
    ls_test_1 = [100, 90, 102, 103, 104, 105]
    ls_test_1_ref = ls_test_1 # not a copy, ls_test_1_ref points to the same list iterable
    ls_test_1.sort()
    print(f"ls_test_1 = {ls_test_1}") # same
    print(f"ls_test_1_ref = {ls_test_1_ref}") # same
    ls_test_1_new_copy = ls_test_1[:] # makes a new list iterable that is a copy via slicing
    ls_test_1 = [x**2 for x in ls_test_1] # list comprehension
    print(f"ls_test_1 = {ls_test_1}") # different
    print(f"ls_test_1_new_copy= {ls_test_1_new_copy}") # different
        
    ls_test_1 = [2,3,4,5,6,7] 

    # .pop, ".shift", ".push", ".unshift",.remove, shuffle, (randint), .join, .split, [slices], (reducing, sum, len, min, max, all, any), .sort, sorted

    # pop(), pop(0), insert(val, len(arr)-1), insert(val, 0)
    print("\n---pop, push, shift, unshift (remove or add by index position)")
    print(f"ls_test_1 = {ls_test_1}")
    ls_test_1.pop()  # "pop" off the end
    print("about to pop off end...")
    for idx, item in enumerate(ls_test_1):
        print(f"{idx}: {item}")
    print("about to shift off of start...like perl reading function's arguments...")
    ls_test_1.pop(0) # "shift" off the start
    for idx, item in enumerate(ls_test_1):
        print(f"{idx}: {item}")
    print("about to push onto the end...")
    ls_test_1.insert(11, len(ls_test_1)-1) # "push" onto the end
    print(f"ls_tests_1 = {ls_test_1}")
    print("about to unshift onto the start...")
    ls_test_1.insert(11, 0) # "unshift" onto the start
    print(f"ls_tests_1 = {ls_test_1}")

    # remove by value
    print("\n---remove(), remove by value in list iterable")
    ls_test_1.remove(5)  # remove a value from the list iterable
    for idx, item in enumerate(ls_test_1):
        print(f"{idx}: {item}")

    # random 
    print("\n---shuffle, in place")
    shuffle(ls_long_1)
    print((ls_long_1))
    rand_int = randint(1,100) 
    print(f"rand_int={rand_int}")

    # join and split
    print("\n---join and split")
    the_str1 = "this is a test string"
    the_str2 = "".join(the_str1.split(" ")) # get rid of white space with join and spilt
    print(f"the_str1 = {the_str1}")
    print(f"the_str2 = {the_str2}")
    
    # slices (slice iterables and make copies of iterables)
    print("\n---slices")
    ls_test_1 = [100, 90, 102, 103, 104, 105]
    print(ls_test_1[:2])
    print(ls_test_1[:3])
    print(ls_test_1[::])  # print all of the list iterable
    print(ls_test_1[::-1])  # reverse the list iterable
    print(ls_test_1[-1])  # last item
    print(ls_test_1[0])
    print(ls_test_1[-6])  # 0 and -6 equivalent in a list iterable with 6 items
    
    # Guido wanted to remove map, filter, reduce and lambda from python 3!
    print("\n---pythonic 'reducing' functions")
    ls_test_1 = [12,4,15,6,7]
    the_sum1 = sum(ls_test_1)
    print(f"the_sum1 = {the_sum1}")
    the_len1 = len(ls_test_1)
    print(f"the_len1 = {the_len1}")
    the_min1 = min(ls_test_1)
    the_max1 = max(ls_test_1)
    print(f"the_min1 = {the_min1}, the_max1 = {the_max1}")
    # truthy test with all(), all must be true to return true
    print(f"all(ls_test_1) = {all(ls_test_1)}")
    # truthy test with any(), any true returns true
    print(f"any(ls_test_1) = {any(ls_test_1)}")
    
    # sorting
    ls_test_1.sort() # "sort()" in place ("sorted()" for immutable sorting)
    print(f"ls_test_1 = {ls_test_1}")
