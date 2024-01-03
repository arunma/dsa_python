from typing import List


def segregate_evens_and_odds(numbers):
    even_start = 0
    for i in range(len(numbers)):
        if not numbers[i] & 1:
            numbers[even_start], numbers[i] = numbers[i], numbers[even_start]
            even_start += 1
    return numbers


def segregate_evens_and_odds_dutch(nums: List[int]) -> List[int]:
    left = 0
    odd_start = 0
    right = len(nums) - 1

    while left <= right:
        val = nums[left]
        if val & 1:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            nums[left], nums[odd_start] = nums[odd_start], nums[left]
            odd_start += 1
            left += 1
    return nums


if __name__ == '__main__':
    print(segregate_evens_and_odds([1, 2, 3, 4]))  # 2,4,1,3
    print(segregate_evens_and_odds_dutch([1, 2, 3, 4]))  # 4,2,3,1
