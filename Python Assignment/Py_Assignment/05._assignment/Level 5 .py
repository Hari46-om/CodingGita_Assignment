# ==============================================================
# Level 5 — String & Character Logic
# ==============================================================

## Q37. Print Characters with Index

# Take a string and print every character along with its index.

# str=input("enter the string :")
# for i in range (len(str)):
#     print(i,str[i])

## Q38. Count Characters Without `len()`

# Take a string and find its length without using `len()`. Use a `for` loop to count the characters.

# str=input("enter the string :")
# len=0
# for i in str:
#     len+=1
# print("output :",len)

## Q39. Count Vowels and Consonants

# Take a string containing English letters and spaces. Count vowels and consonants using one `for` loop. Ignore spaces.

# str=input("enter the string :")
# v=0
# c=0
# x="AEIOUaeiou"
# for i in str:
#     if i in x:
#         v+=1
#     elif " "!=i:
#         c+=1
# print(f"output : Vowels = {v}, Consonants ={c}")

## Q40. Character Frequency

# Take a string and a target character. Count how many times the target appears.

# str=input("enter the string :")
# x=input("enter the charcter to count :")
# count=0
# for i in str:
#     if i==x:
#         count+=1
# print("output :",count)

## Q41. First Occurrence Position

# Take a string and a target character. Find the index of the **first occurrence** of that character.
# If it does not occur, print `Not Found`.

# str=input("enter the string :")
# x=input("enter the string to find index of first occurrence :")
# l=0
# for i in range(len(str)):
#     if str[i]==x and l==0:
#         l+=1
#         print(i)
# if l ==0:
#     print("Not found")


## Q42. Count Uppercase and Lowercase

# Take a string containing English letters. Count uppercase and lowercase characters using one `for` loop.

# str=input("enter the string :")
# u=0
# l=0
# for i in str:
#     if 65<=ord(i)<=90:
#         u+=1
#     elif 97<=ord(i)<=122:
#         l+=1
# print(f"Output : Uppercase ={u}, Lowercase ={l}")

## Q43. Character Code Analyzer

# Take a string and print every character along with its Unicode value using `ord()`.

# str=input("enter the string :")
# for i in str:
#     print(i,ord(i))

## Q44. String Without Vowels

# Take a string and print all characters except vowels. Preserve the original order.

# str=input("enter the string :")
# v="AEIOUaeiou"
# for i in str:
#     if i not in v:
#         print(i,end='')
        
