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





if __name__ == '__main__':
    arr = [1,37,3,12,45,6,8,13,55]
    print(mergesort(arr))