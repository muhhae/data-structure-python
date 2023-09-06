def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def findMax(arr, left, right):
    # Base case: If there's only one element
    if left == right:
        return arr[left]

    # Base case: If there are two elements
    if right == left + 1:
        return max(arr[left], arr[right])

    # Recursive case:
    mid = (left + right) // 2
    leftMax = findMax(arr, left, mid)       # Find max in the left half
    rightMax = findMax(arr, mid+1, right)   # Find max in the right half

    return max(leftMax, rightMax)           # Return the overall max

def Cetak(a):
    if type(a) == int:
        print(a)
    elif type(a) == list:
        for e in a:
            Cetak(e)

l = [1, 2, [3, 4, 5], 5, [7, [8, 9], 3]]
Cetak(l)