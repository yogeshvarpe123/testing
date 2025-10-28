# 101. Subarray Sum Equals K
def subarray_sum(nums, k):
    from collections import defaultdict
    count, curr_sum = 0, 0
    sums = defaultdict(int)
    sums[0] = 1
    for n in nums:
        curr_sum += n
        count += sums[curr_sum - k]
        sums[curr_sum] += 1
    return count

# 102. Find All Duplicates in an Array
def find_duplicates(nums):
    res = []
    for n in nums:
        if nums[abs(n)-1] < 0:
            res.append(abs(n))
        else:
            nums[abs(n)-1] *= -1
    return res

# 103. Longest Consecutive Sequence
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n-1 not in num_set:
            length = 1
            while n+length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# 104. Find the Duplicate Number (Floyd's Tortoise and Hare)
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

# 105. Set Mismatch
def find_error_nums(nums):
    n = len(nums)
    s = set(nums)
    return [sum(nums) - sum(s), n*(n+1)//2 - sum(s)]

# 106. Minimum Size Subarray Sum
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

# 107. Sliding Window Maximum
def max_sliding_window(nums, k):
    from collections import deque
    dq, out = deque(), []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i-k:
            dq.popleft()
        if i >= k-1:
            out.append(nums[dq[0]])
    return out

# 108. Minimum Window Subsequence
def min_window_subsequence(S, T):
    m, n = len(S), len(T)
    res = ""
    i = 0
    while i < m:
        if S[i] == T[0]:
            j = i
            k = 0
            while j < m and k < n:
                if S[j] == T[k]:
                    k += 1
                j += 1
            if k == n:
                end = j-1
                k = n-1
                j -= 1
                while k >= 0:
                    if S[j] == T[k]:
                        k -= 1
                    j -= 1
                start = j+1
                if not res or end-start+1 < len(res):
                    res = S[start:end+1]
                i = start
        i += 1
    return res

# 109. Find Median from Data Stream
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

# 110. Kth Largest Element in an Array
def find_kth_largest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]

# 111. Top K Frequent Words
def top_k_frequent_words(words, k):
    from collections import Counter
    cnt = Counter(words)
    return [w for w, _ in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:k]]

# 112. Sort Colors (Dutch National Flag)
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

# 113. Meeting Rooms II
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

# 114. Task Scheduler
def least_interval(tasks, n):
    from collections import Counter
    cnt = Counter(tasks).values()
    max_count = max(cnt)
    max_count_tasks = list(cnt).count(max_count)
    return max(len(tasks), (max_count - 1)*(n+1) + max_count_tasks)

# 115. Jump Game
def can_jump(nums):
    far = 0
    for i, num in enumerate(nums):
        if i > far:
            return False
        far = max(far, i+num)
    return True

