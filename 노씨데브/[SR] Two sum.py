'''

정수가 저장된 배열 nums이 주어졌을 때,
nums의 원소 중 두 숫자를 더해서 target이 될 수 있으면 True 불가능하면 False
같은 원소를 두 번 사용할 수 없습니다.

제약조건
1. 2 <= nums.length <= 10^4
2. -10^9 <= nums[i] <= 10^9
3. -10^9 <= target <= 10^9

'''

def sumsum(nums, target):
    return None

nums = [4, 1, 9, 7, 5, 3, 16]
target = 14
print(sumsum(nums, target))
# output = True

nums = [2, 1, 5, 7]
target = 4
print(sumsum(nums, target))
# output = False