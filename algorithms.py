"""
O(nlogn)
"""
def mergesort(nums):
    if len(nums) > 1:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        left = mergesort(left)
        right = mergesort(right)

        i = 0
        j = 0

        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                    merged.append(left[i])
                    i+=1
            else:
                if j < len(right):
                    merged.append(right[j])
                    j+=1
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])
        return merged
    return nums


"""
Average time complexity: O(nlogn)
Worst case time complexity: O(n^2)
Requires extra space
"""
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = len(nums)//2
    left = []
    right = []

    for i in range(len(nums)):
        if nums[i] < nums[pivot]:
            left.append(nums[i])
        if nums[i] > nums[pivot]:
            right.append(nums[i])

    return quicksort(left) + [pivot] + quicksort(right)


"""
Average time complexity: O(nlogn)
Worst case time complexity: O(n^2)
In place sorting
"""
def quicksort2(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort2(arr, left, pivot-1)
        quicksort2(arr, pivot+1, right)

def partition(arr, left, right):
    i = left
    j = right-1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i+=1
        while j > left and arr[j] >= pivot:
            j-=1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
memo = {0:0, 1:1}
def fib(num):
    if num in memo:
        return memo[num]
    
    ans = fib(num-1) + fib(num-2)
    memo[num] = ans
    return ans




if __name__ == '__main__':
    arr = [1,5,5,3,4,5,5,2,2,3,4,2,2,1,1,1,2,2,3,3,4,5]
    # quicksort2(arr, 0, len(arr)-1)
    # print(arr)

    print(fib(29))