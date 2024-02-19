numbers = [123, 5245634, 54, 6745674, 5745, 645, 64, 564, 576, 456, 456, 456, 34534, 135, 436476, 7586, 452, 34657]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(numbers)
print(numbers)
