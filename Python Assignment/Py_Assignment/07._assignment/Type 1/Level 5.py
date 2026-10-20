17.

# i = 1
# result = ""

# while i <= 4:
#     result += "A"
#     print(result)
#     i += 1
    
# output:A
#        AA 
#        AAA
#        AAAA

18.

# word = "PY"

# while len(word) < 6:
#     print(word)
#     word += "T"

# print(word)

# output:PY 
#        PYT
#        PYTT
#        PYTTT
#        PYTTTT

19.

# x = 3

# while x > 10:
#     print("Inside")
#     x += 1

# print(x)

# OUTPUT:3

20.

# The program prints 1 0 -1 -2 ... and continues indefinitely because i decreases by 1 each time the loop runs. Since i is always less than or equal to 4, the loop never stops, and "Finished" is never printed.

i = 1

while i <= 4:
    print(i, end=" ")
    i += 1

print("Finished")