# 116. Jump Game II
def jump(nums):
    jumps = far = curr_end = 0
    for i in range(len(nums)-1):
        far = max(far, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = far
    return jumps

# 117. Gas Station
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total = tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i+1
            tank = 0
    return start

# 118. Candy (Greedy)
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

# 119. Largest Number
def largest_number(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x*10, reverse=True)
    return str(int(''.join(nums)))

# 120. Product of Array Except Self (No division)
def product_except_self_2(nums):
    n = len(nums)
    answer = [1]*n
    left = right = 1
    for i in range(n):
        answer[i] *= left
        left *= nums[i]
    for i in range(n-1,-1,-1):
        answer[i] *= right
        right *= nums[i]
    return answer

# 121. Find Minimum in Rotated Sorted Array II (duplicates)
def find_min_2(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid+1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    return nums[left]

# 122. Search Insert Position
def search_insert(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return left

# 123. Find Peak Element II (2D)
def find_peak_grid(mat):
    m, n = len(mat), len(mat[0])
    left, right = 0, n-1
    while left <= right:
        mid = (left+right)//2
        max_row = max(range(m), key=lambda x: mat[x][mid])
        if mid > 0 and mat[max_row][mid]<mat[max_row][mid-1]:
            right = mid-1
        elif mid < n-1 and mat[max_row][mid]<mat[max_row][mid+1]:
            left = mid+1
        else:
            return [max_row, mid]

# 124. Search a 2D Matrix II
def search_matrix_2(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

# 125. Find K Closest Elements
def find_closest_elements(arr, k, x):
    left, right = 0, len(arr)-k
    while left < right:
        mid = (left+right)//2
        if x - arr[mid] > arr[mid+k] - x:
            left = mid+1
        else:
            right = mid
    return arr[left:left+k]

# 126. Split Array Largest Sum (Binary Search)
def split_array(nums, m):
    def can_split(mid):
        count, curr_sum = 1, 0
        for n in nums:
            curr_sum += n
            if curr_sum > mid:
                count += 1
                curr_sum = n
        return count <= m
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left+right)//2
        if can_split(mid):
            right = mid
        else:
            left = mid+1
    return left

# 127. Find First and Last Position of Element in Sorted Array
def search_range(nums, target):
    def find_left():
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
    def find_right():
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        return right
    left, right = find_left(), find_right()
    if left <= right:
        return [left, right]
    return [-1, -1]

# 128. Missing Ranges
def find_missing_ranges(nums, lower, upper):
    res = []
    prev = lower-1
    for i in range(len(nums)+1):
        curr = nums[i] if i < len(nums) else upper+1
        if curr - prev >= 2:
            res.append([prev+1, curr-1])
        prev = curr
    return res

# 129. Summary Ranges
def summary_ranges(nums):
    res = []
    i = 0
    while i < len(nums):
        start = i
        while i+1 < len(nums) and nums[i+1] == nums[i]+1:
            i += 1
        if start == i:
            res.append(str(nums[i]))
        else:
            res.append(f"{nums[start]}->{nums[i]}")
        i += 1
    return res

# 130. Intersection of Two Linked Lists II (With cycle)
def get_intersection_node_with_cycle(headA, headB):
    def get_cycle_entry(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    entryA = get_cycle_entry(headA)
    entryB = get_cycle_entry(headB)
    if entryA != entryB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a != entryA else headB
        b = b.next if b != entryB else headA
    return a

# 131. Linked List Random Node (Reservoir Sampling)
import random
class Solution131:
    def __init__(self, head):
        self.head = head
    def getRandom(self):
        curr, i, res = self.head, 1, None
        while curr:
            if random.randrange(i) == 0:
                res = curr.val
            curr = curr.next
            i += 1
        return res

# 132. Reorder List (LL)
def reorder_list(head):
    if not head or not head.next:
        return
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# 133. Reverse Linked List II (Between positions m and n)
def reverse_between(head, m, n):
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    for _ in range(m-1):
        pre = pre.next
    curr = pre.next
    for _ in range(n-m):
        temp = curr.next
        curr.next = temp.next
        temp.next = pre.next
        pre.next = temp
    return dummy.next

# 134. Swap Nodes in Linked List (kth from start and end)
def swap_nodes(head, k):
    first = last = head
    for _ in range(k-1):
        first = first.next
    fast = first
    while fast.next:
        fast = fast.next
        last = last.next
    first.val, last.val = last.val, first.val
    return head

# 135. Remove Duplicates from Unsorted Linked List
def remove_duplicates_unsorted(head):
    seen = set()
    prev, curr = None, head
    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = curr
        curr = curr.next
    return head

# 136. Find the Intersection of Two Arrays II
def intersect(nums1, nums2):
    from collections import Counter
    counts = Counter(nums1)
    res = []
    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res

# 137. Find the Longest Palindromic Subsequence
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

# 138. Partition Equal Subset Sum
def can_partition(nums):
    s = sum(nums)
    if s % 2 != 0: return False
    target = s // 2
    dp = set([0])
    for num in nums:
        dp |= set([x+num for x in dp])
    return target in dp

# 139. Coin Change II (DP)
def change(amount, coins):
    dp = [1] + [0]*amount
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    return dp[amount]

# 140. Target Sum (DP)
def find_target_sum_ways(nums, S):
    s = sum(nums)
    if S > s or (S+s)%2 != 0: return 0
    target = (S+s)//2
    dp = [1]+[0]*target
    for num in nums:
        for i in range(target, num-1, -1):
            dp[i] += dp[i-num]
    return dp[target]

# 141. Word Search
def exist(board, word):
    m, n = len(board), len(board[0])
    def dfs(i, j, k):
        if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
            return False
        if k == len(word)-1:
            return True
        tmp, board[i][j] = board[i][j], '#'
        res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
        board[i][j] = tmp
        return res
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False

# 142. Sudoku Solver
def solve_sudoku(board):
    def valid(i, j, c):
        for k in range(9):
            if board[i][k] == c or board[k][j] == c or board[i//3*3+k//3][j//3*3+k%3] == c:
                return False
        return True
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if valid(i,j,c):
                            board[i][j] = c
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    solve()

# 143. N-Queens
def solve_n_queens(n):
    res = []
    def solve(queens, xy_diff, xy_sum):
        p = len(queens)
        if p == n:
            res.append(['.'*i + 'Q' + '.'*(n-i-1) for i in queens])
            return
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                solve(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
    solve([], [], [])
    return res

# 144. Knight's Tour (Backtracking)
def knights_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    def solve(x, y, movei):
        if movei == N*N:
            return True
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and board[nx][ny] == -1:
                board[nx][ny] = movei
                if solve(nx, ny, movei+1):
                    return True
                board[nx][ny] = -1
        return False
    board[0][0] = 0
    if solve(0, 0, 1):
        return board
    return []

# 145. Unique Binary Search Trees
def num_trees(n):
    dp = [1]*(n+1)
    for i in range(2, n+1):
        dp[i] = 0
        for j in range(1, i+1):
            dp[i] += dp[j-1]*dp[i-j]
    return dp[n]

# 146. Construct Binary Tree from Preorder and Inorder Traversal
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:idx+1], inorder[:idx])
    root.right = build_tree(preorder[idx+1:], inorder[idx+1:])
    return root

# 147. Flatten Binary Tree to Linked List
def flatten(root):
    if not root: return
    flatten(root.left)
    flatten(root.right)
    if root.left:
        right = root.right
        root.right = root.left
        root.left = None
        curr = root.right
        while curr.right:
            curr = curr.right
        curr.right = right

# 148. Serialize and Deserialize BST
class CodecBST:
    def serialize(self, root):
        vals = []
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ' '.join(vals)
    def deserialize(self, data):
        vals = list(map(int, data.split()))
        def build(lower, upper):
            if vals and lower < vals[0] < upper:
                val = vals.pop(0)
                node = TreeNode(val)
                node.left = build(lower, val)
                node.right = build(val, upper)
                return node
        return build(float('-inf'), float('inf'))

# 149. Binary Tree Right Side View
def right_side_view(root):
    res = []
    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.right, level+1)
        dfs(node.left, level+1)
    dfs(root, 0)
    return res

# 150. Binary Tree Zigzag Level Order Traversal
def zigzag_level_order(root):
    res = []
    if not root:
        return res
    from collections import deque
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right
    return res

# 151. Binary Tree Vertical Order Traversal
def vertical_order(root):
    from collections import defaultdict, deque
    cols = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, col = queue.popleft()
        if node:
            cols[col].append(node.val)
            queue.append((node.left, col-1))
            queue.append((node.right, col+1))
    return [cols[x] for x in sorted(cols)]

# 152. Maximum Width of Binary Tree
def width_of_binary_tree(root):
    max_width = 0
    queue = [(root, 1)]
    while queue:
        next_level = []
        min_index = queue[0][1]
        for node, idx in queue:
            if node.left:
                next_level.append((node.left, 2*idx))
            if node.right:
                next_level.append((node.right, 2*idx+1))
        max_width = max(max_width, queue[-1][1]-queue[0][1]+1)
        queue = next_level
    return max_width

# 153. Lowest Common Ancestor of a Binary Tree
def lowest_common_ancestor_bt(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor_bt(root.left, p, q)
    right = lowest_common_ancestor_bt(root.right, p, q)
    if left and right:
        return root
    return left or right

# 154. Diameter of Binary Tree
def diameter_of_binary_tree(root):
    diameter = 0
    def depth(node):
        nonlocal diameter
        if not node: return 0
        l, r = depth(node.left), depth(node.right)
        diameter = max(diameter, l+r)
        return max(l, r)+1
    depth(root)
    return diameter

# 155. Sum Root to Leaf Numbers
def sum_numbers(root):
    def dfs(node, curr):
        if not node:
            return 0
        curr = curr*10 + node.val
        if not node.left and not node.right:
            return curr
        return dfs(node.left, curr) + dfs(node.right, curr)
    return dfs(root, 0)

# 156. Path Sum II (all paths)
def path_sum(root, targetSum):
    res = []
    def dfs(node, path, s):
        if not node:
            return
        path.append(node.val)
        s += node.val
        if not node.left and not node.right and s == targetSum:
            res.append(path[:])
        dfs(node.left, path, s)
        dfs(node.right, path, s)
        path.pop()
    dfs(root, [], 0)
    return res

# 157. Binary Tree Maximum Path Sum
def max_path_sum(root):
    max_sum = float('-inf')
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        max_sum = max(max_sum, node.val+left+right)
        return node.val + max(left, right)
    dfs(root)
    return max_sum

# 158. Populating Next Right Pointers in Each Node
class Node158:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
def connect(root):
    if not root: return
    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left

# 159. Serialize and Deserialize N-ary Tree
class Node159:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children or []
class CodecNary:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node: return
            res.append(str(node.val))
            for c in node.children:
                dfs(c)
            res.append('#')
        dfs(root)
        return ' '.join(res)
    def deserialize(self, data):
        vals = iter(data.split())
        def dfs():
            v = next(vals)
            if v == '#': return None
            node = Node159(int(v), [])
            while True:
                child = dfs()
                if child is None: break
                node.children.append(child)
            return node
        return dfs()

# 160. Maximum Depth of N-ary Tree
def max_depth_nary(root):
    if not root: return 0
    return 1 + max([max_depth_nary(child) for child in root.children] or [0])

# 161. Find Leaves of Binary Tree
def find_leaves(root):
    res = []
    def dfs(node):
        if not node:
            return -1
        h = 1 + max(dfs(node.left), dfs(node.right))
        if h == len(res):
            res.append([])
        res[h].append(node.val)
        return h
    dfs(root)
    return res

# 162. Binary Tree Cameras
def min_camera_cover(root):
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 1
        l, r = dfs(node.left), dfs(node.right)
        if l == 0 or r == 0:
            res += 1
            return 2
        if l == 2 or r == 2:
            return 1
        return 0
    if dfs(root) == 0:
        res += 1
    return res

# 163. Count Univalue Subtrees
def count_unival_subtrees(root):
    count = 0
    def dfs(node):
        nonlocal count
        if not node:
            return True
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False
            count += 1
            return True
        return False
    dfs(root)
    return count

# 164. Find Duplicate Subtrees
def find_duplicate_subtrees(root):
    from collections import defaultdict
    trees = defaultdict(int)
    res = []
    def collect(node):
        if not node:
            return '#'
        serial = f"{node.val},{collect(node.left)},{collect(node.right)}"
        trees[serial] += 1
        if trees[serial] == 2:
            res.append(node)
        return serial
    collect(root)
    return res

# 165. Count Complete Tree Nodes
def count_nodes(root):
    def height(node):
        return 1 + height(node.left) if node else 0
    h = height(root)
    if h == 0:
        return 0
    if height(root.right) == h-1:
        return (1<<(h-1)) + count_nodes(root.right)
    else:
        return (1<<(h-2)) + count_nodes(root.left)

# 166. Find Bottom Left Tree Value
def find_bottom_left_value(root):
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.right: queue.append(node.right)
        if node.left: queue.append(node.left)
    return node.val

# 167. Maximum Binary Tree
def construct_maximum_binary_tree(nums):
    if not nums:
        return None
    max_idx = nums.index(max(nums))
    root = TreeNode(nums[max_idx])
    root.left = construct_maximum_binary_tree(nums[:max_idx])
    root.right = construct_maximum_binary_tree(nums[max_idx+1:])
    return root

# 168. Find Largest Value in Each Tree Row
def largest_values(root):
    from collections import deque
    res = []
    if not root: return res
    queue = deque([root])
    while queue:
        res.append(max(node.val for node in queue))
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return res

# 169. Find All Numbers Disappeared in an Array
def find_disappeared_numbers(nums):
    for n in nums:
        nums[abs(n)-1] = -abs(nums[abs(n)-1])
    return [i+1 for i, n in enumerate(nums) if n > 0]

# 170. Find All Elements That Appear More Than n/3 Times
def majority_element_2(nums):
    if not nums: return []
    n = len(nums)
    cand1 = cand2 = None
    cnt1 = cnt2 = 0
    for num in nums:
        if num == cand1:
            cnt1 += 1
        elif num == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1, cnt1 = num, 1
        elif cnt2 == 0:
            cand2, cnt2 = num, 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    return [c for c in (cand1, cand2) if nums.count(c) > n//3]

# 171. Find Minimum Absolute Difference in BST
def get_minimum_difference(root):
    prev, res = None, float('inf')
    def inorder(node):
        nonlocal prev, res
        if not node: return
        inorder(node.left)
        if prev is not None:
            res = min(res, node.val - prev)
        prev = node.val
        inorder(node.right)
    inorder(root)
    return res

# 172. Range Sum of BST
def range_sum_bst(root, L, R):
    if not root:
        return 0
    if root.val < L:
        return range_sum_bst(root.right, L, R)
    if root.val > R:
        return range_sum_bst(root.left, L, R)
    return root.val + range_sum_bst(root.left, L, R) + range_sum_bst(root.right, L, R)

# 173. Convert BST to Greater Tree
def convert_bst(root):
    total = 0
    def reverse_inorder(node):
        nonlocal total
        if node:
            reverse_inorder(node.right)
            total += node.val
            node.val = total
            reverse_inorder(node.left)
    reverse_inorder(root)
    return root

# 174. Minimum Height Trees
def find_min_height_trees(n, edges):
    if n == 1: return [0]
    from collections import defaultdict, deque
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    leaves = [i for i in range(n) if len(graph[i]) == 1]
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves
    return leaves

# 175. Find Redundant Connection
def find_redundant_connection(edges):
    parent = list(range(len(edges)+1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        pu, pv = find(u), find(v)
        if pu == pv:
            return [u, v]
        parent[pu] = pv

# 176. Evaluate Reverse Polish Notation
def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in "+-*/":
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a+b)
            elif t == '-': stack.append(a-b)
            elif t == '*': stack.append(a*b)
            else: stack.append(int(a/b))
        else:
            stack.append(int(t))
    return stack[0]

# 177. Basic Calculator II
def calculate(s):
    stack = []
    num, sign = 0, "+"
    s += '+'
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c in "+-*/":
            if sign == '+': stack.append(num)
            elif sign == '-': stack.append(-num)
            elif sign == '*': stack[-1] *= num
            elif sign == '/': stack[-1] = int(stack[-1]/num)
            num = 0
            sign = c
    return sum(stack)

# 178. Valid Parenthesis String (with *)
def check_valid_string(s):
    low = high = 0
    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            low -= 1
            high -= 1
        else: # *
            low -= 1
            high += 1
        if high < 0:
            return False
        low = max(low, 0)
    return low == 0

# 179. Remove Invalid Parentheses (BFS)
def remove_invalid_parentheses(s):
    from collections import deque
    queue = deque([s])
    visited = set([s])
    res, found = [], False
    while queue:
        cur = queue.popleft()
        if is_valid_parentheses(cur):
            res.append(cur)
            found = True
        if found: continue
        for i in range(len(cur)):
            if cur[i] not in '()': continue
            nxt = cur[:i] + cur[i+1:]
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return res

# 180. Longest Valid Parentheses
def longest_valid_parentheses(s):
    stack = [-1]
    res = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, i - stack[-1])
    return res

# 181. Evaluate Division (Graph)
def calc_equation(equations, values, queries):
    from collections import defaultdict, deque
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1/v
    def bfs(x, y):
        if x not in graph or y not in graph:
            return -1.0
        queue = deque([(x, 1.0)])
        visited = set()
        while queue:
            node, prod = queue.popleft()
            if node == y:
                return prod
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append((nei, prod*graph[node][nei]))
        return -1.0
    return [bfs(x, y) for x, y in queries]

# 182. Shortest Path in Binary Matrix
def shortest_path_binary_matrix(grid):
    from collections import deque
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    queue = deque([(0,0,1)])
    visited = set()
    while queue:
        x, y, d = queue.popleft()
        if (x, y) == (n-1, n-1):
            return d
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not grid[nx][ny] and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,d+1))
    return -1

# 183. All Paths from Source to Target (Graph)
def all_paths_source_target(graph):
    res = []
    def dfs(path, u):
        if u == len(graph)-1:
            res.append(path[:])
            return
        for v in graph[u]:
            dfs(path+[v], v)
    dfs([0], 0)
    return res

# 184. Number of Provinces (Union Find)
def find_circle_num(isConnected):
    n = len(isConnected)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j]:
                parent[find(i)] = find(j)
    return len(set(find(x) for x in range(n)))

# 185. Accounts Merge (Union Find)
def accounts_merge(accounts):
    from collections import defaultdict
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    email_to_name = {}
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            email_to_name[email] = name
            parent.setdefault(email, email)
            parent[find(acc[1])] = find(email)
    res = defaultdict(list)
    for email in email_to_name:
        res[find(email)].append(email)
    return [[email_to_name[e]] + sorted(res[e]) for e in res]

# 186. Surrounded Regions
def solve(board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])
    def dfs(i, j):
        if 0<=i<m and 0<=j<n and board[i][j] == 'O':
            board[i][j] = 'S'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)
    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'

