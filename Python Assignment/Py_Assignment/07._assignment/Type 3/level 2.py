### Q46. Find the First and Last Digit

# **Task:** Take a positive integer and print its first digit and last digit on separate lines. The first digit is the leftmost digit.

# n=int(input("enter N :"))
# print("Last digit :",n%10)
# while n>0:
#     x=n%10
#     n//=10
# print("first digit :",x)

### Q47. Count Even Digits

# **Task:** Take a non-negative integer and count how many of its digits are even. Zero is an even digit.

# n=int(input("enter N :"))
# count=0
# if n==0:
#     count+=1
# while n>0:
#     x=n%10
#     if x%2==0:
#         count+=1
#     n//=10
# print(count)

### Q48. Count Odd Digits

# **Task:** Take a non-negative integer and count how many of its digits are odd.

# n=int(input("enter N :"))
# count=0
# while n >0:
#     x=n%10
#     if x%2!=0:
#         count+=1
#     n//=10
# print(count)
    
    
### Q49. Find the Sum of Even Digits

# **Task:** Take a non-negative integer and calculate the sum of only its even digits.

# n=int(input("enter N :"))
# sum=0
# while n>0:
#     x=n%10
#     if x%2==0:
#         sum+=x
#     n//=10
# print(sum)

### Q50. Find the Largest Digit

# **Task:** Take a non-negative integer and find the largest digit present in it.

# n=int(input("enter N :"))
# max=0
# while n>0:
#     x=n%10
#     if x>max:
#         max=x
#     n//=10
# print(max)

### Q51. Find the Smallest Digit

# **Task:** Take a non-negative integer and find the smallest digit present in it.

n=int(input("enter N :"))
min=9
while n>0:
    x=n%10
    if x<min:
        min=x
    n//=10
print(min)