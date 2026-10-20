### Q52. Check Whether a Number Is a Palindrome

# **Task:** A number is a palindrome if it reads the same from left to right and right to left. Take a non-negative integer and print `Palindrome` or `Not Palindrome`. Do not convert the number to a string.

# n=int(input("enter N :"))
# b=n
# rev=0
# while n>0:
#     x=n%10
#     rev*=10
#     rev+=x
#     n//=10
# if rev == b :
#     print("palindrome number")
# else:
#     print("Not palindrom")
    
    
### Q53. Count How Many Times a Digit Appears

# **Task:** Take a non-negative integer `N` and a digit `D` from `0` to `9`. Count how many times digit `D` appears in `N`.


# n=int(input("enter N :"))
# d=int(input("enter the digit :"))
# count=0
# if n==d==0:
#     count+=1
# while n>0:
#     x=n%10
#     if x==d:
#         count+=1
#     n//=10
# print(count)


### Q54. Check Whether All Digits Are the Same

# **Task:** Take a positive integer and print `Yes` if every digit is the same; otherwise, print `No`.

# n=int(input("enter :"))
# s=n%10
# l=0
# a=0
# while n>0:
#     x=n%10
#     l+=1
#     if x==s:
#         a+=1
#     n//=10
# if l==a:
#     print("yes")
# else:
#     print("No")
    
    
### Q55. Compare the Sum of First and Last Digits with the Middle Digits' Sum

# **Task:** Take a positive integer with at least three digits. Find the sum of its first and last digits. Separately, find the sum of all digits between the first and last digits. Print both sums on separate lines. Do not convert the number to a string.


n=int(input("enter :"))
last =n%10
b=n//10
sum=0
while b>0:
    x=b%10
    sum+=x
    b//=10
first=x
print(f"First and last sum : {last+first}")
print(f"Middle digit sum {sum -first}")