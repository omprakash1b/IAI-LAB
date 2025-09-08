
def binary_search(arr, low,high,target):
    mid = (low + high) // 2
    if low > high:
        return -1
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)
    



if __name__ == "__main__":
    arr = [7,56,89,15,65,2,0,9,87,12,5,890, 9, 8, 769,87,34,987]
    val = binary_search(arr,0,len(arr)-1,87)
    print(val)