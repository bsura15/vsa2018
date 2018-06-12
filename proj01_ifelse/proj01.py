# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.

#Then, it prints out a sentence that says the number of years until they graduate.
#Name= raw_input("what is your name?")
#print Name
#grade= raw_input("what grade are you in?")
#years_left= raw_input(12-7)
#print years_left
















# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday
current_day= 11
current_month= 6
birth_month= int(raw_input("what is your birth month in a number?"))
print birth_month
birth_day= int(raw_input("what is the day your were born?(number)"))
print "day"
if birth_month > current_month:
    print "your birthday is in" + str(birth_month - current_month)
else:
    print "your birthday is in" + str(12-(current_month - birth_month))
print "months"
if birth_day > current_day:
    print "your birthday is in" + str(birth_day - current_day)
else:
    print "your birthday is in" + str(30-(current_day - birth_day))
print "days"













# If you complete extensions, describe your extensions here!