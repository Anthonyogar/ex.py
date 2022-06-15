
# for i in range(4):
   # name = input("Enter your name: ")
   # age = int(input("Enter age: "))
   # print(f"Hello, {name}; you are {age} years old")


# def greet_user():
    # name = input("Enter your name: ")
    # age = int(input("Enter age: "))
    # print(f"Hello, {name}; you are {age} years old")
    
    
# def get_sum():
    # num1 = int(input("Enter first value: "))
   # num2 = int(input("Enter second value: "))
    
   # print(f"{num1} + {num2} = {num1 + num2}")
    
# write a programme, asking the user the user to enter two
# numbers and printing the greater

# def print_greater():
  #  num1 = int(input("Enter first value: "))
  #  num2 = int(input("Enter second value: "))
   # num3 = int(input("Enter third value: "))
    # num4 = int(input("Enter fourth value: "))
    # num5 = int(input("Enter fifth value: "))
    # greater = num1
    
   # if num2> greater:
        # greater = num2 
    # if num3 > greater:
       # greater = num3
   #  if num4 > greater:
      # greater = num4
   # if num5 > greater:
     #  greater = num5
       
   # print(greater)    
    
# print_greater()

# get_sum
# greet_user

# write a python function to sum all the numbers in a list





from unittest import result


def print_greater():
    num1 = int(input("Enter first value: "))
    num2 = int(input("Enter second value: "))
    num3 = int(input("Enter third value: "))
    num4 = int(input("Enter fourth value: "))
    num5 = int(input("Enter fifth value: "))
    greater = num1 
    
    
    if num2> greater:
        greater = num2 
    if num3 > greater:
        greater = num3
    if num4 > greater:
        greater = num4
    if num5 > greater:
       greater = num5
       
    print(greater)    
    
print_greater()

# write a python function to multiply all the numbers in a list

def sum_of_list(num):
    ls_numbers = [2,4,6,8,10]
    result = 0
    for num in ls_numbers:
        result += num
    
    print(result)
sum_of_list

def prod_list(num):
    num = [2,4,6,8,10]
    result = 2
    for num in num:
        result *= num
    print(result)    
prod_list("num")
