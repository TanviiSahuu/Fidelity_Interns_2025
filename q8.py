#Create function which bubblesort and sequen_search write time decorator to find time for both.

import time

def time_decorator(func):
    def wrapper(*x, **y):
        start = time.time()
        result = func(*x, **y)
        end = time.time()
        print(f"Total time: {end - start} seconds")
        return result
    return wrapper

@time_decorator
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


@time_decorator
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr.copy())
index = linear_search(arr, 22)

print("Sorted List:", sorted_arr)
print("Element found at index:", index)