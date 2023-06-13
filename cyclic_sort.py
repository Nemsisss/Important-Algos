def cyclic_sort(nums):
# O(n) time complexity
    i = 0
    while i < len(nums):
        # Check if the current element is in its correct position
        if nums[i] != i + 1:
            # Swap the element with the value at its correct position
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    return nums
