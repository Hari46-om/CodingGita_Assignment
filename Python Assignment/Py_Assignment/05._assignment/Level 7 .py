
# ==============================================================
# Level 7 — Tricky Single-Loop Problems
# ==============================================================

## Q53. Second Largest Digit

# Take a number and find the **second largest distinct digit** using one `for` loop.
# Do not use `sort()`, `max()`, or convert the number to a string.

# n=int(input("enter the number :"))
# max=0
# s=0
# import math
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     if x>max :
#        s=max
#        max=x
#     elif x>s and x<max:
#        s=x
#     n//=10
# print("second largest number :", s)

## Q54. Longest Consecutive Equal Character Run

# Take a string and find the length of the longest consecutive run of the same character.


# str=input("enter :")
# best_count=0
# count=1
# for i in range (1,len(str)):
#     # x=str[0]
#     if str[i]==str[i-1]:
#         count+=1
#     else:
#         count=1
#     if count>best_count:
#         best_count=count
# print(best_count)
    
    
## Q55. Most Frequent Character — Controlled Approach

# Take a string and a target character. Count how many times the target occurs and compare it with the number of characters in the string to determine its frequency percentage.

# str=input("enter :")
# letter=input("enter letter to search :")
# count=0
# for i in str :
#     if i==letter:
#         count+=1
# print(f"count :{count} ,frequency ={(count/len(str))*100}%")    


## Q56. Running Digit Sum Until the End

# Take a positive integer. Process its digits from right to left and print the running sum after each digit is processed.

# n=abs(int(input("enter N :")))
# import math
# count=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     count+=x
#     n//=10
#     print(count)


## Q57. Number with Most Even Digits

# Take a positive integer and determine whether it contains more even digits or more odd digits.


# n=int(input("enter :"))
# import math
# o=0
# e=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     if x%2==0:
#         e+=1
#     else:
#         o+=1
#     n//=10
# if e>o:
#     print("More even digit")
# elif e==o:
#     print("equal")
# else:
#     print("More odd digit")


## Q58. Alternating Digit Sum

# Take a positive integer. Starting from the **rightmost digit**, add the 1st digit, subtract the 2nd digit, add the 3rd digit, subtract the 4th digit, and continue this pattern.

# n=abs(int(input("input :")))
# count=0
# import math
# final=0
# for i in range(int(math.log10(n)+1)):
#     x=n%10
#     count+=1
#     if count%2==0:
#         final-=x
#     else :
#         final+=x
#     n//=10
# print(final)


## Q59. Output Prediction — Accumulator Trap


# total = 0
# for i in range(1, 6):
#     total = total + i * 2
#     print(total)
    
# output:2
#        6
#        12
#        20
#        30
       
       
## Q60. Output Prediction — Condition Inside Loop

# Predict the output:

# count = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         count = count + 1
# print(count)

# output:5 because it will show the final output of code it will count +1 when it is even 


## Q61. Debug the Accumulator

# The following program is intended to calculate `1 + 2 + 3 + 4 + 5`, but it is incorrect:

# sum = 0
# for i in range(1, 6):
#     sum += i
# print(sum)

# in evey iteration sum of i 
