import math
import operator as myop # for using myop.contains()
from pprint import pprint # pretty print

# Import shuffle funct from random module, usage: shuffle()
from random import shuffle
# Import randint func from random module, usage: randint()
from random import randint
# Import random module, usage random.function90, eg: random.random()
import random 

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

# Unit testing
import unittest
from create_titles import create_titles

# Type hints
from typing import List # generic List type
from typing import Dict # generic Dictionary type

# Hero battle OOP game
from hero_battle.hero_and_enemies import *

# Iterables
# An iterable is any Python object capable of returning its members one at a time,
# permitting it to be iterated over in a for-loop.
# Sequential iterables: lists, tuples, and strings
# Non-sequential iterables: dictionaries (but insertion ordered in Python 3.7 onwards) and sets

# Python's *UNPACKING is the very similar to JavaScript's ...spread operator
# JS ...spread expands an iterable into individual elements (unpacks vars out of suitcase called my_list)
#
# def add(a, b, c):
#    return a + b + c
# my_list = [1, 2, 3]
# result = add(*my_list)  # Unpacks my_list into 1, 2, 3
# print(result)  # Output: 6
#
# Python's *PACKING is the very similar to JavaScript's ...rest operator
# JS ...rest put the remaining (rest of) values into an array (pack vars into suitcase called numbers)
#
# def sum_all(*numbers):
#    total = 0
#    for num in numbers:
#        total += num
#    return total
# result1 = sum_all(1, 2, 3)  # Packs 1, 2, 3 into a list called numbers
# print(result1)  # Output: 6
#
# Python *args is positional arguments, **kwargs is keyword arguments (for dictionaries)

# Strings, numbers (ints and floats) and tuples are immutable. Give performance optimisation, thread safety, memory efficiency, easier debugging, etc

# simple bank account class
class Account:
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

# Create class that inherits from "unittest.TestCase". Assert is a word that means "affirm".
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

# Python's unpacking *operator, like JS ...rest, unlimited POSITIONAL arguments, positional args: (100,200,300) 
def my_sum(*args: int) -> int: # ...rest *args, 
    the_sum = 0
    for i in args:
        the_sum += i
    return the_sum

# Python's unpacking **operator, like JS ...rest, but for unlimited KEYWORD arguments, keyword args: (a="Hello", b="World", c="\n")
# print(my_concat1(a="Happy",b="Bday",c="To",d="You")) # keyword args packed into suitcase/dict called kwargs
def my_concat1(**kwargs) -> list: # no type hints used for kwargs here
    lst:List[str] = []
    for k,v in kwargs.items():
        print(f"k={k}, type(k)={type(k)}, v={v}, type(v={type(v)})")
        lst+=v
    return lst

# Python type hint parameters for dictionary (no **unpacking operator)
# type-hints only for input parameters
# all keys in the scorecard dictionary must be strings (str), and all values must be integers (int)
def get_total_marks(scorecard: Dict[str, int]) -> int:
    marks = list(scorecard.values())  # marks : List[int]
    return sum(marks)

# Python's unpacking **operator, like JS ...rest, but for unlimited KEYWORD arguments, keyword args: ("the_dict_in"={'apple': 5, 'banana': 3})
# **kwargs and type-hints for input parameters: OVERKILL
def my_concat2(**kwargs: Dict[str,str]) -> list: # type hints for **kwargs used here
    lst:List[str] = []
    input_dict = kwargs["the_dict_in"]
    for v in input_dict.values():
        lst+=v
    return lst

# OOP enemies battling each other
def enemy_v_enemy_battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.get_health_points() > 0 and e2.get_health_points()  > 0:
        print("----------")
        e1.print_info()
        e2.print_info()
        e1.possible_attribute_change()
        e2.possible_attribute_change()
        e2.attack()
        e1.set_health_points(e1.get_health_points()-e2.get_attack_damage())
        e1.attack()
        e2.set_health_points(e2.get_health_points()-e1.get_attack_damage())

    if e1.get_health_points() > 0:
        print("Enemy 1 wins")
    else:
        print("Enemy 2 wins")

# OOP hero battling an enemy (hero uses the pythonic @property decorator
# for getters and setters, enemy uses non-pythonic getters and setters)
def hero_v_enemy_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.get_health_points()  > 0:
        print("----------")
        enemy.possible_attribute_change()
        enemy.attack()
        hero.health_points -= enemy.get_attack_damage()
        hero.attack()
        enemy.set_health_points(enemy.get_health_points()-hero.attack_damage)

    if hero.health_points > 0:
        print("Hero wins")
    else:
        print("Enemy wins")

