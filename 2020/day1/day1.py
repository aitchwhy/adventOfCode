# Day 1, 2020

def solve(input_lines):

    print(f"######### Day 1")

    # read input
    input_nums = [int(elem) for elem in input_lines]

    # Find 2 entries summing to 2020
    sum_target = 2020

    # Find 2 vals sum to target
    seenVals = set()
    for n in input_nums:
        rem = (sum_target - n)
        if (rem in seenVals):
            print (n * rem) # 616 * 1404 = 864864
        seenVals.add(n)


    # sorted approach for 3 values
    sorted_input_nums = sorted(input_nums)
    for left_idx, left in enumerate(sorted_input_nums):
        mid_idx, right_idx = left_idx + 1, len(input_nums)-1
        while (mid_idx < right_idx):
            mid, right = sorted_input_nums[mid_idx], sorted_input_nums[right_idx]
            summed = left + mid + right
            if (summed == sum_target):
                print(left, mid, right)
                print(left * mid * right)
                mid_idx += 1
                right_idx -= 1
                exit
            elif (summed < sum_target):
                # too small summed
                mid_idx += 1
            else: # summed > sum_target
                right_idx -= 1