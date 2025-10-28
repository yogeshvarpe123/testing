# 201. Longest Substring with At Most K Distinct Characters
def length_of_longest_substring_k_distinct(s, k):
    from collections import defaultdict
    left = 0
    count = defaultdict(int)
    max_len = 0
    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# 202. Find All Anagrams in a String
def find_anagrams(s, p):
    from collections import Counter
    ns, np = len(s), len(p)
    if np > ns: return []
    p_count = Counter(p)
    s_count = Counter(s[:np-1])
    res = []
    for i in range(np-1, ns):
        s_count[s[i]] += 1
        if s_count == p_count:
            res.append(i-np+1)
        s_count[s[i-np+1]] -= 1
        if s_count[s[i-np+1]] == 0:
            del s_count[s[i-np+1]]
    return res

# 203. Longest Repeating Character Replacement
def character_replacement(s, k):
    from collections import Counter
    left = 0
    max_count = 0
    count = Counter()
    max_len = 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# 204. Minimum Window Substring
def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

# 205. Subarrays with K Different Integers
def subarrays_with_k_distinct(A, K):
    from collections import defaultdict
    def at_most_k(k):
        count = defaultdict(int)
        res = left = 0
        for right in range(len(A)):
            if count[A[right]] == 0:
                k -= 1
            count[A[right]] += 1
            while k < 0:
                count[A[left]] -= 1
                if count[A[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
        return res
    return at_most_k(K) - at_most_k(K-1)

# 206. Longest Palindromic Substring
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        tmp = expand(s, i, i)
        if len(tmp) > len(res): res = tmp
        tmp = expand(s, i, i+1)
        if len(tmp) > len(res): res = tmp
    return res
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

# 207. Longest Palindromic Subsequence
def longest_palindromic_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

# 208. Valid Parentheses String (with *)
def check_valid_string(s):
    low = high = 0
    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        if high < 0:
            return False
        low = max(low, 0)
    return low == 0

# 209. Basic Calculator
def calculate(s):
    stack = []
    num, sign = 0, 1
    res = 0
    s = s.replace(' ', '')
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num*10 + int(s[i])
                i += 1
            res += sign * num
            continue
        if s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif s[i] == ')':
            res = stack.pop() * res + stack.pop()
        i += 1
    return res

# 210. Decode Ways
def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [1, 1]
    for i in range(1, n):
        if s[i] == '0':
            if s[i-1] in '12':
                dp.append(dp[-2])
            else:
                return 0
        elif 10 <= int(s[i-1:i+1]) <= 26:
            dp.append(dp[-1]+dp[-2])
        else:
            dp.append(dp[-1])
    return dp[-1]

# 211. Zigzag Conversion
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * numRows
    idx, step = 0, 1
    for c in s:
        rows[idx] += c
        if idx == 0:
            step = 1
        elif idx == numRows - 1:
            step = -1
        idx += step
    return ''.join(rows)

# 212. Multiply Strings
def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    res = [0]*(len(num1)+len(num2))
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            mul = int(num1[i])*int(num2[j])
            pos1 = i+j
            pos2 = i+j+1
            s = mul + res[pos2]
            res[pos1] += s // 10
            res[pos2] = s % 10
    result = ''.join(map(str, res)).lstrip('0')
    return result or "0"

# 213. Wildcard Matching
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]

# 214. Regular Expression Matching
def is_match_regex(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(2, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] |= dp[i-1][j]
    return dp[m][n]

# 215. Count and Say
def count_and_say(n):
    res = "1"
    for _ in range(n-1):
        prev = res
        res = ""
        i = 0
        while i < len(prev):
            count = 1
            while i+1 < len(prev) and prev[i] == prev[i+1]:
                i += 1
                count += 1
            res += str(count) + prev[i]
            i += 1
    return res

# 216. String to Integer (Atoi)
def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
    sign, i, n = 1, 0, len(s)
    if s[0] in "+-":
        sign = -1 if s[0] == '-' else 1
        i += 1
    res = 0
    while i < n and s[i].isdigit():
        res = res*10 + int(s[i])
        i += 1
    res *= sign
    res = max(min(res, 2**31-1), -2**31)
    return res

# 217. Reverse Words in a String
def reverse_words(s):
    return ' '.join(s.strip().split()[::-1])

# 218. Longest Common Subsequence
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

# 219. Edit Distance
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# 220. Minimum Path Sum
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]

# 221. Unique Paths
def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]

