age = input("Enter your age: ")
age = int(age)
have_own_car = input("Do you own your own car (y/n): ")

if (age > 21) and (have_own_car == 'y'):
   print ("You are over 21 years old and own your own car")


if (age > 21) and (have_own_car == 'n'):
   print ("You are over 21 years old and you do NOT own your own car")


if (age == 21) and (have_own_car == 'y'):
   print ("You are  21 years old and you  own your own car")

if (age == 21) and (have_own_car == 'n'):
   print ("You are  21 years old and you NOT  own your own car")

if (age < 21) and (have_own_car == 'y'):
   print ("You are younger than  21 years old and you  own your own car")


if (age < 21) and (have_own_car == 'n'):
   print ("You are younger than  21 years old and you do NOT  own your own car")










