#taking input from user 

age = input("Please enter your age: ")
age1 = int(input("Please enter your age: "))  # type casting
print("Your age is: " + age)
print(type(age))  # This will show that the type of 'age' is <class 'str'>

#find your current age 
current_year = 2026
birth_year = current_year - age1
print("Your birth year is: " + str(birth_year))

#byear = int(input("Please enter your birth year: "))
#cyear = 2026
#age2 = cyear - byear
#print(age1)