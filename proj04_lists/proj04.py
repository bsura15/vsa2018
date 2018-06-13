# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

numb_name = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

for item in numb_name:
    if item < 5:
        print item



print "______"


#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [11, 22 ,3 ,6 , 8 , 9 ,15 ,10 ,12 ,4]
b = [88, 53 ,3 ,5 , 8, 7, 15, 34, 14, 2]

for item in a:
    for item_b in b:
        if item == item_b:
            print item





#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.

counter = 0
#sum = 1
for item in d:
    if item == "a":
        d[counter] = "*"
    counter = counter + 1
print d


print "________"

#Part IV

#Ask the user for a string, and print out whether this string is a palindrome or not.

print "Hello!"
list_one = str
list_two = str
str = raw_input("Choose a word and I will tell you whether it is a palindrome or not:")
list_two.reverse
list_one = list_two
print ""






