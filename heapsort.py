# heapify
# modify the binary tree to become a max-heap

def heapify(arr, n, i):
    # find largest among root and children
    largest = i  # i starts with 0
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[i] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
for i in range(n):
    print(arr[i])

# priority queue

# Insert(S, x)

# Maximum(S)
# Extract-Max(S)




