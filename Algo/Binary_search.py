def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)  

#find first and last postion of an element in a sorted array

def find_first_and_last(arr, target):
    def first_element():
        left,right=0,len(arr)-1
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]==target:
                right=mid-1
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
    def last_element():
        left,right=0,len(arr)-1
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]==target:
                left=mid+1
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return right
    return first_element(),last_element()

arr = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
target = 5
result = find_first_and_last(arr, target)
print(result)  
    
