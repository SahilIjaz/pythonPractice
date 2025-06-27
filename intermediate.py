print('Prioma number in python')
import math
num =int(input("Enter a number:"))
i=1
if(num == 1 or num ==2 ):
    print("Prime number")
else:
    for i in range (2, int(math.sqrt(num))+1):
        if(num%i==0):
            print("Composite number")
        else:
            print("Prme number.")


print("Program to print random number")
import random
startNum= int(input("Enetr the starting number:"))
endNum = int(input('Enetr the ending number:'))
num=random.randint(startNum,endNum)
print("The number between range is:",num)


print("All prime numbers")
import math
limit =  int(input('Enetr the limit:'))
for i in range(2,limit+1):
    isPrime = True
    for j in range (2,int(math.sqrt(i))+1):
        if i%j ==0:
            isPrime = False
            break
    if isPrime:
        print("Prime number is:",i)


print ("Convert celcius to fahrenheite")
celcius = int( input("Enter temparature in celcius:"))
faran = (celcius * (9/5)) + 32
print("Temparatue in Fahrenheite is:",faran,'F')


print("Factorial of a number:")
number = int( input("Enetr a number:"))
fact = 1
for i in range(1,number+1):
    fact = fact * i
print("Factorial of",number,"is",fact)


print("Display the multiplication table")
number = int( input("Enetr the number:"))
limit = int( input("Eneter the limit:"))

for i in range (1,limit+1):
    print(number, "x" ,i, "=" ,number * i)


print("Display the Faibonacci series.")
number = int( input("Enetr the number:"))

print(0," ")
print(1," ")
num = 1
i = 1 
while num < number:
    num = i + num
    j = i
    if num >= number:
        break
    print(num," ")
    i = num 
    num = j


print("Armstrong number")
number = input("enter a number:")
reversed = number[::-1]
if number == reversed:
    print("Armstrong number")
else:
    print("Not an armstring number")

        
print("Sum of natural numbers")
limit = int( input("Enter the last digit:"))
sum = 0
for i in range(0,limit +1):
    sum += i
print("Sum of natural numbers to limit is:",sum)
    


   
    