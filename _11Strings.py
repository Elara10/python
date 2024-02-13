name="Harry"
friend="Rohan"
anotherFriend='Lovish'
apple='''He said,
Hi Harry
hey I am good
"I want to eat an apple'''
print("Hello "+ name)
# print(apple)
print(name[0])

print("Let's use a for loop")
for character in apple:
    print(character)





names="Harry,Shubham"
print(len(names))

fruit="Mango"
len1=len(fruit)
print("Mango is a",len1,"letter word.")
print(fruit[0:4])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])
print(fruit[-3:-1])

QUICK QUIZ
nm="Harry"
print(nm[-4:-2])



# STRINGS ARE IMMUTABLE
a="!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))
blogHeading="introduction to js"
print(blogHeading.capitalize())
str1="Welcome to the Console !!!"
print(len(str1))
# print(len(str1.center(50)))
# print(a.count("r"))
# print(str1.endswith("!!!"))
# print(str1.endswith("the",4,15))
str2="He's name is Dan.He is an honest man."
# print(str2.find("is"))
# print(str2.index("Dan"))
# str3="WelcomeToTheConsole"
# print(str3.isalnum())
# str4="Welcome"
# print(str4.isalpha())
# print(str4.islower())
# str5="We wish you a merry christmas\n"
# print(str5.isprintable())
# str6="    "
# print(str6.isspace())
# str7="World Health Organization"
# print(str7.istitle())

# str8="WORLD HEALTH ORGANIZATION"
# print(str8.isupper())


# str9="Python is a Interpreted Language"
# print(str9.startswith("Python"))
# print(str9.swapcase())


str10="His name is Dan.Dan is an honest man."
print(str10.title())