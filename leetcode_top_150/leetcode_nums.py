import random
from typing import List
import collections


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
        index = 0
        for elem in sorts:
            if index >= len(nums1):
                return
            nums1[index] = elem
            index += 1

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

    def removeDuplicates1(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow, fast = 2, 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

    # hash表的方式
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 先排序后拿值的方式
    def majorityElement1(self, nums: List[int]) -> int:
        nums.sort()
        # // 双斜杠除法属于整数除法，保留整数
        # / 单斜杠触发属于浮点数触发，结果保留小数
        return nums[len(nums) // 2]

    # 基于上面方法的基础，先随机拿数组中的一个值，然后认为他就是数组中出现超过n/2的元素，然后去验证他是不是超过n/2
    # 如果不满足，继续枚举下一个元素，不过这种算法可能陷入死循环，是最不好的情况
    def majorityElement2(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            sum = 0
            for num in nums:
                if num == candidate:
                    sum += 1
            if sum > majority_count:
                return candidate

    # Boyer-Moore 投票算法
    def majorityElement3(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    # 168.轮转数组(https://leetcode.cn/problems/rotate-array/)
    # 使用额外的数组
    def rotate(self, nums, k):
        n = len(nums)
        new_arr = [0] * n
        for i in range(n):
            new_arr[(i + k) % n] = nums[i]
        nums[:] = new_arr
    # 数组翻转
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    # 121. 买卖股票的最佳时机
    # 只是返回最大利润
    def maxProfit(self, prices: List[int]) -> int:
        int_max = int(1e9)
        min_price = int_max
        max_profile = 0
        for price in prices:
            max_profile = max(price - min_price, max_profile)
            min_price = min(price, min_price)
        return max_profile
    # 122. 买卖股票的最佳时机 II 此题目中可以在规定的数列里面随时卖出，需要求出总利润最大值
    # 动态规划
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i]表示第i天的股票价格
        # dp[i][0]表示当天完成交易后，手里面没有股票
        #      1. 前一天就没有股票，所以收益为dp[i-1][0]
        #      2. 前一天手里有股票，需要将昨天的收益，加上今天股票的价格，所以收益为dp[i-1][1]+prices[i]
        # dp[i][1]表示当天完成交易后，手里还有股票
        #      1. 前一天就有股票，所以收益为dp[i-1][1]
        #      2. 前一天没有股票，需要在今天买入股票，所以要扣除今天的股票价格所以收益为dp[i-1][0]-prices[i]
        #  初始值为： dp[0][0]=0  dp[0][1]=-prices[i]
        #  由于最后一天手里持有股票的收益肯定小于或者等于不持有股票的收益  所以dp[n-1][0]>dp[n-1][1]
        #  所以最大利润输出dp[n-1][0]
        n = len(prices)
        dp = [[0] * 2 for i in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]
    # 贪心算法
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1, n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans
