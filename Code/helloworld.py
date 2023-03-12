from cgitb import text


print("hello world")
print(5/2) # division
print(5//2) # want to know number of times 2 goes into 5, without the remainder
print(5%2) # show only the remainder of 5/2
print(1000000) # avoid commas(,) when entering numbers
print(2**2) # 2 raised to the power 2
red_bucket = "shaphan"
print(red_bucket)
print (5==4) # Is 5 equal to 4?
print (5!=4) # Is 5 NOT equal to 4?

Daniel_age = 2
Age_at_Kindergarten = 4
print (Daniel_age == Age_at_Kindergarten) # Is Daniel's age equal to age at Kindergarten?

#write conditional statements (if)
Daniel_age = 2
Age_at_Kindergarten = 4
if Daniel_age < Age_at_Kindergarten: # condition is true, then print next line code
    print("Daniel should be in pre-school") 

Daniel_age = 5
Age_at_Kindergarten = 4
if Daniel_age > Age_at_Kindergarten: # condition is true, then print next line code
    print("Daniel should be in nursery school")

#Alternative way of expressing the above two conditions in one code
Daniel_age = 5
Age_at_Kindergarten = 4
if Daniel_age < Age_at_Kindergarten:
    print("Daniel should be in pre-school") # print this result if the above condition is true
else:
    print("Daniel should be in Kindergarten or in another class") # print this result if the above condition is not true

#check and display results when first condition is not true, second is and thid is not
Daniel_age = 4
Age_at_Kindergarten = 4
if Daniel_age < Age_at_Kindergarten:  # condition not true, nothing will print
    print("Daniel should be in pre-school")
elif Daniel_age == Age_at_Kindergarten: # condition true, print
    print("Enjoy kindergarten")
else:
    print("Daniel should be in another class") # condition not true, nothing will print

#check and display results when onlt the last condition is true
Daniel_age = 5
Age_at_Kindergarten = 4
if Daniel_age < Age_at_Kindergarten:  # condition not true, nothing will print
    print("Daniel should be in pre-school")
elif Daniel_age == Age_at_Kindergarten: # condition true, nothing will print (elif = else if)
    print("Enjoy kindergarten")
else:
    print("Daniel should be in another class") # condition true, print


# How tocreate Functions in Python
# A function is a block of code that you can package together with a name and it does something

# def = define; print_shaphan() = new function created
# A function must first be defined before calling it
def print_shaphan(): # define
    text = "Shaphan is learning python"
    print(text)
    print(text)
    print(text)
print_shaphan() # call
print_shaphan()
print_shaphan()

# can also specify the text within the function defined
def print_shaphan(text): # defined func expects a parameter (also called 'value')
    print(text) # takes the parameter/value passed intothe func
    print(text)
    print(text)
print_shaphan("Shaphan is learning python") # "Shaphan is learning python" is a parameter passed into the function

# Pass values into a func using conditional statements
# E.g., determine where a child should be in school based on his/her age
def school_age_calculator(age, name):# get two values/parameters/arguments (age nad name) about the child
    if age < 4:
        print("Enjoy the time!", name, "is only", age )
    elif age == 4:
        print("Enjoy kindergarten!,", name)
    else:
        print("They grow up so fast!")
school_age_calculator(4, "Daniel") # vary the number (4) to get different results printed

# How to get a parameter back from a func
# E.g., determine age in ten years using a func
def add_ten_to_age(age):
    New_age = age + 10
    return New_age # return results of age + 10

How_Old_Will_I_Be = add_ten_to_age(2)
print(How_Old_Will_I_Be)