# 222. Unique Paths II (with Obstacles)
def unique_paths_with_obstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1-obstacleGrid[0][0]
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1 or (i == 0 and j == 0):
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[-1][-1]
    
    
    
    

# 223. Minimum Edit Distance (Levenshtein)
def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# 224. Maximum Subarray Product
def max_product(nums):
    res = max(nums)
    cur_min = cur_max = 1
    for n in nums:
        tmp = cur_max * n
        cur_max = max(n, tmp, cur_min * n)
        cur_min = min(n, tmp, cur_min * n)
        res = max(res, cur_max)
    return res

# 225. Maximum Subarray Sum Circular
def max_subarray_sum_circular(A):
    total = 0
    max_sum = cur_max = float('-inf')
    min_sum = cur_min = float('inf')
    for a in A:
        cur_max = max(cur_max + a, a)
        max_sum = max(max_sum, cur_max)
        cur_min = min(cur_min + a, a)
        min_sum = min(min_sum, cur_min)
        total += a
    return max(max_sum, total - min_sum) if max_sum > 0 else max_sum

# 226. Maximum Product Subarray (contiguous, can be negative)
def max_product_subarray(nums):
    max_so_far = min_so_far = res = nums[0]
    for n in nums[1:]:
        candidates = (n, max_so_far*n, min_so_far*n)
        max_so_far = max(candidates)
        min_so_far = min(candidates)
        res = max(res, max_so_far)
    return res

# 227. Subarray Sum Closest to Zero
def subarray_sum_closest(nums):
    prefix = [(0, -1)]
    s = 0
    for i, n in enumerate(nums):
        s += n
        prefix.append((s, i))
    prefix.sort()
    min_diff = float('inf')
    res = [0, 0]
    for i in range(1, len(prefix)):
        diff = abs(prefix[i][0] - prefix[i-1][0])
        if diff < min_diff:
            min_diff = diff
            left = min(prefix[i][1], prefix[i-1][1]) + 1
            right = max(prefix[i][1], prefix[i-1][1])
            res = [left, right]
    return res

# 228. Subarray Sum Equals K (Prefix sum + Hashmap)
def subarray_sum_equals_k(nums, k):
    from collections import defaultdict
    count, curr_sum = 0, 0
    sums = defaultdict(int)
    sums[0] = 1
    for n in nums:
        curr_sum += n
        count += sums[curr_sum - k]
        sums[curr_sum] += 1
    return count

# 229. Maximum Size Subarray Sum Equals k
def max_sub_array_len(nums, k):
    prefix_sum, d, max_len = 0, {0: -1}, 0
    for i, n in enumerate(nums):
        prefix_sum += n
        if prefix_sum - k in d:
            max_len = max(max_len, i - d[prefix_sum - k])
        if prefix_sum not in d:
            d[prefix_sum] = i
    return max_len

# 230. Minimum Size Subarray Sum (Sliding Window)
def min_sub_array_len(target, nums):
    left = 0
    curr_sum = 0
    res = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            res = min(res, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return 0 if res == float('inf') else res

# 231. Majority Element (Moore Voting)
def majority_element(nums):
    count, candidate = 0, None
    for n in nums:
        if count == 0:
            candidate = n
        count += (1 if n == candidate else -1)
    return candidate

# 232. Median of Two Sorted Arrays
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    if len(A) > len(B):
        A, B = B, A
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2
        j = half - i - 2
        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i+1] if (i+1) < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j+1] if (j+1) < len(B) else float('inf')
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

