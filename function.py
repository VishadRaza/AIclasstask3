# def greet(): #function definition
#     print("good morning")
#
# greet() # function call


# def add(a,b): # here a and b are parameters
#     s = a + b
#     return s
#
#
# def subtract(num1, num2):
#     print("Subtraction: ", str(num1-num2))
#
#
# def multiplication(a, b):
#     print("Multiplication: ", a*b)
#
#
# def division(num1, num2):
#     print("Division: ", num1/num2)
#
#
# a = int(input('Enter number 1 '))
# b = int(input('enter number 2 '))
# s = add(a,b) # passing data a, b are arguments
# print("addition: ",s)
# subtract(a,b)
# multiplication(a,b)
# division(a,b)

# def my_pet(owner, pet, city = "karachi"): # here city is default parameter
#     print(owner, "is an owner of ",pet, " they are from ", city)
#
#
# my_pet("Sarah", "Cat")  # position argument passing
#
# my_pet(pet="cat", owner="sarah")  # keyword argument passing
#
# my_pet(pet="cat", owner="Sarah", city="lahore")  # here city lahore will replace karachi

# 4 types of function
# takes nothing return nothing
# take some something return nothing
# takes nothing but return something
# takes some thing return something


# type 3 example


# def sum():
#     a = 5
#     b = 3
#
#     return a+b
#
#
# s = sum()
# print(s)

# type 4 example

#
# def sum(val1,val2):
#     result = val1+val2
#     return result
#
#
# a = int(input("enter 1st number "))
# b = int(input("enter 2nd number "))
#
# output = sum(a,b)
# print(output)

# def number_check(a):
#     if a%2 ==0:
#         s = 0
#     else:
#         s =1
#     return s
#
#
# a = int(input("enter number "))
# z = number_check(a)
# if z == 0:
#     print(a , " is an even number")
# else:
#     print(a, " is an odd number")

# -------x--------x-------

# def pizza(crust, *topping):  # *means multiple values single * means tupple
#    print("You have ordered a pizza with ",crust, " crust with a following topping ")
#    for each in topping:
#        print(each)
#
#
# pizza("Thick", "Green olives", "Chicken", "Black Olives")

# use of double *
#cannot use single * on two arguments at same time
# def pizza(crust, **topping): #double * means dictionaries
#     print("You have orderes a pizza with ",crust," crust with the following toppings ")
#     for key,value in topping.items():
#         print(key, ": ",value)
#
# pizza("Thick",topping1 ="Green Olives", topping2 = "Chicken", topping3 ="black olives")

def pizza(*crust, **topping): #double * means dictionaries
    print("You have orderes a pizza with ",crust," crust with the following toppings ")
    for value in topping.values():
        print(value)

pizza("Thick", "Thin",topping1 ="Green Olives", topping2 = "Chicken", topping3 ="black olives")

#factorial
#fabionnic

#make aa function that takes order of jewelley/ grocery and its quantity in second function calculate bill 2 types of bill first total amount and individual
#discount offer is bill is > 25000 25% discount <=15000 no discount if bill ?=50000 50% discount