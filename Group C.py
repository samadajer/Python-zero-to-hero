# Write a python script that checks if the sum of two integers is 20 or if one of the integers is 20
# return true
#e.g
# 9, 11 will return True
# 20, 12 will also return True
# 13, 17 will return False
first_number = int(input("the first number "))
second_number = int(input("the second number "))
addition = (first_number + second_number)
print(addition)
if addition == 20 or first_number == 20 or second_number == 20:
    print("True")
elif addition <20 or first_number<20 or second_number<20:
      print(f"False")
elif addition > 20 or first_number>20 or second_number>20:
      print(f"False")