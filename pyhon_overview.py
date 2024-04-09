# string literal
my_money = 50
my_spend = 15*1.03
print(f"I have ${my_money-my_spend} left")

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

ls1 = [100,101,102,103,104,105]
# slicing list
print (ls1[:2])
print (ls1[:3])
print (ls1[::])   # print all of list
print (ls1[::-1]) # reverse list
print (ls1[-1])   # last item
print (ls1[0])
print (ls1[-6])   # 0 and -6 equivalent in list with 6 items

# for loops (for, enumerate and range)
for item in ls1:
    print(f"{item}")
for idx,item in enumerate(ls1):
    print(f"{idx}: {item}")
for i in range(0,50):
    print(f"{i}",end=" ")
print()

# pop(), remove by index
ls1.pop() # pops -1 by default
for idx,item in enumerate(ls1):
    print(f"{idx}: {item}")
ls1.pop(0)
for idx,item in enumerate(ls1):
    print(f"{idx}: {item}")
# remove(), remove by value
ls1.remove(101) # remove a value from the list
for idx,item in enumerate(ls1):
    print(f"{idx}: {item}")