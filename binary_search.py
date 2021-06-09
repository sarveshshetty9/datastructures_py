
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

arr = [1,2,3,4,5,6,7]
target = 6
print(binary_search(arr, target))
