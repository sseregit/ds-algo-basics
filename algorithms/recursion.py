def sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_recursive(lst[1:])


lst = [1, 2, 3, 4, 5]
print(sum_recursive(lst))


def binary_search(arr, target, low, high):
    if low > high:
        return -1
    center = (high + low) // 2
    result = arr[center]
    if target == result:
        return center
    elif target > result:
        return binary_search(arr, target, center+1, high)
    else:
        return binary_search(arr, target, low, center)


sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]

target = 99
result = binary_search(sorted_array, target, 0, len(sorted_array) - 1)
print(f"요소 {target}은 인덱스 {result}에 있습니다.")