# Python is a duck-typed language, if it looks like a duck, it is a duck
class Dog:
    def say(self):
        print("woof")
class Cat:
    def say(self):
        print("meow")

# Main
if __name__ == '__main__':
    """ will end program if y=unit test run
    print("\n---unit testing")
    unittest.main()
    """

    """ don't want to ask for user input all the time
    print("\n---try except")
    while True:  # TEEF (try, except, else, finally)
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

    

    # object orientated programming (oop)
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

    # big-list-1
    # strings (and formated string literals, f-strings)
    # concat with +, f-string, .join
    # slicing with slice[:], f-strings, list()
    # case: .upper(), .lower(), .title()
    # replace all characters in a string with .replace(), or certain number of chars with replace(num)
    # check if it contains with operator.contains(), need to import operator
    # evaluate expression in string with eval()
    # trim leading/trailing whitespace via .split(), or remove all .,89 trailing/leading characters with .split(".,89")
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
    does_contain = myop.contains(my_str12, "RISE")
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
    print("\n---zoo list")
    my_zoo = ["elephant", "snake", "monkey", "tiger", "rhino"]
    print(f"my_zoo = {my_zoo}")
    my_zoo.pop() # remove the last animal from the list (pop(-1) is default)
    my_zoo.pop(2) # remove animal from index 2
    my_zoo.append("lion") # add a lion to the end of the list
    my_zoo.pop(0) # remove the first animal from the list
    print(f"my_zoo = {my_zoo}")
    print(f"my_zoo[:3] = {my_zoo[:3]}")

    ls_test_1 = [2,3,4,5,6,7] 

    # for loops. for, for with enumerate and for with range
    print("\n---for loop")
    for item in ls_test_1:
        print(f"{item}")
    print("\n---for loop with enumerate")
    for idx, item in enumerate(ls_test_1):
        print(f"{idx}: {item}")
    ls_long_1 = []
    print("\n---for loop with range")
    for i in range(0, 50):
        print(f"{i}", end=" ", sep=" ")
        ls_long_1.append(i)
   
    # printing with *unpacking (...spreading)
    print("\n---printing with *unpacking")
    print(
        *ls_long_1, sep=" ", end="\n"
    )  # astrix unpacks the list iterable into a new list iterable without formatting, so like print(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,....)
    print("\n---unpacking a list into specific variables then the remaining into *rest")
    first, second, *rest = ls_long_1  # unpacking into variables and a list iterable
    print(f"first={first}, second={second}, rest={rest}")
    
    # printing with unpacking *args (...rest)
    print("\n---python unpacking *args == ...rest")
    print(my_sum(1,2,3))
    print(my_sum(1,2,3, 400, 500))

    # printing via unpacking dictionaries with **kwargs (...rest) and/or type-hinting
    print("\n---python unpacking dictionaries with **kwargs / type-hinting combos")
    # **kwargs only for input parameters
    print(my_concat1( a="Happy", b="Bday", c="To", d="You")) # keyword args
    # type-hints only for input parameters
    scores_dic1 = {'english': 3, 'maths': 4, 'history': 3}
    print(f"get_total_marks(scores_dic1) = {get_total_marks(scores_dic1)}")
    # **kwargs and type-hints for input parameters: OVERKILL!
    print(my_concat2( the_dict_in={"a":"Merry", "b":"Xmas", "c":"Everyone"})) # the_dict_in={} is needed to create keyword args, trick is 2nd argument is a dict
    hogmanay = {"x":"Happy", "y":"New", "z":"Year"}
    print(my_concat2(the_dict_in=hogmanay)) # the_dict_in={} is needed to create a keyword args, trick is 2nd argument is a dict

    # tuples. used for datasets
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

    # set (no duplicates). used for very fast organisation and remove duplicates from list
    print("\n---sets")
    my_set1 = {1,2,2,3,3,4,5,6}
    print(f"my_set1 = {my_set1}")
    print(f"len(my_set1) = {len(my_set1)}") # uniques only
    #print(f"my_set1[0]{my_set1[0]}") # error, sets are unordered, cannot access by index
    my_set1.add(100)
    print(f"my_set1.add(100) = ", end= "") # add value to the set
    print(my_set1)
    my_set1.discard(1)
    print(f"my_set1.discard(1) = ", end= "") # remove value from the set
    print(*my_set1, sep="-", end = "\n")
    my_set1.clear()
    print(f"my_set1.clear() = ", end= "") # clear all values from the set
    print(my_set1)
    my_set1.update([2000, 2001])
    print(f"my_set1.update([2000,2001]) = ", end= "") # add more than one value to the set
    print(*my_set1, sep="_", end = "\n")

    # dictionary (as of python 3.7, dictionaries are insertion ordered!)
    print("\n---dictionaries")
    my_dic1 = {"k1": 101, "k2": 102, 2233: 102.5, 333: 103, 'k4': 104}
    for key,value in my_dic1.items():
        print(f"key = {key}, value = {value}")
    # reverse the key and value for each item
    rev_dic1 = {v:k for k,v in my_dic1.items()}
    print(f"rev_dic1 = {rev_dic1}")
    print ("popping first key in the dictionary")
    rev_dic1.pop(101)
    print(f"rev_dic1 = {rev_dic1}")
    rev_dic2 = rev_dic1 # "reference copy", rev_dic2 points to rev_dic1 data
    #rev_dic3 = rev_dic1.copy() # "value copy" via copy method
    rev_dic3 = {**rev_dic1} # unpacking / spread "value copy" of KEYWORD args double asterisk
    print("pooping 102 from rev_dic2")
    rev_dic2.pop(102)
    print(f"rev_dic1 = {rev_dic1}")
    print(f"rev_dic2 = {rev_dic2}")
    print("pooping 103 from rev_dic3")
    rev_dic3.pop(103)
    print(f"rev_dic1 = {rev_dic1}")
    print(f"rev_dic3 = {rev_dic3}")
    print("---assignment")
    my_vehicle = {
        "model": "Ford",
        "make": "Explorer",
        "year": 2018,
        "mileage": 40000
    }
    for k,v in my_vehicle.items():
        print(f"key={k}, value={v}")
    my_vehicle2 = {**my_vehicle}
    print(f"my_vehicle2 = {my_vehicle2}")
    # adding items to vehicle 2
    my_vehicle2.update({"number_of_tyres":4}) # pass dictionary item to update method
    my_vehicle2["number_of_exhausts"]=1 # create a new key and assign it a value
    print(f"my_vehicle2 = {my_vehicle2}")
    # deleting items form vehicle 2
    my_vehicle2.pop("number_of_tyres") # delete the mileage key / value pair
    my_vehicle2.popitem() # delete the final key / value pair
    del my_vehicle2["mileage"] # delete the mileage key / value pair
    print(f"my_vehicle2 = {my_vehicle2}")
    print([k for k in my_vehicle2.keys()]) # print only vehicle 2's keys using list comprehension

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

    # big-list-2
    # list iterable methods / functions
    # ".pop", ".shift", ".push", ".unshift" with .pop() and .insert(val, idx)
    # delete by value with .remove
    # random with shuffle, randint, random
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

    # shuffle, randint and random 
    print("\n---shuffle, randint and random")
    #shuffle(ls_long_1)
    shuffle(ls_long_1) # shuffle the list
    print((f"shuffling list iterable in place: {ls_long_1}"))
    print(f"random int between 1 & 10, inclusive of 1 and 10 (1,10): {randint(1,10)}")
    print(f"random float between 0 & 1, exclusive of zero and inclusive of 1 [0,1): {random.random()}")

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

    # OOP
    print("\n---type inference off, explicit types in python, type hints for variables")
    legs: int = 4
    ears: int = 2
    weight_kg: float = 70.3
    name: str = "John Smith"
    male: bool = True
    print(f"legs={legs}, type(legs)={type(legs)}")
    print(f"ears={ears}, type(ears)={type(ears)}")
    print(f"weight_kg={weight_kg}, type(weight_kg)={type(weight_kg)}")
    print(f"male={male}, type(male)={type(male)}")
    print(f"name={name}, type(name)={type(name)}")
    # using imported enemy class from hero_battle.Enemy
    print("---hero battle with with encapsulation (private, name mangled, attributes)")
    zombie = Enemy("Zombie", 10, 2) # instantiate new enemy object
    big_zombie = Enemy("Big-Zombie", 100, 10) # instantiate new enemy object
    zombie.print_info()
    big_zombie.print_info()
    """BEWARE, we can create a new instance attribute called "__type_of_enemy" specific to the zombie
    instance which is DIFFERENT from the private "__type_of_enemy" attribute defined in the class"""
    #zombie.__type_of_enemy = "Oogggggre" # (1) new attribute specific to the zombie instance
    #print(f"zombie.__type_of_enemy = {zombie.__type_of_enemy}") # (2) gives error (so long as (1) above not explicitly defined)
    """ DON'T DO (1) or (2) above, will not be what we expect. DON'T DO (3) below, works but very bad practice"""
    #print(f"zombie._Enemy__type_of_enemy = {zombie._Enemy__type_of_enemy}") # (3) works but linter saying don't do this, use getters & setters
    """ DO (4) below, getters and setters are proper practice for private / name mangled attributes"""
    zombie.get_type_of_enemy() # (4) using the private attribute "__type_of_enemy" defined in the class

    zombie_child = Zombie(5, 1)
    zombie_child.talk()    
    zombie_child.spread_disease()
    # python method overloading (without @overload decorator)
    zombie_child.spread_disease("Gyads min, I'm rife wee it")
    # python method overloading (with @overload decorator)
    zombie_child.eat_flesh()
    zombie_child.eat_flesh(111222333)
    zombie_child.eat_flesh("I love the taste of flesh in the morning")

    ogre = Ogre(7, 3)
    print(f"{ogre.get_type_of_enemy()} has {ogre.get_health_points()} health points and attacks with damage {ogre.get_attack_damage()}")
    ogre.talk()

    print("\n---time for enemy v enemy OOP battle")
    battle_zombie = Zombie(10,2)
    battle_ogre = Ogre (7,3)
    enemy_v_enemy_battle(battle_zombie, battle_ogre)

    print("\n---composition (has-a relationship): hero v enemy battle")
    # interface: is-a relationship (car is a vehicle; inheritance)
    # composition: has-a relationship (vehicle has an engine)
    # composition is when a class has another class
    # a vehicle must have an engine, but an engine need not have a vehicle
    battle_baddie = Zombie (8,1) 
    battle_goodie = Hero(5,1,Weapon("Sword",2))
    battle_goodie.use_weapon()
    hero_v_enemy_battle(battle_goodie, battle_baddie)

    print("\n---duck types (duck typing) for 'virtual functions', use 'hasattrib'")
    # python duck types for "virtual functions"
    pet_dog = Dog()
    pet_dog.say() # prints "woof"
    pet_cat = Cat()
    pet_cat.say() # prints "meow"
    pet_list = [pet_dog, pet_cat] # list of DIFFERENT instatiated objects
    for a_pet in pet_list:
        # terany operator, execute method if class has that attribute
        a_pet.say() if hasattr(a_pet,"say") else ...

    print("\n---MyPy Type Hints with append() and extend()")
    ls_test_3: List = [1,2,3,4,5] # important: List by iteself means type Any
    print(f"ls_test_3 = {ls_test_3}")
    app_1: List[int] = [111, 222] # List of int type
    # append pushes a SINGLE object to a list iterable
    ls_test_3.append(app_1) # we can append a list (ie: [111,222]) to a type of List[Any] 
    print(f"ls_test_3 = {ls_test_3}") # [1,2,3,4,5,[111,222]]
    # extend pushes a MULTIPLE objects, one at a time, to a list iterable (objects are stored in a list)
    ls_test_3.extend([8888,9999]) 
    print(f"ls_test_3 = {ls_test_3}") # [1,2,3,4,5,[111,222],8888,9999]

    print("\n---Python ternary operator")
    # ternary
    print("two is bigger than one") if 2 > 1 else print("two is not bigger than one")

    print("\n---Python reverse list traversal (-1, -1, -1)")
    my_list = [1,2,3,4,5]
    print(my_list)
    for i in range(len(my_list)-1, -1, -1): # start at end, stop at one before -1 (zero), step of -1 (rev dir)
        print(my_list[i])
    print(my_list[::-1]) # reverse list via slicing with step size of -1 (more "pythonic")

    print("\n---Dictionaries have mutable keys - mutable types are used in Python DSA")
    dict1 = {"animal": "cat"}  # Correct dictionary creation
    print(dict1["animal"])  # Output: cat
    dict2 = dict1  # dict2 and dict1 reference the same dictionary
    dict2["animal"] = "dog"  # Modify the shared dictionary
    print(dict1["animal"])  # Output: dog (changes are reflected in dict1)
    print(dict2["animal"])  # Output: dog (dict2 also reflects the changes)
