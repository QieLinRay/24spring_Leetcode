def findDuplicate(nums: list[int]) -> int:
    left, right = 1, len(nums) - 1
    target = -1
    while left <= right:
        mid = (left + right) // 2
        count = sum(1 for num in nums if num <= mid)

        if count <= mid:
            left += 1
        else:
            right = mid - 1
            target = mid
    return target

def findDuplicate1(nums: list[int]) -> int:
    left,right = 1, len(nums) - 1
    target = -1
    while left <= right:
        mid = (left + right)//2
        count = sum(1 for num in nums if num <= mid)

        if count <= mid:
            left = mid + 1
        else:
            right = mid - 1
            target = mid
    return target


if __name__ == "__main__":
    nums = [1,2,3,4,5,2]
    a = findDuplicate(nums)
    print(a)


