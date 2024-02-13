# a=int(input("Enter your age"))
# print("Your age is:",a)
# if(a>18):
#    print("You can drive")
# else:
#    print("You cannot drive")


# if else  elif--1

# applePrice=10
# budget=200
# if(budget-applePrice>590):
#     print("Alexa,add 1 kg Apples to the cart.")
# elif(budget-applePrice>70):
#     print("Its okay you can buy")
# else:
#     print("Alexa,do not add Apples to the cart.")


# if else elif--2

# num=int(input("Enter your number"))
# if(num<0):
#     print("Number is negative.")
# elif(num==0):
#     print("Number is zero.")
# elif(num==999):
#     print("Number is special.")
# else:
#     print("Number is positive.")
# print("I am happy now")





# NESTED IF
num=int(input("Enter a number"))
if(num<0):
   print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10  and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
    