import algorithm
print("Write down the first list")
print("Example, [2,3,3]")
mylist=eval(input())
print("Write down the second list")
mylist1=eval(input())
if len(mylist) != len(mylist1):
    print("ERROR!")
    print("The two lists must have the same amount of numbers")
algorithm.do_calculation(mylist, mylist1)