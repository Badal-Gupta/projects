import numbers
import string
import random
length=int(input("Enter the length of Password you want: "))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
special=string.punctuation
number=numbers.Number
if length <12:
    pwd=lower+upper+digit+special+str(number)
    passd=random.sample(pwd,length)
    password = "".join(passd)
    print("Your Password is:",password)
    print("This Password is ignored")
else:
    pwd=lower+upper+digit+special+str(number)
    passd=random.sample(pwd,length)
    password="".join(passd)
    print("Your Password is:", password)
    print("This Password is accepted")

