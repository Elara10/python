
# REQUIRED ARGUMENTS

# def average(a,b):
#     print("The average is",(a+b)/2)

# average(1,5)



# DEFAULT ARGUMENTS

# def average(a=9,b=7):
#    print("The average is",(a+b)/2)
# average(1,5)----->iN THIS CASE IT WILL PRINT 3.0 BECAUSE REQUIRED ARGUMENTS HAS MORE PRIORITY THAN DEFAULT ONE



# def average(a=8,b=9):
#     print("The average is",(a+b)/2)

# average(1)-->output 5.0 BEACUSE 1+9/2=5.0


# def average(a=9,b=6):
#     print("The average is",(a+b)/2)

# average(b=5)->7.0






# def name(fname,mname="John",lname="Watson"):
#     print("Hello,",fname,mname,lname)
# name("Any")->Hello, Any John Watson

# def name(fname,mname="John",lname="Watson"):
#     print("Hello,",fname,mname,lname)
# name("Any","Agarwal")------->Hello, Any Agarwal Watson



# def name(fname,mname="John",lname="Watson"):
#     print("Hello,",fname,mname,lname)
# name("Any","Agarwal","Jain")->Hello, Any Agarwal Jain





# VARIABLE LENGTH ARGUMENTS

# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#       sum=sum+i
#     print("Average is :",sum/len(numbers))
# average(5,6,1,6)




def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(fname="James",mname="Buchanan",lname="Barnes")