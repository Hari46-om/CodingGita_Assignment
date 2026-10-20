# ==============================================================
# Level 8 — Real-Life Single-Loop Problems
# ==============================================================


## Q62. Daily Expense Analyzer

# Take the number of days and then enter the expense for each day. Using one `for` loop, calculate:

# - total expense
# - highest expense
# - lowest expense

# day=int(input("enter the number of days :"))
# hi=0
# low=None
# total=0
# for i in range(day):
#     n=int(input("enter the expenses  :"))
#     if n>hi:
#         hi=n
#     if i==0 or n<low :
#         low=n
#     total+=n
# print(f"total :{total}\nHighest :{hi}\nLowest :{low}")


## Q63. Student Marks Analyzer

# Take the number of subjects and enter marks one by one. Using one `for` loop, calculate:

# - total marks
# - average marks
# - highest marks
# - lowest marks

# n=int(input("enter the number of subject :"))
# total=0
# higest=0
# lowest=None
# for i in range (n):
#     m=int(input("enter the marks"))
#     total+=m
#     if m>higest:
#         higest=m
#     if i==0 or lowest>m:
#         lowest=m
# print(f"Total: {total}\nAverage: {total/n}\nHighest: {higest}\nLowest: {lowest}")


## Q64. Attendance Analyzer

# Take the number of working days. For each day, input `P` for Present or `A` for Absent. Count present days, absent days, and calculate attendance percentage.

# n=int(input("enter the number of working days :"))
# p=0
# a=0
# for i in range (n):
#     l=input("enter are you p or a :")
#     if l=="p":
#         p+=1
#     if l=="a":
#         a+=1
# print(f"present : {p}\nabsent :{a}\nAttendence :{(p/n)*100}%")


## Q65. Electricity Usage Analyzer

# Take the number of days and the electricity units used each day. Calculate total units and the number of days where usage was above `10` units.


# n=int(input("enter the number of days :"))
# count=0
# t=0
# for i in range (n):
#     u=int(input("enter the units used :"))
#     if u>10:
#         count+=1
#     t+=u
# print(f"Total Units : {t}\nDays Above 10 :{count}")

## Q66. Shopping Bill Analyzer

# Take the number of products and their prices. Using one `for` loop, calculate the total bill and count how many products cost more than `1000`.

# n=int(input("enter the number of products :"))
# total=0
# count=0
# for i in range (n):
#     c=int(input("enter the price of products :"))
#     if c>1000:
#         count+=1
#     total+=c
# print(f"Total Bills : {total}\nproducts Above 1000 :{count}")


## Q67. Login Attempt Analyzer

# Take `N` login attempts. For each attempt, input `success` or `failed`. Count successful and failed attempts and calculate the success percentage.


# n=int(input("enter the number of login attempts :"))
# s=0
# f=0
# for i in range(n):
#     a=input("enter result :")
#     if a=="success":
#         s+=1
#     if a=="failed":
#         f+=1
# print(f"Successful :{s}\nFailed :{f}\nSuccess Rate :{(s/n)*100}%")
