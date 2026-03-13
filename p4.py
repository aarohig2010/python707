#check even odd order 
number = int(input("enter any number:"))
if number % 2==0:
   print("even number")
else:
     print("odd number")   
if number & 1==0:
    print("even")
if number %2 !=0:
    print("odd")         

    #find the largest of the three number 
    a,b,c  = 12,35,46
    if a>b and b>c: 
       print(b)
    if c>=a and c>=b:
       print ("c is greater", c)   

#find the factorial od the number 
n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("Factorial =", fact)
#multiplication table(1-10,11-20)
for i in range(1,11):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()

#(11-20) 
for i in range(11,21):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()
# fibbonacci series 
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
# armstrong number find
n = int(input("Enter number: "))
temp = n
sum = 0

while n > 0:
    r = n % 10
    sum = sum + r**3
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not Armstrong")
# prime number 
n = int(input("Enter number: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not prime")
# pallindrome number or string
n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome") 
  
        

