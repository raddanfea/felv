my_arr = [0, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10]
target = 4
low = 0
high = len(my_arr) - 1
while low <= high:
    mid = (low + high) // 2
    if my_arr[mid] == target:
        print("Found target at:", mid)
        my_arr.remove(my_arr[mid])
    else:
        if my_arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
