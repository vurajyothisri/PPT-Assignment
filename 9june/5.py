def find_max(arr, n):
    if n == 0:
        return arr[0]
    else:
        return max(arr[n], find_max(arr, n - 1))


array = [1, 4, 3, -5, -4, 8, 6]
result = find_max(array, len(array) - 1)
print(result)
