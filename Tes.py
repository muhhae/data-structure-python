n = str(input())

num_count = [0] * 10

for e in n:
    if e.isnumeric():
        num_count[int(e)] += 1

for e in num_count:
    print(e, end=" ")