# ==============================================================
# Level 6 — Midpoint, Half & String Logic
# ==============================================================

## Q45. Find the Middle Character

# Take a string and find its middle character using its length and indexing.
# For this question, assume the string length is odd.

# str=input("enter the string :")
# m=len(str)
# for i in range(len(str)):
#     if i==m//2:
#         print(str[i])

## Q46. First Half and Second Half

# Take a string with an even number of characters. Find and print its first half and second half.

# str=input("enter the string with even character ")
# k=len(str)
# f=""
# l=""
# for i in range (k):
#     if k//2 > i:
#         f+=str[i]
#     else:
#         l+=str[i]
# print(f"output:\nfirst half \t:{f}\nsecond half \t:{l}")

## Q47. Split a String by Length — Odd vs Even

# Take a string as input.

# Use the string length and a **single `for` loop** to divide the string into halves.

# - If the length is **odd**:
#   - Print the first half.
#   - Print the middle character.
#   - Print the second half.
# - If the length is **even**:
#   - Print the first half.
#   - Print the second half.
# - Do not use slicing to directly obtain the final halves.
# - Use one `for` loop for the character-processing logic.


# str=input("enter the string :")
# m=""
# l=""
# f=""
# for i in range(len(str)):
#     if len(str)%2==0:
#         if len(str)//2 > i:
#             f+=str[i]
#         else:
#             l+=str[i]
#     else:
#         if len(str)//2>i:
#             f+=str[i]
#         elif len(str)//2==i:
#             m+=str[i]
#         else:
#             l+=str[i]
# if len(str)%2==0:
#     print(f"Output : \nFirst Half :{f}\nSecond Half :{l}")
# else:
#     print(f"Output : \nFirst Half :{f}\nMiddle :{m}\nSecond Half :{l}")
    
            
## Q48. Compare Two Halves

# Take a string of even length. Split it logically into two equal halves and check whether both halves are identical.
# Use one `for` loop.

# str=input("enter the string of even length :")
# f=""
# l=""
# for i in range(len(str)):
#     if len(str)//2>i:
#         f+=str[i]
#     else:
#         l+=str[i]
# if l==f:
#     print("equals halves")
# else:
#     print("Differnt Halves")


## Q49. Mirror the String

# Take a string and determine whether its first and last characters match, second and second-last match, and so on.
# Print `Symmetric` if all corresponding characters match; otherwise print `Not Symmetric`.
# Use one `for` loop.

# str=input("enter the string :")
# le=len(str)
# x=False
# for i in range (le//2):
#     if str[i]!=str[(le-1)-i]:
#         x=True
# if x==False:
#     print("Symmetric")
# else:
#     print("Not Symmetric")

## Q50. Alternate Character Extraction

# Take a string and print characters at even indexes only.

# str=input("enter the string :")
# for i in range (len(str)):
#     print("Output:",end='')
#     if i%2==0:
#         print(str[i],end='')

## Q51. Count Characters at Even and Odd Indexes

# Take a string and count how many characters occur at even indexes and how many occur at odd indexes.

# str=input("enter the string :")
# o=0
# e=0
# for i in range(len(str)):
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print(f"Output : Even Index ={e}, Odd Index ={o}")

## Q52. Swap Adjacent Characters

# Take a string with an even number of characters. Print the string after swapping every adjacent pair.

# str=input("enter the even character :")
# new=""
# for i in range (len(str)):
#     if i%2==0:
#         new+=str[i+1]
#         new+=str[i]
# print(new)
