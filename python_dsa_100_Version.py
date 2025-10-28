# 100 DSA Problems with Solutions in Python

# 1. Two Sum
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

# 2. Reverse an Array
def reverse_array(arr):
    return arr[::-1]

# 3. Check Palindrome String
def is_palindrome(s):
    return s == s[::-1]

# 4. Fibonacci Number (Recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 5. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

# 6. Valid Parentheses
def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

# 7. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

# 8. Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray_sum(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# 9. Move Zeroes to End
def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    return nums

# 10. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0
    insert_pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[insert_pos] = nums[i]
            insert_pos += 1
    return insert_pos

# 11. Rotate Array
def rotate_array(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# 12. Intersection of Two Arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# 13. Plus One
def plus_one(digits):
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# 14. Single Number
def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

# 15. Missing Number
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

# 16. Contains Duplicate
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# 17. Best Time to Buy and Sell Stock
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# 18. Climbing Stairs (DP)
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b

# 19. Pascal's Triangle
def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

# 20. Valid Anagram
def is_anagram(s, t):
    return sorted(s) == sorted(t)

# 21. Group Anagrams
from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

# 22. First Unique Character in a String
def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

# 23. Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

# 24. Valid Palindrome (ignoring non-alphanumeric)
def is_palindrome_string(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# 25. Implement strStr()
def str_str(haystack, needle):
    return haystack.find(needle)

# 26. Count and Say
def count_and_say(n):
    result = "1"
    for _ in range(n-1):
        prev, result = result, ""
        i = 0
        while i < len(prev):
            count = 1
            while i+1 < len(prev) and prev[i] == prev[i+1]:
                i += 1
                count += 1
            result += str(count) + prev[i]
            i += 1
    return result

# 27. Length of Last Word
def length_of_last_word(s):
    return len(s.strip().split(' ')[-1])

# 28. Add Binary
def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# 29. Sqrt(x)
def my_sqrt(x):
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        num = mid * mid
        if num > x:
            right = mid - 1
        elif num < x:
            left = mid + 1
        else:
            return mid
    return right

# 30. Valid Perfect Square
def is_perfect_square(num):
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == num:
            return True
        elif sq < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

# 31. Power of Three
def is_power_of_three(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# 32. Roman to Integer
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in reversed(s):
        curr = roman[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

# 33. Integer to Roman
def int_to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res = ""
    for i, v in enumerate(val):
        res += syms[i]*(num//v)
        num %= v
    return res

# 34. Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# 35. Insert Interval
def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
    res.append(newInterval)
    return res

# 36. Spiral Matrix
def spiral_order(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res

# 37. Rotate Image (90 degrees)
def rotate(matrix):
    matrix[:] = zip(*matrix[::-1])
    matrix[:] = [list(row) for row in matrix]
    return matrix

# 38. Set Matrix Zeroes
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = any(matrix[0][j] == 0 for j in range(cols))
    col_zero = any(matrix[i][0] == 0 for i in range(rows))
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if col_zero:
        for i in range(rows):
            matrix[i][0] = 0
    return matrix

# 39. Search a 2D Matrix
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

# 40. Longest Increasing Subsequence
def length_of_LIS(nums):
    import bisect
    dp = []
    for num in nums:
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    return len(dp)