# 233. Find First and Last Position of Element in Sorted Array
def search_range(nums, target):
    def find_bound(is_left):
        left, right = 0, len(nums)-1
        bound = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                bound = mid
                if is_left:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return bound
    return [find_bound(True), find_bound(False)]

# 234. Find Minimum in Rotated Sorted Array
def find_min(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]

# 235. Search in Rotated Sorted Array
def search_rotated(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
    return -1

# 236. Find Peak Element
def find_peak_element(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid
    return left

# 237. Intersection of Two Arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# 238. Intersection of Two Arrays II
def intersect(nums1, nums2):
    from collections import Counter
    a, b = Counter(nums1), Counter(nums2)
    res = []
    for k in a:
        res += [k]*min(a[k], b.get(k, 0))
    return res

# 239. Find the Duplicate Number
def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# 240. Find All Duplicates in an Array
def find_duplicates(nums):
    res = []
    for n in nums:
        if nums[abs(n)-1] < 0:
            res.append(abs(n))
        nums[abs(n)-1] *= -1
    return res

# 241. Find All Numbers Disappeared in an Array
def find_disappeared_numbers(nums):
    for n in nums:
        nums[abs(n)-1] = -abs(nums[abs(n)-1])
    return [i+1 for i, n in enumerate(nums) if n > 0]

# 242. First Missing Positive
def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1

# 243. Largest Rectangle in Histogram
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i-stack[-1]-1
            max_area = max(max_area, height*width)
        stack.append(i)
    heights.pop()
    return max_area

# 244. Trapping Rain Water
def trap(height):
    if not height: return 0
    left, right = 0, len(height)-1
    left_max = right_max = 0
    res = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1
    return res

# 245. Maximal Rectangle
def maximal_rectangle(matrix):
    if not matrix: return 0
    n = len(matrix[0])
    height = [0]*(n+1)
    max_area = 0
    for row in matrix:
        for i in range(n):
            if row[i] == '1':
                height[i] += 1
            else:
                height[i] = 0
        stack = []
        for i in range(n+1):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                max_area = max(max_area, h*w)
            stack.append(i)
    return max_area

# 246. Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# 247. Insert Interval
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

# 248. Non-overlapping Intervals
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count, end = 0, float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count

# 249. Meeting Rooms
def can_attend_meetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

# 250. Meeting Rooms II
def min_meeting_rooms(intervals):
    if not intervals: return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    s = e = rooms = 0
    while s < len(intervals):
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
        else:
            e += 1
            s += 1
    return rooms

# 251. Gas Station
def can_complete_circuit(gas, cost):
    total = tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i+1
            tank = 0
        total += gas[i] - cost[i]
    return start if total >= 0 else -1

# 252. Candy
def candy(ratings):
    n = len(ratings)
    res = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            res[i] = res[i-1]+1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            res[i] = max(res[i], res[i+1]+1)
    return sum(res)

# 253. Jump Game
def can_jump(nums):
    far = 0
    for i, num in enumerate(nums):
        if i > far:
            return False
        far = max(far, i+num)
    return True

# 254. Jump Game II
def jump(nums):
    jumps = far = curr_end = 0
    for i in range(len(nums)-1):
        far = max(far, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = far
    return jumps

# 255. Best Time to Buy and Sell Stock
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# 256. Best Time to Buy and Sell Stock II
def max_profit_2(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

# 257. Best Time to Buy and Sell Stock with Transaction Fee
def max_profit_with_fee(prices, fee):
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash

# 258. Best Time to Buy and Sell Stock III
def max_profit_3(prices):
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2

# 259. House Robber
def rob(nums):
    prev = curr = 0
    for n in nums:
        prev, curr = curr, max(curr, prev+n)
    return curr

# 260. House Robber II
def rob_2(nums):
    if len(nums) <= 1:
        return nums[0] if nums else 0
    def helper(nums):
        prev = curr = 0
        for n in nums:
            prev, curr = curr, max(curr, prev+n)
        return curr
    return max(helper(nums[1:]), helper(nums[:-1]))

# 261. House Robber III (Tree DP)
def rob_3(root):
    def dfs(node):
        if not node: return (0, 0)
        left = dfs(node.left)
        right = dfs(node.right)
        return (node.val + left[1] + right[1], max(left) + max(right))
    return max(dfs(root))

# 262. Coin Change
def coin_change(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] < float('inf') else -1

# 263. Coin Change II
def change(amount, coins):
    dp = [1]+[0]*amount
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    return dp[amount]

# 264. Climbing Stairs
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# 265. Minimum Cost Climbing Stairs
def min_cost_climbing_stairs(cost):
    n = len(cost)
    a, b = 0, 0
    for i in range(2, n+1):
        a, b = b, min(b+cost[i-1], a+cost[i-2])
    return b

# 266. Longest Increasing Subsequence
def length_of_LIS(nums):
    import bisect
    dp = []
    for n in nums:
        i = bisect.bisect_left(dp, n)
        if i == len(dp):
            dp.append(n)
        else:
            dp[i] = n
    return len(dp)

# 267. Russian Doll Envelopes
def max_envelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    import bisect
    dp = []
    for _, h in envelopes:
        i = bisect.bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = h
    return len(dp)

# 268. Longest Common Substring
def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    maxlen = 0
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]+1
                maxlen = max(maxlen, dp[i+1][j+1])
    return maxlen

# 269. Partition Equal Subset Sum
def can_partition(nums):
    s = sum(nums)
    if s % 2: return False
    target = s // 2
    dp = set([0])
    for n in nums:
        dp |= set([x+n for x in dp])
    return target in dp

# 270. Ones and Zeroes (DP)
def find_max_form(strs, m, n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    for s in strs:
        zeros, ones = s.count('0'), s.count('1')
        for i in range(m, zeros-1, -1):
            for j in range(n, ones-1, -1):
                dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
    return dp[m][n]

# 271. Target Sum (DP)
def find_target_sum_ways(nums, S):
    s = sum(nums)
    if S > s or (S+s)%2 != 0: return 0
    target = (S+s)//2
    dp = [1]+[0]*target
    for n in nums:
        for i in range(target, n-1, -1):
            dp[i] += dp[i-n]
    return dp[target]

# 272. Combination Sum IV
def combination_sum4(nums, target):
    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for n in nums:
            if i >= n:
                dp[i] += dp[i-n]
    return dp[target]

# 273. Perfect Squares
def num_squares(n):
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[n]

# 274. Integer Break
def integer_break(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j, dp[j])*max(i-j, dp[i-j]))
    return dp[n]

# 275. Word Break
def word_break(s, wordDict):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        for w in wordDict:
            if dp[i-len(w)] and s[i-len(w):i] == w:
                dp[i] = True
    return dp[-1]

# 276. Word Break II
def word_break2(s, wordDict):
    n = len(s)
    dp = [[] for _ in range(n+1)]
    dp[0] = ['']
    for i in range(1, n+1):
        for w in wordDict:
            if i >= len(w) and s[i-len(w):i] == w:
                for l in dp[i-len(w)]:
                    dp[i].append((l+' '+w).strip())
    return dp[-1]

# 277. Palindrome Partitioning
def partition(s):
    res = []
    def backtrack(start, path):
        if start == len(s):
            res.append(path)
            return
        for end in range(start+1, len(s)+1):
            if s[start:end] == s[start:end][::-1]:
                backtrack(end, path+[s[start:end]])
    backtrack(0, [])
    return res

# 278. Palindrome Partitioning II
def min_cut(s):
    n = len(s)
    cut = [x-1 for x in range(n+1)]
    for i in range(n):
        for a, b in ((i,i), (i,i+1)):
            while a >= 0 and b < n and s[a] == s[b]:
                cut[b+1] = min(cut[b+1], 1+cut[a])
                a -= 1
                b += 1
    return cut[-1]

# 279. Largest Sum of Averages
def largest_sum_of_averages(A, K):
    n = len(A)
    P = [0]
    for x in A:
        P.append(P[-1]+x)
    dp = [0]*(n+1)
    for i in range(n):
        dp[i] = (P[n]-P[i])/(n-i)
    for k in range(K-1):
        for i in range(n):
            for j in range(i+1, n):
                dp[i] = max(dp[i], (P[j]-P[i])/(j-i)+dp[j])
    return dp[0]

# 280. Paint House
def min_cost(costs):
    if not costs: return 0
    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])
    return min(costs[-1])

# 281. Paint Fence
def num_ways(n, k):
    if n == 0: return 0
    if n == 1: return k
    same, diff = 0, k
    for i in range(2, n+1):
        same, diff = diff, (same+diff)*(k-1)
    return same+diff

# 282. Maximum Length of Repeated Subarray
def find_length(A, B):
    m, n = len(A), len(B)
    dp = [[0]*(n+1) for _ in range(m+1)]
    res = 0
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j]+1
                res = max(res, dp[i+1][j+1])
    return res

