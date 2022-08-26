print('Hello World', end=" | ") # print is a new line by default for each new print, setting 'end' overrides it

print("Hello World Two")

name = 'Madison'
age = 26

print(f'my name is {name} and i am {age}') # equivalent of console.log(`hi i'm ${variable}`) in js

name = "Mads" # you can redeclare variables wherever and change type

'''this is how you write multi line comments
apparently? lol lets find out'''

print(name[0]) # accesses first index in a string

print(name[0:3]) # slices name variable from indexes 0 through 3 and prints

print('test string for capitalisation'.capitalize()) # capitalise the string it's applied to

''' declare functions in python with the def keyword.
then, name your function and open brackets. see main.py for example.'''

'''
def function_name(parameters):
    # What the function does goes here
    return result 
    '''