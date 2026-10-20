# ==============================================================
# Level 4 — Number & Digit Logic
# ==============================================================

## Q23. Count Digits Using a Loop

# Take a positive integer and count its digits using a `for` loop. Do not convert the number to a string.

# import math
# n=int(input("enter the number :"))
# count=0
# for i in range(int(math.log10(n))+1):
#     x=n%10
#     count+=1
#     n//=10
# print(count)


## Q24. Sum of Digits

# Take an integer and find the sum of its digits using one `for` loop.

# n=int(input("enter the number :"))
# import math
# sum=0
# for i in range (int(math.log10(n)+1)):
#     x=n%10
#     sum+=x
#     n//=10
# print(sum)

## Q25. Product of Digits

# Take an integer and find the product of its digits.

# n=int(input("enter the number :"))
# import math
# product=1
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     product*=x
#     n//=10
# print(product)

## Q26. Count Even Digits

# Count how many digits of a given integer are even.

# n=int(input("enter the number :"))
# import math 
# count=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     if x%2==0:
#         count+=1
#     n//=10
# print(count)

## Q27. Sum of Even Digits

# Find the sum of only the even digits of a number.

# n=int(input("enter the number"))
# import math
# sum=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     if x%2==0:
#         sum+=x
#     n//=10
# print(sum)

## Q28. Largest Digit Without `max()`

# Find the largest digit of a number using one `for` loop. Do not use `max()` and do not convert the number to a string.

# import math
# n=abs(int(input("enter the number :")))
# max=0
# for i in range (int(math.log10(n)+1)):
#     x=n%10
#     if x>max:
#         max=x
#     n//=10
# print(max)

## Q29. Smallest Digit Without `min()`

# Find the smallest digit of a number using one `for` loop. Do not use `min()`.

# import math
# n=abs(int(input("enter the number :")))
# min=n%10
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     if x<min:
#         min=x
#     n//=10
# print(min)

## Q30. Reverse a Number

# Reverse the digits of a positive integer using one `for` loop and `%` / `//`.

# import math 
# n=abs(int(input("enter the number :")))
# r=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     r*=10
#     r+=x
#     n//=10
# print(r)    


## Q31. Palindrome Number

# Check whether a number reads the same from left to right and right to left. Use one `for` loop.

# import math
# n=int(input("enter the number :"))
# o=n
# r=0
# for i in range (int(math.log10(n)+1)):
#     x=n%10
#     r*=10
#     r+=x
#     n//=10
# if o==r:
#     print("Palindrome")
# else:
#     print("Not Palindrom")


## Q32. Count a Specific Digit

# Take an integer and a target digit. Count how many times that digit occurs.

# n=int(input("enter the number :"))
# x=int(input("enter the number to be count :"))
# count=0
# import math
# for i in range (int(math.log(n)+1)):
#     y=n%10
#     if y==x:
#         count+=1
#     n//=10
# print("Output :",count)
   

## Q33. First Digit Using Repeated Division

# Find the first/leftmost digit of a positive integer using a `for` loop and repeated integer division. Do not convert the number to a string.

# import math
# n=int(input("enter the number :"))
# for i in range (int(math.log10(n)+1)):
#     x=n%10
#     n//=10
# print(x) 

## Q34. Difference Between Largest and Smallest Digit

# Find the largest digit and smallest digit of a number, then print their difference. Do not use `max()` or `min()`.

# import math
# n=int(input("enter the number :"))
# min=9
# max=0
# for i in range (int(math.log10(n)+1)):
#     x=n%10
#     if x>max:
#         max=x
#     if x<min:
#         min=x
#     n//=10
# print("output :",max-min)

## Q35. Digit Position Value

# Take a positive integer and print each digit with its position from the right, starting from position `1`.

# import math
# n=int(input("enter the number :"))
# for i in range (1,int(math.log10(n)+2)):
#     x=n%10
#     n//=10
#     print(x," ",i)

## Q36. Armstrong Number — 3 Digit

# Take a 3-digit number and check whether it is an Armstrong number.

# import math
# n=int(input("enter the three digit number :"))
# o=n
# sum=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     sum+=x**3
#     n//=10
# if sum==o:
#     print("armstrong number")
# else:
#     print("not a armstrong number")
