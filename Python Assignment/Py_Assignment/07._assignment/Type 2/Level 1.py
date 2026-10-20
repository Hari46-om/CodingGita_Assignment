### Q21. Print Numbers from 1 to N

# **Task:** Take a positive integer `N` and print all numbers from `1` to `N`, each on a new line.

# n=int(input("enter N :"))
# i=1
# while i<=n:
#     print(i)
#     i+=1
    
### Q22. Print Numbers from N to 1

# **Task:** Take a positive integer `N` and print the numbers in descending order, from `N` to `1`.

# n=int(input("enter N :"))
# while n>=1:
#     print(n)
#     n-=1

### Q23. Print Even Numbers up to N

# **Task:** Take a positive integer `N` and print all even numbers from `2` up to `N`. If `N` is odd, stop at the last even number below it.

# n=int(input("enter N :"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1

### Q24. Print Odd Numbers up to N

# **Task:** Take a positive integer `N` and print all odd numbers from `1` up to `N`.

# n=int(input("enter N :"))
# i=1
# while i<=n:
#     if i%2!=0:
#         print(i)
#     i+=1
    
### Q25. Print Multiples of a Number

# **Task:** Take two positive integers, `K` and `N`. Print the multiples of `K` that are less than or equal to `N`.

k=int(input("enter the multiples :"))
n=int(input("enter N :"))
i=1
while i<=n:
    if i%k==0:
        print(i)
    i+=1