# 283. Distinct Subsequences
def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [1]+[0]*n
    for i in range(1, m+1):
        for j in range(n, 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] += dp[j-1]
    return dp[n]

# 284. Decode Ways II
def num_decodings2(s):
    m = 10**9+7
    a, b = 1, 1
    for i, c in enumerate(s):
        temp = b
        if c == '0':
            b = 0
        elif c == '*':
            b *= 9
        if i > 0:
            if s[i-1] == '1':
                if c == '*':
                    b += a*9
                else:
                    b += a
            elif s[i-1] == '2':
                if c == '*':
                    b += a*6
                elif c <= '6':
                    b += a
            elif s[i-1] == '*':
                if c == '*':
                    b += a*15
                elif c <= '6':
                    b += a*2
                else:
                    b += a
        b, a = b%m, temp
    return b

# 285. Number of Submatrices That Sum to Target
def num_submatrix_sum_target(matrix, target):
    from collections import Counter
    m, n = len(matrix), len(matrix[0])
    res = 0
    for i in range(m):
        arr = [0]*n
        for j in range(i, m):
            for k in range(n):
                arr[k] += matrix[j][k]
            count = Counter({0:1})
            curr = 0
            for a in arr:
                curr += a
                res += count[curr-target]
                count[curr] += 1
    return res

