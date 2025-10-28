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

# 41. Coin Change (DP)
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

# 42. Subsets
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [item + [num] for item in res]
    return res

# 43. Permutations
def permute(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        for perm in permute(nums[:i] + nums[i+1:]):
            res.append([nums[i]] + perm)
    return res

# 44. Combination Sum
def combination_sum(candidates, target):
    res = []
    def dfs(path, target, idx):
        if target == 0:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            if candidates[i] <= target:
                dfs(path + [candidates[i]], target - candidates[i], i)
    dfs([], target, 0)
    return res

# 45. Word Break
def word_break(s, wordDict):
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for word in wordDict:
            if dp[i-len(word)] and s[i-len(word):i] == word:
                dp[i] = True
    return dp[-1]

# 46. LRU Cache (Design)
class LRUCache:
    def __init__(self, capacity):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 47. Min Stack (Design)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.min_stack[-1]

# 48. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x):
        self.in_stack.append(x)
    def pop(self):
        self.peek()
        return self.out_stack.pop()
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    def empty(self):
        return not self.in_stack and not self.out_stack

# 49. Implement Stack using Queues
from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return not self.q

# 50. Number of Islands (DFS)
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

# 51. Flood Fill
def flood_fill(image, sr, sc, newColor):
    orig = image[sr][sc]
    if orig == newColor:
        return image
    def dfs(r, c):
        if (0 <= r < len(image)) and (0 <= c < len(image[0])) and image[r][c] == orig:
            image[r][c] = newColor
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
    dfs(sr, sc)
    return image

# 52. Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# 53. Invert Binary Tree
def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# 54. Symmetric Tree
def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
    return is_mirror(root, root)

# 55. Binary Tree Level Order Traversal
def level_order(root):
    res = []
    if not root:
        return res
    from collections import deque
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res

# 56. Convert Sorted Array to BST
def sorted_array_to_bst(nums):
    if not nums: return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

# 57. Path Sum
def has_path_sum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    return has_path_sum(root.left, targetSum - root.val) or has_path_sum(root.right, targetSum - root.val)

# 58. Lowest Common Ancestor of BST
def lowest_common_ancestor(root, p, q):
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)
    return root

# 59. Validate BST
def is_valid_bst(root, left=float('-inf'), right=float('inf')):
    if not root:
        return True
    if not (left < root.val < right):
        return False
    return is_valid_bst(root.left, left, root.val) and is_valid_bst(root.right, root.val, right)

# 60. Kth Smallest Element in a BST
def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

# 61. Serialize and Deserialize Binary Tree
class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ' '.join(vals)
    def deserialize(self, data):
        vals = iter(data.split())
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# 62. Course Schedule (Graph, Topological Sort)
def can_finish(numCourses, prerequisites):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0]*numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    queue = deque([i for i in range(numCourses) if indegree[i]==0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return count == numCourses

# 63. Number of Connected Components in an Undirected Graph
def count_components(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        parent[find(u)] = find(v)
    return len(set(find(x) for x in range(n)))

# 64. Clone Graph
class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    old_to_new = {}
    def dfs(node):
        if not node:
            return None
        if node in old_to_new:
            return old_to_new[node]
        copy = GraphNode(node.val)
        old_to_new[node] = copy
        copy.neighbors = [dfs(nei) for nei in node.neighbors]
        return copy
    return dfs(node)

# 65. Word Ladder (BFS)
def ladder_length(beginWord, endWord, wordList):
    from collections import deque
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    queue.append((next_word, length+1))
                    wordSet.remove(next_word)
    return 0

# 66. Find All Anagrams in a String
def find_anagrams(s, p):
    from collections import Counter
    res, p_count, s_count = [], Counter(p), Counter(s[:len(p)-1])
    for i in range(len(p)-1, len(s)):
        s_count[s[i]] += 1
        if s_count == p_count:
            res.append(i-len(p)+1)
        s_count[s[i-len(p)+1]] -= 1
        if s_count[s[i-len(p)+1]] == 0:
            del s_count[s[i-len(p)+1]]
    return res

# 67. Top K Frequent Elements
def top_k_frequent(nums, k):
    from collections import Counter
    return [item for item, _ in Counter(nums).most_common(k)]

# 68. Product of Array Except Self
def product_except_self(nums):
    n = len(nums)
    res = [1]*n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

# 69. Find Minimum in Rotated Sorted Array
def find_min(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# 70. Search in Rotated Sorted Array
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

# 71. Find Peak Element
def find_peak_element(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid
    return left

# 72. Valid Sudoku
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            if num in rows[i] or num in cols[j] or num in boxes[(i//3)*3 + j//3]:
                return False
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i//3)*3 + j//3].add(num)
    return True

# 73. Minimum Window Substring
def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = i = 0
    res = (0, float('inf'))
    for right, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if right-left < res[1]-res[0]:
                res = (left, right)
            need[s[left]] += 1
            missing += 1
            left += 1
    return "" if res[1] == float('inf') else s[res[0]:res[1]]

# 74. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_map = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right-left+1)
    return max_len

# 75. Longest Palindromic Substring
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

# 76. Edit Distance
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
                dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# 77. Decode Ways
def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[-1]

# 78. Maximum Product Subarray
def max_product(nums):
    res = max(nums)
    cur_min = cur_max = 1
    for n in nums:
        tmp = cur_max * n
        cur_max = max(n, tmp, cur_min * n)
        cur_min = min(n, tmp, cur_min * n)
        res = max(res, cur_max)
    return res

# 79. House Robber
def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    dp = [0]*len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

# 80. House Robber II (Circular)
def rob2(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))

# 81. Unique Paths (DP)
def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

# 82. Unique Paths II (Obstacles)
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

# 83. Minimum Path Sum
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

# 84. Triangle (Minimum Path Sum)
def minimum_total(triangle):
    dp = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(i+1):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    return dp[0]

# 85. Maximal Square
def maximal_square(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*(n+1) for _ in range(m+1)]
    ans = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])
    return ans * ans

# 86. Largest Rectangle in Histogram
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, H * W)
        stack.append(i)
    heights.pop()
    return max_area

# 87. Trapping Rain Water
def trap(height):
    if not height:
        return 0
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

# 88. Merge Sorted Array
def merge_sorted_array(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    nums1[:n] = nums2[:n]
    return nums1

# 89. Remove Element
def remove_element(nums, val):
    i = 0
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
    return i

# 90. Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_end = True
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.is_end
    def starts_with(self, prefix):
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True

# 91. Linked List Cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 92. Remove Linked List Elements
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

# 93. Reverse Linked List
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# 94. Merge K Sorted Lists
import heapq
def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

# 95. Find Intersection Node of Two Linked Lists
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# 96. Palindrome Linked List
def is_palindrome_linkedlist(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]

# 97. Remove Nth Node From End of List
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

# 98. Odd Even Linked List
def odd_even_list(head):
    if not head:
        return None
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

# 99. Copy List with Random Pointer
class RandomListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    curr = head
    while curr:
        next = curr.next
        copy = RandomListNode(curr.val)
        curr.next = copy
        copy.next = next
        curr = next
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    curr = head
    pseudo = RandomListNode(0)
    copy_curr = pseudo
    while curr:
        next = curr.next.next
        copy = curr.next
        copy_curr.next = copy
        copy_curr = copy
        curr.next = next
        curr = next
    return pseudo.next

# 100. Add Two Numbers (Linked List)
def add_two_numbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val = v1 + v2 + carry
        carry = val // 10
        curr.next = ListNode(val % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next