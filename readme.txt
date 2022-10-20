-Purpose: Assembling together everything learned in this unit, part one
-Practice Grade on how much of criteria is met

-Prompt:
-Make a program that accepts two lists of numbers from the user of equal length, and prints out a list that has boolean representing if the elements from both lists at that location are both greater than 5.
e.g.
[1,2,6,6] and then [1,6,7,3] gets [False, False, True, False]


-Requirements:
-Program must use have two files: main.py and algorithm.py. algorithm.py should do all the heavy lifting of calculating the lists, and main.py holds the interface for the user.
-Refresher: to use multiple files, use "import __", where "__" is the name of the file you want to import in the current folder (without the .py extension). This will execute all of the imported file, and store all its data in __.
e.g. 
main.py:
import algorithm
mylist = [5]
algorithm.do_calculation(mylist)

algorithm.py:
def do_calculation:
	...


-Program must use a conditional operator
-Refresher: and takes two conditions (True or False) and returns a condition representing if they are both True, or does the same thing except it represents if either are True, not takes one condition and negates it. All equality operators (< == != > <= >=) return conditions.
e.g.
(not a > 1) or (b < 2)


-Program must use list comprehension for the calculation, and be written in one line.
-Refresher: list comprehension is like a compression of a for loop. It looks like [<each_new_element> for <iterator> in <container> {optional:} if <condition>]
e.g. 
[i for i in range(0,5)] == [0,1,2,3,4]
[i+1 for i in [1,2,3] if i != 2] == [2,4]

-Program must give the user an error if they fail two provide two valid lists or if they are of different lengths, and then give them an oppurtunity to try again.


-Program must give a sensible interface for the user, using input() and print()


-Program must give the correct result


-Program must be uploaded to public github so I can see it