# 187. Pacific Atlantic Water Flow
def pacific_atlantic(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    pac, atl = set(), set()
    def dfs(i, j, visited, prev):
        if (i,j) in visited or not (0<=i<m and 0<=j<n) or matrix[i][j]<prev:
            return
        visited.add((i,j))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            dfs(i+dx, j+dy, visited, matrix[i][j])
    for i in range(m):
        dfs(i, 0, pac, -float('inf'))
        dfs(i, n-1, atl, -float('inf'))
    for j in range(n):
        dfs(0, j, pac, -float('inf'))
        dfs(m-1, j, atl, -float('inf'))
    return list(pac & atl)

# 188. Course Schedule II (Topological Sort)
def find_order(numCourses, prerequisites):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0]*numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    queue = deque([i for i in range(numCourses) if indegree[i]==0])
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return res if len(res) == numCourses else []

# 189. Alien Dictionary (DFS Topological Sort)
def alien_order(words):
    from collections import defaultdict
    adj = defaultdict(set)
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                adj[c1].add(c2)
                break
    visited, res = {}, []
    def dfs(c):
        if c in visited:
            return visited[c]
        visited[c] = False
        for nei in adj[c]:
            if not dfs(nei): return False
        visited[c] = True
        res.append(c)
        return True
    if not all(dfs(c) for c in set(''.join(words))):
        return ""
    return ''.join(res[::-1])

