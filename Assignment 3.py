# Assignment 3
## 1.Eligible for voting or not
age =int(input('enter your age'))
if age >=18:
    print ('you are eligible for vote')
else :
	print ('you are not eligible for vote')


## 2.Number is even or odd
num=int(input('enter the num'))
if num%2==0:
	print (f'the {num} is  even')
else:
	print(f'the {num} is odd')
	
	
## 3.Number is prime or not
n=int(input('enter the number'))
j=0
for i in range(2,n+1):
	
	if n%i==0:
		j+=1
	else:
		pass
if j==1:
	print(f'{n} is prime number')
else:
	print('not a prime number')
	

## 4.Number is positive or not
n=int(input('enter a number'))
if n>0:
	print(f'{n} is positive number')
else:
	print('negative number')

	
## 5.Quardatic equation
a=int(input('enter x**2 coefficent'))
b=int(input('enter x coefficent'))
c=int(input('enter the constant'))
d=b**2-(4*a*c)
if d==0:
	print(f'roots are equal they are : {(-b)/(2*a)}')
elif( d>0):
	print(f'roots are real and distent are : {(-b+(d**0.5))/(2*a)},{(-b-(d**0.5))/(2*a)}')
else:
    
    y=x=(-b)/(2*a)
    print(f'roots are imaginary they are {x}+{-(d/(2*a))}i and {y}-{-(d/(2*a))}i')
    
    

## 6.Number is positive or negative or zero
n=int(input('enter a number:'))
if n>0:
	print('number is positive ')
elif n==0:
	print('zero')
else:
	print('number is negative')


## 7.print the number in words
x={1:"one",2:"two",3:"three",4:"four",5:"five"}
p=[1,2,3,4,5]
n=int(input('enter the number in between 1-5'))
if (n in p):
	print(f'number in words is {x[n]}')
else:
	print('the nunber is not in between 1-5 try again')
	
	

## 8.vowel or consonant
a=str(input('enter a character A-Z')).lower()
if a in ['a','e','i','o','u']:
	print(f'{a} is an vowel')
else:
	print(f'{a} is a consonant')

	