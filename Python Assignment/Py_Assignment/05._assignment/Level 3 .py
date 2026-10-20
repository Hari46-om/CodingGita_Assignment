# ==============================================================
# Level 3 — Factorial & Product Logic
# ==============================================================

## Q15. Factorial of a Number

# Take an integer `N` and calculate `N!` using a `for` loop.

# n=int(input("enter the number :"))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

# Q16. Factorial from 1 to N

# Take `N` and print the factorial of every number from `1` to `N`

# n=int(input("enter the number :"))
# factorial=1
# for i in range (1,n+1):
#     factorial*=i
#     print(f"{i}! = {factorial}")

## Q17. Product of Even Numbers

# Take `N` and find the product of all even numbers from `2` to `N`.

# n=int(input("enter the number :"))
# product=1
# for i in range (2,n+1):
#     if i%2==0:
#         product*=i
# print("output :",product)


## Q18. Product of Odd Numbers

# Take `N` and find the product of all odd numbers from `1` to `N`. 

# n=int(input("enter the number :"))
# product=1
# for i in range(1,n+1):
#     if i%2!=0:
#         product*=i
# print("output :",product)  

## Q19. Double Factorial — Even Numbers

# Take an even number `N`. Calculate:
# `N × (N-2) × (N-4) × ... × 2`
# Use one `for` loop.

# n=int(input("enter the number :"))
# factorial=1
# for i in range (1,n+1):
#     if i%2==0:
#         factorial*=i
# print(factorial)
    
   
## Q20. Sum of Squares

# Take `N` and calculate:
# `1² + 2² + 3² + ... + N²` 

# n=int(input("enter the number :"))
# sum=0
# for i in range(1,n+1):
#     sum+=i**2
# print(sum)  
  

## Q21. Sum of Cubes

# Take `N` and calculate:
# `1³ + 2³ + 3³ + ... + N³`

# n=int(input("enter the number :"))
# sum=0
# for i in range (1,n+1):
#     sum+=i**3
# print(sum)

## Q22. Factorial-Based Sum

# Take `N` and calculate:
# `1! + 2! + 3! + ... + N!`
# Use only one `for` loop.

# n=int(input("enter the nuber :"))
# x=1
# sum=0
# for i in range (1,n+1):
#     x*=i
#     sum+=x
# print(sum)
