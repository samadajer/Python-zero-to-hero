#Create a list that contains at least one string, int and a float
my_list = ['Abdul', 12, 12.4]
print(my_list)

#How do i index a nested list? for example if i want to grab 2 from [1,1,[1,2]]
my_list = [1,1,[1,2]]
print(my_list[-1][-1])

#If lst = [0,1,2]. what is the result of Lst.pop()
lst = [0,1,2]
print(lst.pop())

#list can have multiple objects/data types? YES

#When do we choose a list and when do we use a dictionary
#We use lists when we want to store multiple items in a variable
#We make use of a dictionary to store data in values in keys:value pairs

#Create a dictionary with a 3 key-value pair
dict = {'Name': 'Hakeem', 'Age': 28, 'Height': 167}
print(dict)

#Create a dictionary where all the keys are strings and all the values are integers
dict = {'employees_numbers':{'wemmy': 1221, 'muritadoh': 1222, 'ola': 1223, 'sulyman': 1224}}
print(dict['employees_numbers']['wemmy'])

#Dictionaries can retain order and are a sequence. |YES

#Given d = {'k1':[1,2,3]}. What is the output of d['k1'][1]t. Invalid syntax
d = {'k1':[1,2,3]}
print(d['k1'][1])

#Dictionaries are immutable.   keys are immutable while dictionary themselves are mutable

#d = {'simple_key':'hello'}. grab hello
d = {'simple_key': 'hello'}
print(d['simple_key'])

#my_dict = {'k1':{'K2':'hello'}} grab hello
my_dict = {'k1':{'k2':'hello'}}
print(my_dict['k1']['k2'])

#my_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]}
my_dict = {'k1':[{'nest_key' :['this is deep', ['hello']]}]}
print(my_dict['k1'][0]['nest_key'][-1])

my_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(my_dict['k1'][2]['k2'][1]['tough'][-1])