arr = [7, 4, 3, 67, 34, 1, 8]


def bubble_sort(arr):
    n = len(arr)
    for j in range(0, n - 1):
        for i in range(0, n - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


bubble_sort(arr)
print(arr)  # [1, 3, 4, 7, 8]