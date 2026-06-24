class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        found = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                found = mid
                break

            elif target > nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        return found