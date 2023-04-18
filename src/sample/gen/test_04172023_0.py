def max_subarray_sum(nums):
    """
    Problem:

    Given a list of integers nums, return the maximum sum that can be obtained by choosing a contiguous subarray of nums and then multiplying each of its elements by its index in the subarray. If there are multiple subarrays with the same maximum sum, return the one with the smallest starting index.

    Example:

    Input: nums = [1, 2, 3, 4, 5]
    Output: 35
    Explanation: The maximum sum can be obtained by choosing the subarray [4, 5], which has a sum of 9, and then multiplying each of its elements by its index in the subarray, resulting in 4*1 + 5*2 = 14.

    Input: nums = [-1, -2, -3, -4, -5]
    Output: 0
    Explanation: All subarrays have a negative sum, so the result is 0.

    Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    Solution:

    The idea is to iterate through all possible subarrays, calculate their sum and multiply each element by its index, keeping track of the maximum sum and the corresponding subarray. To iterate through all possible subarrays, we use two nested loops to generate all pairs of starting and ending indices. To calculate the sum and multiply each element by its index, we use another loop. Finally, we return the maximum sum and the corresponding subarray.

    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """

    max_sum = 0
    max_subarray = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray_sum = 0
            for k in range(i, j + 1):
                subarray_sum += nums[k] * (k - i + 1)
            if subarray_sum > max_sum:
                max_sum = subarray_sum
                max_subarray = nums[i : j + 1]
    return max_sum, max_subarray


assert max_subarray_sum([1, 2, 3, 4, 5]) == (35, [4, 5])
assert max_subarray_sum([-1, -2, -3, -4, -5]) == (0, [])
assert max_subarray_sum([1, -2, 3, -4, 5]) == (10, [3, -4, 5])