# 286. Maximum Sum of 3 Non-Overlapping Subarrays
def max_sum_of_three_subarrays(nums, k):
    n = len(nums)
    sum_ = [0]+list(nums)
    for i in range(1, n+1):
        sum_[i] += sum_[i-1]
    left, right = [0]*n, [n-k]*n
    total = sum_[k]-sum_[0]
    for i in range(k, n):
        if sum_[i+1]-sum_[i+1-k] > total:
            left[i] = i+1-k
            total = sum_[i+1]-sum_[i+1-k]
        else:
            left[i] = left[i-1]
    total = sum_[n]-sum_[n-k]
    for i in range(n-k-1, -1, -1):
        if sum_[i+k]-sum_[i] >= total:
            right[i] = i
            total = sum_[i+k]-sum_[i]
        else:
            right[i] = right[i+1]
    res, maxsum = [], 0
    for i in range(k, n-2*k+1):
        l, r = left[i-1], right[i+k]
        total = (sum_[l+k]-sum_[l])+(sum_[i+k]-sum_[i])+(sum_[r+k]-sum_[r])
        if total > maxsum:
            maxsum = total
            res = [l, i, r]
    return res

# 287. Maximum Subarray Sum with One Deletion
def maximum_sum(arr):
    n = len(arr)
    f = g = res = arr[0]
    for i in range(1, n):
        g = max(f, g+arr[i])
        f = max(arr[i], f+arr[i])
        res = max(res, f, g)
    return res

# 288. Partition Array into Disjoint Intervals
def partition_disjoint(A):
    left_max, overall_max = A[0], A[0]
    idx = 0
    for i in range(1, len(A)):
        overall_max = max(overall_max, A[i])
        if A[i] < left_max:
            left_max = overall_max
            idx = i
    return idx+1

