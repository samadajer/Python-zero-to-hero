question = "Hello there, how old are you?"  #What index will return "how old"?
print(question[13:20])
story = "Python is awesome"  #What is story[2:4] + story[-1] ?
print(story[2:4] + story[-1])
mystring = "Python rocks" #What is len(mystring)?
print(len(mystring))
#flower = "Rose" #What is flower[0] = "P" ; print(flower)? Will it return "Pose"?
#flower[0] = "P"
#print(flower) No; Strings are immutable
word = "Python is so cool" #What is word[-4:] * 3
print(word[-4:] * 3)
#Write a code that returns "pepsi" as "PEPSI"
brand = ("pepsi")
print(brand.upper())
#Write a code that return "macdonald" as "MacDonald"
food = "macdonald"
print(food[0].upper() + food[1:3].lower() + food[3].upper() + food[4:].lower())
#Write a code that returns "MUSHRAH" as "mushrah"
name = "MUSHRAH"
print(name.lower())
#Using the built-in method, how will you "Hello World" as a list?
mystring = "Hello World"
print(mystring.split())
#How do i add a "-" in between every character in a string "Python is cool" ?
mystring = "Python is cool"
print('-'.join(mystring))
#How do I remove "Hello" from "Hello World"?
mystring = "Hello World"
print(mystring[0:5])
#What is the index of the first character in a string?
#The index of the first character in a string is 0
mystring = "Abdulsamad"
print(mystring.index("A"))
#Using one of the string built-in methods,  print out the numbers of 'o' in the string; "Hello, python is sooo cool"?
mystring = "Hello, python is sooo cool"
print(mystring.count('o'))
#If I want to write this string: "hello world! welcome to Python" as a title case, what inbuilt method of python will I call? =title()
title_case = "hello world! welcome to python"
print(title_case.title())