# 190. Number of Distinct Islands
def num_distinct_islands(grid):
    def dfs(i, j, d, path):
        if not (0<=i<len(grid) and 0<=j<len(grid[0])) or grid[i][j]==0:
            return
        grid[i][j] = 0
        path.append(d)
        dfs(i+1, j, 'd', path)
        dfs(i-1, j, 'u', path)
        dfs(i, j+1, 'r', path)
        dfs(i, j-1, 'l', path)
        path.append('b')
    shapes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                path = []
                dfs(i, j, 'o', path)
                shapes.add(tuple(path))
    return len(shapes)

# 191. Number of Islands II (Union Find)
def num_islands2(m, n, positions):
    parent = {}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    islands = 0
    res = []
    for i, j in positions:
        if (i,j) in parent:
            res.append(islands)
            continue
        parent[(i,j)] = (i,j)
        islands += 1
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+dx, j+dy
            if (ni,nj) in parent:
                pi, pj = find((i,j)), find((ni,nj))
                if pi != pj:
                    parent[pi] = pj
                    islands -= 1
        res.append(islands)
    return res

# 192. Count of Smaller Numbers After Self
def count_smaller(nums):
    res = []
    def sort(enum):
        half = len(enum)//2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            m, n = len(left), len(right)
            i = j = 0
            while i < m or j < n:
                if j == n or (i < m and left[i][1] <= right[j][1]):
                    enum[i+j] = left[i]
                    res[left[i][0]] += j
                    i += 1
                else:
                    enum[i+j] = right[j]
                    j += 1
        return enum
    res = [0]*len(nums)
    sort(list(enumerate(nums)))
    return res

