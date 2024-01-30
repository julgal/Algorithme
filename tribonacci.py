def tribonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]

    nums = [0,1,1]
    while len(nums) < n:
        nums.append(sum(nums[-3:]))
    return nums
