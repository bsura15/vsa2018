# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci
sequence is a sequence of numbers where the next number in the sequence is the sum of the
previous two numbers in the sequence. The sequence looks like this:
1, 1, 2, 3, 5, 8, 13...
"""

current_number = 1
previous_number = 0
x = int(raw_input("enter a number"))

next_number = (previous_number + current_number)

for numb in range(0, x):
    print next_number
    previous_number = current_number
    current_number = next_number
    next_number = (previous_number + current_number)











x = int(raw_input("enter a number"))
print x * x

















