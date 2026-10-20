### Q31. Calculate the Total Cost

# **Task:** A shop sells one notebook for `PRICE` rupees. Take the price of one notebook and the number of notebooks purchased, `QUANTITY`. Calculate the total cost using repeated addition.

# PRICE=int(input("enter the PRICE :"))
# QUANTITY=int(input("enter the QUANTITY :"))
# i=1
# total_cost=0
# while i<=QUANTITY:
#     total_cost+=PRICE
#     i+=1
# print(total_cost)



### Q32. Calculate Total Savings

# **Task:** A student saves the same amount of money every day. Take `DAILY_SAVING` and `DAYS`. Calculate the total amount saved after that many days using a loop.


# DAILY_SAVING=int(input("enter daily saving :"))
# DAYS=int(input("enter number of day saving :"))
# total_saving=0
# i=1
# while i<=DAYS:
#     total_saving+=DAILY_SAVING
#     i+=1
# print(total_saving)

### Q33. Calculate a Number Raised to a Power

# **Task:** Take two non-negative integers, `BASE` and `POWER`. Calculate `BASE` raised to `POWER` using repeated multiplication. Assume `POWER` is between `0` and `8`.


# BASE=int(input("enter base value :"))
# POWER=int(input("enter power value :"))
# i=1
# result=1
# while i<=POWER:
#     result*=BASE
#     i+=1
# print(result)
    

### Q34. Calculate Factorial

# **Task:** Take a non-negative integer `N` and calculate its factorial. The factorial of `N` is the product of all integers from `1` to `N`. Remember that `0! = 1`.

# n=abs(int(input("enter the value of N :")))
# i=1
# fac=1
# while i<=n:
#     fac*=i
#     i+=1
# print(fac)


### Q35. Find the Sum from START to END

# **Task:** Take two integers, `START` and `END`, where `START` is less than or equal to `END`. Calculate the sum of all integers from `START` through `END`, including both endpoints.


START=int(input("enter the start value :"))
END=int(input("enter the end value :"))
sum=0
while START<=END:
    sum+=START
    START+=1
print(sum)









