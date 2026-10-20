### Q36. Count Down by Two

# **Task:** Take a positive even integer `N`. Print numbers from `N` down to `2`, decreasing by `2` each time.

# n=int(input("enter the value of N :"))
# while n>0:
#     print(n)
#     n-=2

### Q37. Repeatedly Divide by Two

# **Task:** Take a positive integer `N`. Print the value of `N` after repeatedly applying integer division by `2`. Continue while the value is greater than `0`. Print each new value after dividing.

# n=int(input("enter the value of N :"))
# while n>0:
#     print(n//2)
#     n//=2
    
    
### Q38. Count How Many Steps Are Needed

# **Task:** Start with a positive integer `N`. In each step, subtract `3` from the number. Continue until the value becomes less than or equal to `0`. Print the number of steps taken.

# n=int(input("enter the value of N :"))
# count=0
# while 0<n:
#     n-=3
#     count+=1
# print(count)

### Q39. Save Until the Target Is Reached

# **Task:** A student already has `SAVED` rupees and adds `DAILY_AMOUNT` rupees each day. Calculate how many days are needed for the savings to become greater than or equal to `TARGET`. Assume `SAVED` is less than `TARGET` and `DAILY_AMOUNT` is positive.

# SAVED=int(input("enter saved value :"))
# DAILY_AMOUNT=int(input("enter daily amount value :"))
# TARGET=int(input("enter target value :"))
# day=0
# while TARGET>SAVED:
#     SAVED+=DAILY_AMOUNT
#     day+=1
# print(day)

### Q40. Print a Number Sequence in Reverse Steps

# **Task:** Take two positive integers, `START` and `STEP`, where `START` is divisible by `STEP`. Print values starting from `START`, subtracting `STEP` each time, and stop after printing `0`.

# START=int(input("enter the start value :"))
# STEP=int(input("enter the step value :"))
# print(START)
# while START-STEP>=0:
#     print(START-STEP)
#     START-=STEP

