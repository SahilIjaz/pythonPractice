num_1 = 2
num_2 = 3

sum = num_1 + num_2 
print('Sum is ',sum)


numOne = float( input ("Enetr a number:"))
numTwo = float( input ("Enter another number:"))
sum = numOne + numTwo
print('Sum of your enterred numbers is : ',int(sum))


print("Hello World! by Python program.")

print("Square root calculation question")
num = int(input("Enter the number to get square root:"))
sqr = num**(1/2)
print ("the square root of ",num,"is",sqr)

import math
numSimple = int(input("Enter a number to get square root:"))
sqr = math.sqrt(numSimple)
print("the square ropt of entered number is:",sqr)


print("Calculatioon of area of Triangle")
base = int(input('Enter the value of base:'))
length = int(input('Enter value of length:'))
height = int(input("Enter the value of heigth:"))
area = (1/2)*(length * height)
print("The area of triangle is :",area)


print('Swapinhg the two numbers.')
num1 = int( input('Enter a number:'))
num2 = int( input('Eneter another number:'))
num1 = num1 - num2 
num2 = num1 + num2
num1 = num2 - num1
print("The value of number 1 is:",num1)
print("Value of number 2 is:",num2)


print("Converting km to miles.")
km = int( input("Enetr the value of km:"))
miles = km * (0.62)
print("Miles are:",miles)



while True:
    print('checking is number positive, negative or zero')
    number = int( input("Eneter the number:"))

    if(number < 0):
        print("Number is negative.")
    elif (number > 0):
        print('Number is positive.')
    else:
        print('Number is 0.')
    a = input('Enetr a character')[0]
    if (a == 'a'):
        break

print("Checking if number is even or odd.")

while True:
    number = int( input("Enter a number:"))
    if(number % 2 == 0):
        print("Number si an even number.")
    else:
        print("Number is odd number.")
    a = input("enter s to stop:")[0]
    if(a == 's'):
        break


number = int( input('Enter a number:'))
print("Even" if (number%2 ==0) else 'Odd')

print("Checking leap year.")
while True:
    year = int( input('Enetr a year:'))
    print('Leap year' if (year % 4 == 0 ) else "Not a leap year")
    a = input('Enetr s to stop:')[0]
    if( a== 's'):
        break



print("Finding the largets number among three.")

while True:
    num1 = int( input('Enetr a number:'))
    num2 = int( input('Enter second number:'))
    num3 = int( input("Enetr last number:"))

    if(num1 > num2 and num1 > num3):
        print('num1 is largest.')
    elif(num2 > num1 and num2 > num3):
        print('num2 is largest.')
    elif(num3 > num2 and num3 > num1):
        print("num3 is largest.")
    else:
        print('num1, num2 and num3 are equal.')

    s = input('Enetr s to stop:')[0]
    if(s == 's'):
        break