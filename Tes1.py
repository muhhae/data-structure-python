max = int(input())
min = max

for i in range(max):
    a = max
    for j in range(max):
        print(a, end=" ")
        if a > min : a -= 1

    for j in range(2, max + 1):
        if j < min : print(min, end=" ")
        else : print(j, end=" ")
    min -= 1
    print()

min += 2
for i in range(1, max):
    a = max
    for j in range(max):
        print(a, end=" ")
        if a > min : a -= 1

    for j in range(2, max + 1):
        if j < min : print(min, end=" ")
        else : print(j, end=" ")

    min += 1
    print()