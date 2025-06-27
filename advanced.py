print("Printing the power to the given limit")

import math
limit = int( input("Enter the limit: "))
number = int( input("Enter the number: "))

for i in range(limit):
    print("The powr is ",int(math.pow(number,i)))



print("Get all the number divisible")

startLimit = int( input("Enter the starting number: "))
lastNumber = int( input("Enter the last number: "))

number = int(input ("Enter the number: "))

for  i in range(startLimit,lastNumber+1):
    if int(i) % int(number)  == 0:
        print('Number is :',i)


print("Convert a number to binary, octal, hexadecimal")
decimal = int( input("Enter a number:"))
convert = int( input("Enter th ebase to be converted:"))

if convert == 2:
    answer = bin(decimal)
elif convert == 8:
    answer = oct(decimal)
elif convert == 16:
    answer = hex(decimal)

print("The number in demanded base is:",answer)

print('Convert ASCII values and numbers')
char = input("Enter the character:")
number = ord(char)
print('The number is: ',number)


print('Find HCF')
def findHcf(x,y):
    while y!=0:
        x,y =y, x%y
    return x

int1 = int( input('Entert first number: '))
int2 =int( input('Enter second number: '))
print('HCF is: ',findHcf(int1,int2))

print('Factors of a number')
number = int( input("Enter a number: "))
for i in range(1,number + 1):
    if number % i == 0:
        print(' ',i)


print('Simple calculator')
numberOne = int( input('Enter a number: '))
numberTwo = int( input("Enter another number: "))
operator = input('Enter operator: ')

if operator == '+':
    result = numberOne + numberTwo
elif operator == '-':
    result = numberOne - numberTwo
elif operator == '*':
    result = numberOne * numberTwo
elif operator == '/':
    result = numberOne / numberTwo
elif operator == '%':
    result = numberOne % numberTwo

print('Result is: ',result)


print('Shuffle deck of cards')
import random
import math
while True:
 a = input('Enter option: ')
 if a =='a':
     deck = random.randint(1,6)
     print('Dice has: ',deck)
 else:
   break

 

