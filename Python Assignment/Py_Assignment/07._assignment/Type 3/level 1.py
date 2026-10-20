### Q41. Count the Digits

# **Task:** Take a non-negative integer `N` and count how many digits it contains. Treat `0` as a one-digit number.

# n=int(input("enter :"))
# count=0
# if n==0:
#     count+=1
# while n>0:
#     count+=1
#     n//=10
# print(count)

### Q42. Find the Sum of Digits

# **Task:** Take a non-negative integer and calculate the sum of its digits.

# n=int(input("enter N :"))
# sum=0
# while n>0:
#     x=n%10
#     sum+=x
#     n//=10
# print(sum)

### Q43. Reverse a Number

# **Task:** Take a non-negative integer and print its digits in reverse order as a number. Leading zeroes in the reversed result are not displayed.

# n=int(input("enter N :"))
# rev=0
# while n>0:
#     x=n%10
#     rev*=10
#     rev+=x
#     n//=10
# print(rev)

### Q44. Find the Product of Digits

# **Task:** Take a non-negative integer and calculate the product of all its digits. The product of the digits of `0` is `0`.

# n=int(input("enter N :"))
# product=1
# if n==0:
#     product=0
# while n>0:
#     x=n%10
#     product*=x
#     n//=10
# print(product)


### Q45. Print Digits from Right to Left

# **Task:** Take a positive integer and print one digit per line, starting from the rightmost digit and moving left.


n=int(input("enter N :"))
while n>0:
    x=n%10
    print(x)
    n//=10
    