# 193. Largest Rectangle in Binary Matrix
def maximal_rectangle(matrix):
    if not matrix:
        return 0
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

# 194. Find the Celebrity (Graph in Matrix)
def find_celebrity(M):
    n = len(M)
    cand = 0
    for i in range(1, n):
        if M[cand][i]:
            cand = i
    if all(M[cand][i] == 0 for i in range(n) if i != cand) and all(M[i][cand] == 1 for i in range(n) if i != cand):
        return cand
    return -1

# 195. Find the Town Judge
def find_judge(n, trust):
    count = [0]*(n+1)
    for a, b in trust:
        count[a] -= 1
        count[b] += 1
    for i in range(1, n+1):
        if count[i] == n-1:
            return i
    return -1

# 196. Reconstruct Itinerary
def find_itinerary(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    res = []
    def visit(airport):
        while graph[airport]:
            visit(graph[airport].pop())
        res.append(airport)
    visit("JFK")
    return res[::-1]

# 197. Minimum Genetic Mutation
def min_mutation(start, end, bank):
    from collections import deque
    bank = set(bank)
    queue = deque([(start, 0)])
    while queue:
        word, step = queue.popleft()
        if word == end:
            return step
        for i in range(len(word)):
            for c in "ACGT":
                nxt = word[:i]+c+word[i+1:]
                if nxt in bank:
                    bank.remove(nxt)
                    queue.append((nxt, step+1))
    return -1

# 198. Longest Increasing Path in a Matrix
def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    def dfs(i,j):
        if dp[i][j]:
            return dp[i][j]
        val = matrix[i][j]
        dp[i][j] = 1 + max([dfs(i+dx, j+dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]
                             if 0<=i+dx<m and 0<=j+dy<n and matrix[i+dx][j+dy]>val] or [0])
        return dp[i][j]
    return max(dfs(i,j) for i in range(m) for j in range(n))

# 199. Count Submatrices With All Ones
def num_submat(mat):
    m, n = len(mat), len(mat[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j]:
                if i: mat[i][j] += mat[i-1][j]
    for row in mat:
        stack = []
        count = 0
        for val in row + [0]:
            width = 0
            while stack and stack[-1][0] >= val:
                h, w = stack.pop()
                count -= h*w
                width += w
            count += val*(width+1)
            stack.append((val, width+1))
            res += count
    return res

# 200. Find the Shortest Superstring
def shortest_superstring(A):
    n = len(A)
    overlap = [[0]*n for _ in range(n)]
    for i, x in enumerate(A):
        for j, y in enumerate(A):
            if i != j:
                for k in range(1, min(len(x), len(y))+1):
                    if x[-k:] == y[:k]:
                        overlap[i][j] = k
    dp = [[""]*n for _ in range(1<<n)]
    for i in range(n):
        dp[1<<i][i] = A[i]
    for mask in range(1<<n):
        for last in range(n):
            if not (mask & (1<<last)):
                continue
            for curr in range(n):
                if mask & (1<<curr): continue
                candidate = dp[mask][last] + A[curr][overlap[last][curr]:]
                if dp[mask | (1<<curr)][curr] == "" or len(candidate) < len(dp[mask | (1<<curr)][curr]):
                    dp[mask | (1<<curr)][curr] = candidate
    return min([s for s in dp[-1] if s], key=len)