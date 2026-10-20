### Q26. Multiplication Table

# **Task:** Take an integer `N` and print its multiplication table from `N × 1` to `N × 10`.

# n=int(input("enter value of N :"))
# i=1
# while i<=10:
#     print(f"{n} x {i} = {n*i}")
#     i+=1
    
### Q27. Count by a Given Step

# **Task:** Take two positive integers, `START` and `STEP`. Starting from `START`, print the next five values, adding `STEP` after each value. Print exactly five numbers.

# START=int(input("enter START :"))
# STEP=int(input("enter STEP :"))
# i=1
# print(START)
# while i<5:
#     i+=1
#     print(START+STEP)
#     START+=STEP
    
    
### Q28. Sum of Numbers from 1 to N

# **Task:** Take a positive integer `N` and calculate the sum of all integers from `1` to `N`. Print only the final sum.


# n=int(input("enter the value of N :"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

### Q29. Sum of Even Numbers up to N

# **Task:** Take a positive integer `N` and calculate the sum of all even numbers from `2` up to `N`.

# n=int(input("enter the value of N :"))
# sum=0
# i=1
# while i<=n:
#     if (i%2==0):
#         sum+=i
#     i+=1
# print(sum)


### Q30. Sum of Odd Numbers up to N

# **Task:** Take a positive integer `N` and calculate the sum of all odd numbers from `1` up to `N`.

# n=int(input("enter the value of N :"))
# sum=0
# i=1
# while i<=n:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(sum)