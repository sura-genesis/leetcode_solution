def two_sum(nums, target):
    num_indices = {}  # Dictionary to store the indices of numbers

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            return [num_indices[complement], i]

        # Add the current number and its index to the dictionary
        num_indices[num] = i

    # If no solution is found
    return None

