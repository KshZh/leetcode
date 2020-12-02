# [112. Path Sum](https://leetcode.com/problems/path-sum/)

> Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> Given the below binary tree and `sum = 22`,
>
> ```
>       5
>      / \
>     4   8
>    /   / \
>   11  13  4
>  /  \      \
> 7    2      1
> ```
>
> return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.

```java
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.addFirst(root) ;	    
        while (!stack.isEmpty()) {
            TreeNode cur = stack.removeFirst() ;	
            if (cur.left==null && cur.right==null) {	    		
                if (cur.val == sum ) return true ;
            }
            if (cur.right != null) {
                cur.right.val += cur.val;
                stack.addFirst(cur.right) ;
            }
            if (cur.left != null) {
                cur.left.val += cur.val;
                stack.addFirst(cur.left);
            }
        }
        return false ;
    }
}
```

```java
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null) return false;
    
        if(root.left == null && root.right == null && sum - root.val == 0) return true;
    
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
```

# [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

> Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> Given the below binary tree and `sum = 22`,
>
> ```
>       5
>      / \
>     4   8
>    /   / \
>   11  13  4
>  /  \    / \
> 7    2  5   1
> ```
>
> Return:
>
> ```
> [
>    [5,4,11,2],
>    [5,8,4,5]
> ]
> ```

```java
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(root, sum, new ArrayList<>(), res);
        return res;
    }
    
    // 回溯。
    private void dfs(TreeNode root, int left, List<Integer> path, List<List<Integer>> res) {
        if (root == null) {
            return;
        }
        left -= root.val;
        path.add(root.val);
        if (root.left==null && root.right==null && left==0) {
            res.add(new ArrayList<>(path));
        } else {
            dfs(root.left, left, path, res);
            dfs(root.right, left, path, res);
        }
        path.remove(path.size()-1);
    }
}
```

# [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

> You are given a binary tree in which each node contains an integer value.
>
> Find the number of paths that sum to a given value.
>
> The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
>
> The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
>
> **Example:**
>
> ```
> root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
> 
>    10
>   /  \
>  5   -3
> / \    \
> 3   2   11
> / \   \
> 3  -2   1
> 
> Return 3. The paths that sum to 8 are:
> 
> 1.  5 -> 3
> 2.  5 -> 2 -> 1
> 3. -3 -> 11
> ```

```java
// 前缀和数组/哈希表，能够在O(1)内求得区间和。
//
// currSum是根到当前结点的路径上的结点和。
// prefixSum的key是从根到当前结点的路径上的前缀和（前缀和当然是从根开始），由于既有正数也有负数，所以可能有多个相等的前缀和，用value存储有多少个相等的前缀和。
// 然后对于每一个结点，求出前缀和为currSum-target的前缀和个数，就得到从根到当前结点路径上的某个中间结点到当前结点的路径和为target的路径个数。
// 比如某条根到某结点的路径是：1,2,-1,-1,2，target为2，前缀和序列为1,3,2,1,3，可以看到前缀和为1的前缀和有2个，当走到最后一个结点2时，currSum为3（即整条路径的和），减去target，得到1，就得到中间某个结点到当前结点的路径和为target的路径个数为2，具体是{2, -1, -1, 2}, {2}。
class Solution {
    public int pathSum(TreeNode root, int sum) {
        HashMap<Integer, Integer> prefixSum = new HashMap();
        prefixSum.put(0,1);
        return helper(root, 0, sum, prefixSum);
    }
    
    public int helper(TreeNode root, int currSum, int target, HashMap<Integer, Integer> prefixSum) {
        if (root == null) {
            return 0;
        }
        
        currSum += root.val;
        int res = prefixSum.getOrDefault(currSum - target, 0);
        prefixSum.put(currSum, prefixSum.getOrDefault(currSum, 0) + 1);
        
        res += helper(root.left, currSum, target, prefixSum) + helper(root.right, currSum, target, prefixSum);
        prefixSum.put(currSum, prefixSum.get(currSum) - 1);
        return res;
    }
}
```

# [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

> Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
>
> The length of path between two nodes is represented by the number of edges between them.
>
> 
>
> **Example 1:**
>
> **Input:**
>
> ```
>            5
>           / \
>          4   5
>         / \   \
>        1   1   5
> ```
>
> **Output:** 2
>
> 
>
> **Example 2:**
>
> **Input:**
>
> ```
>            1
>           / \
>          4   5
>         / \   \
>        4   4   5
> ```
>
> **Output:** 2
>
> 
>
> **Note:** The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

```java
// O(N), O(N).
class Solution {
    int ans;
    public int longestUnivaluePath(TreeNode root) {
        ans = 0;
        arrowLength(root);
        return ans;
    }
    public int arrowLength(TreeNode node) {
        if (node == null) return 0;
        int left = arrowLength(node.left)
        int right = arrowLength(node.right);
        int arrowLeft = 0, arrowRight = 0;
        if (node.left != null && node.left.val == node.val) {
            // 查看是否可以接上。
            arrowLeft += left + 1;
        }
        if (node.right != null && node.right.val == node.val) {
            // 查看是否可以接上。
            arrowRight += right + 1;
        }
        ans = Math.max(ans, arrowLeft + arrowRight);
        return Math.max(arrowLeft, arrowRight); // 返回子树中满足条件的最长的那条路径。
    }
}
```

# [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

> 给定一个非空二叉树，返回其最大路径和。
>
> 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
>
> 示例 1:
>
> ```
> 输入: [1,2,3]
> 
>     1
>    / \
>   2   3
> 
> 输出: 6
> ```
>
> 示例 2:
>
> ```
> 输入: [-10,9,20,null,null,15,7]
> 
> -10
> / \
> 9  20
>  /  \
> 15   7
> 
> 输出: 42
> ```

```java
class Solution {
  int max_sum = Integer.MIN_VALUE;

  public int max_gain(TreeNode node) {
    if (node == null) return 0;

    // max sum on the left and right sub-trees of node
    // 如果子分支的和为负数，那么就不连上这个分支了。
    int left_gain = Math.max(max_gain(node.left), 0);
    int right_gain = Math.max(max_gain(node.right), 0);

    // the price to start a new path where `node` is a highest node
    int price_newpath = node.val + left_gain + right_gain;

    // update max_sum if it's better to start a new path
    max_sum = Math.max(max_sum, price_newpath);

	// 返回和最大的其中一支供上层组成路径。
    return node.val + Math.max(left_gain, right_gain);
  }

  public int maxPathSum(TreeNode root) {
    max_gain(root);
    return max_sum;
  }
}

// 作者：LeetCode
// 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-de-zui-da-lu-jing-he-by-leetcode/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```