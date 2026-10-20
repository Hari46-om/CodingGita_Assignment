# ==============================================================
# Level 9 — Final Challenges
# ==============================================================


###Q68. Number Profile

# Take a positive integer and, using exactly one `for` loop, find all of the following:

# - number of digits
# - sum of digits
# - largest digit
# - smallest digit
# - number of even digits
# - number of odd digits

# Do not convert the number to a string. Do not use `max()` or `min()`.


# n=int(input("enter the number :"))
# d=0
# s=0
# l=0
# sm=9
# e=0
# o=0
# import math
# for i in range (int(math.log10(n)+1)):
#     x=n%10
#     if x>l:
#         l=x
#     if sm>x:
#         sm=x
#     if x%2==0:
#         e+=1
#     else:
#         o+=1
#     d+=1
#     s+=x
#     n//=10
# print(f"Digits : {d}\nSum : {s}\nLargest : {l}\nSmallest : {sm}\nEven Numbers : {e}\nOdd Digits : {o}")


## Q69. String Balance Challenge

# Take a string containing letters. Using exactly one `for` loop, calculate:

# - total characters
# - vowels
# - consonants
# - uppercase characters
# - lowercase characters
# - characters at even indexes

# Ignore spaces when counting vowels/consonants/uppercase/lowercase, but include them in total characters and index positions.


# str=input("enter the string :")
# t,v,c,u,l,e=0,0,0,0,0,0
# k="aeiouAEIOU"
# for i in range (len(str)):
#     p=ord(str[i])
#     t+=1
#     if p>=65 and p<=90:
#         if str[i] in k:
#             v+=1
#         else:
#             c+=1
#         u+=1
#     if p>=97 and p<=122:
#         if str[i] in k:
#             v+=1
#         else:
#             c+=1
#         l+=1
#     if i%2==0:
#         e+=1
# print(f"Total Characters: {t}\nVowels: {v}\nConsonants: {c}\nUppercase: {u}\nLowercase: {l}\nEven Index Characters: {e}")
