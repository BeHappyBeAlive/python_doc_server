from typing import List


class Solution:
    # 88. 合并两个有序数组
    # 采用逆向双指针法
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tail = m + n - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] >= nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1

    # 采用正向双指针法
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        sorts = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorts.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorts.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                sorts.append(nums1[p1])
                p1 += 1
            else:
                sorts.append(nums2[p2])
                p2 += 1
        nums1[:] = sorts

    # 27.移除元素
    # 正向双指针
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

    # 逆向双指针
    def removeElement1(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

    # 26.删除排序数组中的重复项
    # 双指针
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
