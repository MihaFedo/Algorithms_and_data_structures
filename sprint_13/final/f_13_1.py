def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif (
              nums[mid] < target 
              and (nums[right] >= target or nums[mid] >= nums[right])
              or (nums[left] > target and nums[mid] >= nums[left])
        ): 
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
