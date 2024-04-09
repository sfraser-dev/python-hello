import io
from random import shuffle
from random import randint
from pprint import pprint  # pretty print

print("\n---string literal")
my_money = 50
my_spend = 15 * 1.03
print(f"I have ${my_money-my_spend} left")

"""
# try / except
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

print("\n---slices")
ls_test_1 = [100, 101, 102, 103, 104, 105]
print(ls_test_1[:2])
print(ls_test_1[:3])
print(ls_test_1[::])  # print all of list
print(ls_test_1[::-1])  # reverse list
print(ls_test_1[-1])  # last item
print(ls_test_1[0])
print(ls_test_1[-6])  # 0 and -6 equivalent in list with 6 items

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
print(
    *ls_long_1, sep=" ", end="\n"
)  # astrix unpacks the list into a new list without formatting
print("\n---unpacking a list into specific variables then the reamining into *rest")
first, second, *rest = ls_long_1
print(f"first={first}, second={second}, rest={rest}")

print("\n---tuple unpacking")
list_of_tups_1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
for idx, (x, y) in enumerate(list_of_tups_1):
    print(f"{idx}: {x} {y}")

print("\n---tuple packing via zip (opposite of enumerate)")
tuple_1 = (1, 2, 3, 4, 5, 6)
tuple_2 = (11, 12, 13, 14, 15, 16, 17, 18)
print(list(zip(tuple_1, tuple_2)))

print("\n---IN PLACE, pop(), remove by index")
ls_test_1.pop()  # pops -1 by default
for idx, item in enumerate(ls_test_1):
    print(f"{idx}: {item}")
ls_test_1.pop(0)
for idx, item in enumerate(ls_test_1):
    print(f"{idx}: {item}")
print("\n---IN PLACE, remove(), remove by value")
ls_test_1.remove(101)  # remove a value from the list
for idx, item in enumerate(ls_test_1):
    print(f"{idx}: {item}")


print("\n---IN PLACE shuffle")
shuffle(ls_long_1)
print((ls_long_1))
rand_int = randint(1,100) 
print(f"rand_int={rand_int}")