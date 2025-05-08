def linear_search(linear_list, target):
    for index in range(len(linear_list) - 1):
        if (target == linear_list[index]):
            return index
    return -1


arr = [12, 5, 7, 9, 3, 15, 2, 8, 6]
target = 9
print(linear_search(arr, target))
    