# 289. Minimum Number of Refueling Stops
def min_refuel_stops(target, startFuel, stations):
    import heapq
    heap, i, res, n = [], 0, 0, len(stations)
    while startFuel < target:
        while i < n and stations[i][0] <= startFuel:
            heapq.heappush(heap, -stations[i][1])
            i += 1
        if not heap:
            return -1
        startFuel += -heapq.heappop(heap)
        res += 1
    return res

# 290. Minimum Falling Path Sum
def min_falling_path_sum(matrix):
    n = len(matrix)
    for i in range(n-2, -1, -1):
        for j in range(n):
            matrix[i][j] += min(matrix[i+1][j-1 if j-1>=0 else 0:j+2])
    return min(matrix[0])

# 291. Cherry Pickup
def cherry_pickup(grid):
    n = len(grid)
    dp = [[[-float('inf')]*n for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = grid[0][0]
    for k in range(1, 2*n-1):
        for i in range(max(0, k-n+1), min(n, k+1)):
            for j in range(max(0, k-n+1), min(n, k+1)):
                if grid[i][k-i] == -1 or grid[j][k-j] == -1:
                    continue
                val = grid[i][k-i]
                if i != j:
                    val += grid[j][k-j]
                dp[i][j][k] = max(
                    dp[x][y][k-1]
                    for x in [i, i-1] for y in [j, j-1]
                    if 0<=x<n and 0<=y<n and dp[x][y][k-1] != -float('inf')
                ) + val
    return max(0, dp[n-1][n-1][2*n-2])

# 292. Largest Plus Sign
def order_of_largest_plus_sign(N, mines):
    grid = [[1]*N for _ in range(N)]
    for i, j in mines:
        grid[i][j] = 0
    left = [[0]*N for _ in range(N)]
    right = [[0]*N for _ in range(N)]
    up = [[0]*N for _ in range(N)]
    down = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                left[i][j] = (left[i][j-1] if j else 0)+1
                up[i][j] = (up[i-1][j] if i else 0)+1
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if grid[i][j]:
                right[i][j] = (right[i][j+1] if j<N-1 else 0)+1
                down[i][j] = (down[i+1][j] if i<N-1 else 0)+1
    res = 0
    for i in range(N):
        for j in range(N):
            res = max(res, min(left[i][j], right[i][j], up[i][j], down[i][j]))
    return res

# 293. Largest Perimeter Triangle
def largest_perimeter(A):
    A.sort(reverse=True)
    for i in range(len(A)-2):
        if A[i] < A[i+1]+A[i+2]:
            return A[i]+A[i+1]+A[i+2]
    return 0

# 294. Kth Largest Element in an Array
def find_kth_largest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]

# 295. Kth Smallest Element in a Sorted Matrix
def kth_smallest(matrix, k):
    import heapq
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    for _ in range(k-1):
        val, x, y = heapq.heappop(heap)
        if y+1 < n:
            heapq.heappush(heap, (matrix[x][y+1], x, y+1))
    return heap[0][0]

# 296. Find Median from Data Stream
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

# 297. Top K Frequent Elements
def top_k_frequent(nums, k):
    from collections import Counter
    return [x for x, _ in Counter(nums).most_common(k)]

# 298. Sort Colors
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1
    return nums

# 299. Find All Anagrams in a String
def find_anagrams_str(s, p):
    from collections import Counter
    ns, np = len(s), len(p)
    if np > ns: return []
    p_count = Counter(p)
    s_count = Counter(s[:np-1])
    res = []
    for i in range(np-1, ns):
        s_count[s[i]] += 1
        if s_count == p_count:
            res.append(i-np+1)
        s_count[s[i-np+1]] -= 1
        if s_count[s[i-np+1]] == 0:
            del s_count[s[i-np+1]]
    return res

# 300. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_map = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right-left+1)
    return max_len