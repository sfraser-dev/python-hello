# reviewing written python notes

import io
from random import shuffle
from random import randint

mylist = [4,3,6,5]

# pop removes chosen index from the list
popped = mylist.pop(-1)
print(mylist)
print(popped)

# sort is an IN PLACE method
mylist.sort()
print(mylist)

# reverse is also an IN PLACE method
mylist.reverse()
print(mylist)
mylist = [1,2,3,4,5,6]
print(mylist[::-1])

with open("myfile.txt", mode="w") as fh:
    fh.writelines(["line1\n", "line2\n", "line3\n"])
fh.close()
file_content = []
with open("myfile.txt","r") as fh:
    file_content = fh.read()
fh.close()
print(file_content)

mylist = [3, 5, 2, 1, 4]
mylist.reverse()
print(mylist)

# AND, OR and NOT logical operator
print((100==100) and (2==2))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    if num % 2 == 0:
        print(num)

# list of tuples (common structure used in Python libraries)
mylist = [(1,2), (3,4), (5,6), (7,8)]
print(len(mylist))
# tuple unpacking
for (x,y) in mylist:
    print(f"{x} {y}")

# looping through dictionary (dictionaries are not ordered)
mydict = {"k1":1, "k2":2, "k3":3}
for k in mydict.keys():
    print(k)
for k in mydict.values():
    print(k)
for k in mydict.items():
    print(k)
# tuple unpacking for dictionaries
for k,v in mydict.items():
    print(f"{k} {v}")

# range (generator, special function generate information, but not in memory)
for num in range(0,11,2):
    print(num)

# enumerate
mylist = [2,4,6,8,10]
for idx, num in enumerate(mylist):
    print(f"{idx}, {num}")

# zip (tuple packing)
mylist2 = ['c','d','e','f','g']
mylist3 = [100, 200, 300, 400, 500]
print(list(zip(mylist, mylist2, mylist3)))

# random library
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
print(randint(0,100))

# list comprehension
mylist = [x**2 for x in range(0,11)]
print(mylist)
mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)

thestr = "Print only words that start with an s in this sentence"
mywords = thestr.split(" ")
# print only words that start with an s
s_only = [x for x in mywords if x[0].lower()=='s']
print(s_only)
# print out even length words
even_only = [x for x in mywords if len(x)%2==0]
print(even_only)
