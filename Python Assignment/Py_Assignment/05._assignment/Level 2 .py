# ==============================================================
#  Level 2 — Counting & Accumulation
# ==============================================================

## Q7. Sum of Numbers in a Range

# Take `start` and `end`. Find the sum of all integers from `start` to `end` using one `for` loop.

# start=int(input("Enter starting value :"))
# end=int(input("Enter ending value :"))
# b=0
# for i in range (start,end+1):
#     b+=i
# print(b)

## Q8. Count Multiples of 3

# Take `N` and count how many numbers from `1` to `N` are divisible by `3`.

# n=int(input("enter the number :"))
# count=0
# for i in range (1,n+1):
#     if i%3==0:
#         count+=1
# print(count)


## Q9. Sum of Multiples of 4

# Take `N` and calculate the sum of all numbers from `1` to `N` divisible by `4`.

# n=int(input("enter the number :"))
# sum=0
# for i in range (1,n+1):
#     if i % 4 ==0:
#         sum+=i
# print("Output :", sum)

## Q10. Count Numbers with Two Conditions

# Take `N` and count numbers from `1` to `N` that are divisible by **both 3 and 5**.

# n=int(input("enter the number :"))
# count=0
# for i in range(1,n+1):
#     if i%3==0 and i%5==0 :
#         count+=1
# print(count)

## Q11. Sum Numbers Except Multiples of 3

# Take `N` and find the sum of numbers from `1` to `N` that are **not divisible by 3**.

# n=int(input("enter the number :"))
# sum=0
# for i in range(1,n+1):
#     if i%3!=0 :
#         sum+=i
#         print(i)
# print(sum)


## Q12. Count Even and Odd Together

# Take `N`. Using one loop, count how many numbers from `1` to `N` are even and how many are odd.

# n=int(input("enter the number :"))
# even=0
# odd=0
# for i in range (1,n+1):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"Output : Even = {even}, Odd = {odd}")


## Q13. Running Sum

# Take `N`. Print the running sum after every number from `1` to `N`.

# n=int(input("enter the number :"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print(sum)

## Q14. Running Product

# Take `N`. Starting with `1`, multiply by every number from `1` to `N` and print the product after each iteration.

# n=int(input("enter the number :"))
# multiply=1
# for i in range(1,n+1):
#     multiply*=i
#     print(multiply)

