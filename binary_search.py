

def search_iterative1(arr, x):
    index = 0
    for index, y in enumerate(arr):
        if y == x:
            return index
        index += 1
    return -1;
    
def search_iterative2(arr, x):
    for index, y in enumerate(arr):
        if y == x:
            return index
    return -1;
    
def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
 
    return -1
    
def binary_search_recursive(arr, x):
    if len(arr) == 0:
        return -1;

    midindex = (len(arr) - 1) // 2
    if (arr[midindex] == x):
        return midindex
    elif arr[midindex] > x:
        return binary_search_recursive(arr[:midindex], x)
    elif arr[midindex] > x:
        return midindex + binary_search_recursive(arr[midindex + 1:], x)    
    else:
        return -1