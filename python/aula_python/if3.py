age = input("Enter your age: ")
age = int(age)
have_own_car = input("Do you own your own car (y/n): ")

if age > 21:
   if have_own_car == 'y':
     print ("You are over 21 years old and own your own car")
   else:
     print ("You are over 21 years old and do NOT own your own car")

else:
   if have_own_car == 'y':
     print ("You are yonger than 21 years old and own your own car")
   else:
     print ("You are over 21 years old and do NOT own your own car")

