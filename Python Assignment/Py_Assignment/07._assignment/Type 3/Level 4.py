### Q56. Print Factorial Values from 1! to N!

# **Task:** Take a positive integer `N`. Print the factorial value for every number from `1` to `N`, one result per line. Use one loop and update the factorial result as the number increases.

# n=int(input("enter :"))
# fac=1
# i=1
# while n>=i:
#     fac*=i
#     print(fac)
#     i+=1
    
    
### Q57. Check Whether a Number Is a Factorial Value

# **Task:** Take a positive integer `N`. Print `Yes` if `N` is equal to the factorial of some non-negative integer; otherwise, print `No`. Examples of factorial values are `1`, `2`, `6`, `24`, and `120`.
    
    
# n=int(input("enter :"))
# fact=1
# i=1
# c=0
# while n>=i:
#     fact*=i
#     if fact==n:
#         c+=1
#     i+=1
# if c>=1:
#     print("yes")
# else:
#     print("No")


### Q58. Find the Largest Factorial Not Greater Than N

# **Task:** Take a positive integer `N`. Find the largest factorial value that is less than or equal to `N`. Consider `1` as the starting factorial value.


# n=int(input("enter :"))
# fac=1
# i=1
# max=0
# while n>=i:
#     fac*=i
#     if n>=fac:
#         if max<fac:
#             max=fac
#     i+=1
# print(max)
        