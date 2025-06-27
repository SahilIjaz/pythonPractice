# print("Printing the power to the given limit")

# import math
# limit = int( input("Enter the limit: "))
# number = int( input("Enter the number: "))

# for i in range(limit):
#     print("The powr is ",int(math.pow(number,i)))



print("Get all the number divisible")

startLimit = int( input("Enter the starting number: "))
lastNumber = int( input("Enter the last number: "))

number = int(input ("Enter the number: "))

for  i in range(startLimit,lastNumber+1):
    if int(i) % int(number)  == 0:
        print('Number is :',i)
