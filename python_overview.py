import math
import operator as op
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

# *Unpacking (...spread and ...rest)
# Python's *unpacking is the same as JavaScript's ...spread and ...rest operators
# JS ...rest put the remaining (rest of) values into an array
# JS ...spread expands an iterable into individual elements
# Python *rest: first, second, *rest = long_list # first 2 items from list put into "first" and "second" vars and the remaining items are put into a list called "rest"
# Python *spread: lst=[1,2,3]; new_list=[*lst, 4, 5]; print(new_list) # 1,2,3,4,5; lst was unpacked (...spread) into its individual items


# Strings, numbers (ints and floats) and tuples are immutable. Give performance optimisation, thread safety, memory efficiency, easier debugging, etc

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

    # file IO
    fh1 = open("test_file.txt", "w")
    fh1.write("original style 1\noriginal style 2")
    fh1.close()
    # "with" and "as" doesn't require the file handle to be closed
    my_text_list = ["with as line 1", "with as line 2", "with as line 3"]
    with open("test_file_with_as.txt", "w") as fh_2:
        fh_2.writelines(s+"\n" for s in my_text_list) # need to explicitly add newlines to writelines

    # OOP
    print("\n---oop")
    joe = Account("joe", 101.11)
    print(joe)
    joe.deposit(10)
    print(joe)
    joe.withdraw(50)
    print(joe)

    # modules and packages
    print("\n---modules, packages and libs")
    module1() 
    module2()
    module3()
    module4()
    module5()

    # logical operators
    print("\n---logical operators: and, or, not")
    print(f"True and False = {True and False}")
    print(f"True or False = {True or False}")
    print(f"True and not False = {True and not False}")

    # maths functions
    # abs()
    # round()
    # ceil()
    # floor()
    # randint
    print(f"abs(-4.55) = {abs(-4.55)}")
    print(f"round(-4.55) = {round(-4.55)}")
    print(f"math.ceil(-4.55) = {math.ceil(-4.55)}") # import math 
    print(f"math.floor(-4.55) = {math.floor(-4.55)}")
    rand_int = randint(1,100) # import randint
    print(f"rand_int={rand_int}")

    # strings (and formated string literals, f-strings)
    # concat with +, f-string, .join
    # slicing with slice[:], f-strings, list()
    # case: .upper(), .lower(), .title()
    # replace all characters in a string with .replace(), or certain number of chars with replace(num)
    # check if it contains with operator.contains(), need to import operator
    # evaluate expression in string with eval()
    # trim leading/trailing whitespace via .split(), or remove all .,89 trailing/leading characters with .split(".,89")
    print("\n---formated string literals")
    my_money = 50
    my_spend = 15 * 1.03
    print(f"I have ${my_money-my_spend} left")
    # string concatenation
    print("\n---string concatenation")
    my_str1 = "hello"
    my_str1 += " world"
    print(f"my_str1 = {my_str1}")
    my_str2 = "starship"
    my_str3 = "enterprise"
    my_str4 = " ".join([my_str2, my_str3])
    print(f"my_str4 = {my_str4}")
    my_str5, my_str6, my_str7 = "Joe", "Danger", "Bloggs"
    my_str8 = f"{my_str5}-{my_str6}-{my_str7}"
    print(f"my_str8 = {my_str8}")
    # substring via slicing
    print(f"my_str2[:4] = {my_str2[0:4]}") # string index 0,1,2 and 3 grabbed
    # strings are immutable, use (1) slice & reassemble, (2) f-stings or (3) type conversion to deal with this
    # (1), title capitalises the first letter of each work like a book title
    my_str9 = my_str3[:].title()
    print(f"my_str9 = {my_str9}")
    # (2)
    my_str10 = f"E{my_str3[1:]}"
    print(f"my_str10 = {my_str10}")
    # (3)
    MY_TEMP_LIST = list(my_str3.upper())
    print(f"my_str3 type = {type(my_str3)}")
    print(f"my_temp_list type = {type(MY_TEMP_LIST)}")
    MY_TEMP_LIST[0]="e"
    my_str11 = "".join(MY_TEMP_LIST)
    print(f"my_str11 = {my_str11}")
    # string replace
    my_str12 = my_str11.replace("P","~")
    print(f"my_str12 = {my_str12}")
    # string contains (uses: import operator)
    does_contain = op.contains(my_str12, "RISE")
    print(f"does_contain = {does_contain}")
    # evaluate expression in a string with eval()
    my_str13 = "(2**3)/4"
    print(f"my_str13 = {my_str13}, eval(my_str13) = {eval(my_str13)}")
    # trimming leading and trailing whitespace by default via strip(). can also strip any multitude of leading and trailing characters
    print("\n---trimming with strip")
    my_str14 = "    honey--  "
    print(f"my_str14.strip() = {my_str14.strip()}")
    my_str14 = ",,,,,honey--" # reassigning a new string to variable my_str14 (I'm not changing the CONTENTS of the immutable string)
    print(f"my_str14.strip(',') = {my_str14.strip(',')}")
    my_str14 = ",,,,,honey--88999...."
    print(f"my_str14.strip(',89.') = {my_str14.strip(',89.')}")
    
    ls_test_1 = [2,3,4,5,6,7] 

    # for loops
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
    
    # tuple unpacking
    print("\n---tuple unpacking")
    list_of_tups_1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for idx, (x, y) in enumerate(list_of_tups_1):
        print(f"{idx}: {x} {y}")
    
    # tuple packing
    print("\n---tuple packing via zip (opposite of enumerate)")
    tuple_1 = (1, 2, 3, 4, 5, 6)
    tuple_2 = (11, 12, 13, 14, 15, 16, 17, 18)
    print(list(zip(tuple_1, tuple_2)))

    # list iterable copying 
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

    # list iterable methods / functions
    # ".pop", ".shift", ".push", ".unshift" with .pop() and .insert(val, idx)
    # delete by value with .remove
    # random with shuffle()
    # break and fix with .join, .split
    # slice and splice with [:] and the slice() object
    # pythonic reducing with sum, len, min, max, all, any (instead of map, filter, reduce; also comprehensions rather than lambdas more pythonic)
    # sort with .sort, sorted
    # concate with append(val), [*unpack, val, val], lst += [val, val]

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
    #shuffle(ls_long_1)
    shuffle(ls_long_1)
    print((ls_long_1))

    # join and split
    print("\n---join and split")
    the_str1 = "this is a test string"
    the_str2 = "".join(the_str1.split(" ")) # get rid of white space with join and spilt
    print(f"the_str1 = {the_str1}")
    print(f"the_str2 = {the_str2}")
    
    # slices (slice list iterable and make copies of list iterables)
    print("\n---slicing")
    ls_test_1 = [100, 90, 102, 103, 104, 105]
    print(ls_test_1[:2])
    print(ls_test_1[:3])
    print(ls_test_1[::])  # print all of the list iterable
    print(ls_test_1[::-1])  # reverse the list iterable
    print(ls_test_1[-1])  # last item
    print(ls_test_1[0])
    print(ls_test_1[-6])  # 0 and -6 equivalent in a list iterable with 6 items
    slice_object24 = slice(2,4)
    print(f"ls_test_1[slice_object24] = {ls_test_1[slice_object24]}") # using "slice object" to slice the list iterable

    # splicing (assigning to a slice)
    print("\n---splicing")
    my_colors = ["red", "green", "blue", "black"]
    print(f"original my_colors = {my_colors}")
    my_colors [1:3] = ["orange", "yellow", "aqua"]
    print(f"spliced my_colors = {my_colors}")
    
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
    print("\n---sorting")
    ls_test_1.sort() # "sort()" in place ("sorted()" for immutable sorting)
    print(f"ls_test_1 = {ls_test_1}")

    # list concatenation
    print("\n---list concatenation")
    ls_test_2 = [*ls_test_1, 1000, 1001] # concat via python *unpacking (...spread)
    print(f"ls_test_2 = {ls_test_2}")
    ls_test_2 = ls_test_1 + [2000, 2001] # concat via "+"" sign
    print(f"ls_test_2 = {ls_test_2}") 
    ls_to_append_temp = [3000, 3001]
    for i in ls_to_append_temp:
        ls_test_1.append(i) # append() adds a single value to the end of list iterable
    print(f"ls_test_1 = {ls_test_1}") 

    