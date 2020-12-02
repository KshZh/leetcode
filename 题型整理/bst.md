# [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

> Given a binary search tree with non-negative values, find the minimum [absolute difference](https://en.wikipedia.org/wiki/Absolute_difference) between values of any two nodes.
>
> **Example:**
>
> ```
> Input:
> 
>    1
>     \
>      3
>     /
>    2
> 
> Output:
> 1
> 
> Explanation:
> The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
> ```
>
>  
>
> **Note:**
>
> - There are at least two nodes in this BST.
> - This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

```java
// 利用BST的性质，对BST做中序遍历，能够得到一个非递减序列，然后比较相邻元素，取差最小的。
// 783的题解可以直接套用这一题的，所以就不记录了。
// 如果不是BST，而是普通的二叉树，那么朴素的解法就是遍历一次，把结点值收集到容器中，然后排序，然后比较相邻元素，取差最小的。时间复杂度为O(NlogN)。
class Solution {
    TreeNode prev = null;
    int min = Integer.MAX_VALUE;
    
    public int getMinimumDifference(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        getMinimumDifference(root.left);
        
        if (prev!=null && root.val-prev.val<min) {
            min = root.val-prev.val;
        }
        prev = root;
        
        getMinimumDifference(root.right);
        
        return min;
    }
}
```

```java
// 迭代版中序遍历。
class Solution {
    public int getMinimumDifference(TreeNode root) {
        // https://docs.oracle.com/en/java/javase/13/docs/api/java.base/java/util/Deque.html
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode p=root, prev=null;
        int min = Integer.MAX_VALUE;
        while (!stack.isEmpty() || p!=null) {
            while (p != null) {
                // 先序遍历，则在这里处理根。
                stack.addFirst(p);
                p = p.left;
            }
            
            p = stack.removeFirst();
            
            // 中序遍历，则在这里处理根。
            if (prev!=null && p.val-prev.val<min) {
                min = p.val-prev.val;
            }
            prev = p;
            
            p = p.right;
        }
        
        return min;
    }
}
```

# [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

> Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
>
> **Example 1:**
>
> ```
> Input: 
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> 
> Target = 9
> 
> Output: True
> ```
>
>  
>
> **Example 2:**
>
> ```
> Input: 
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> 
> Target = 28
> 
> Output: False
> ```

```java
// 哈希表。
// O(N), O(N).
public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set < Integer > set = new HashSet();
        return find(root, k, set);
    }
    public boolean find(TreeNode root, int k, Set < Integer > set) {
        if (root == null)
            return false;
        if (set.contains(k - root.val))
            return true;
        set.add(root.val);
        return find(root.left, k, set) || find(root.right, k, set);
    }
}
```

```java
// 利用BST的性质，先中序遍历得到一个非递减序列，然后使用首尾双指针求解two sum。
// O(N), O(N).
// 不过有时候可能上面的解法优一点，因为上面的解法只要找到解就不会再继续遍历了。
public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        List < Integer > list = new ArrayList();
        inorder(root, list);
        int l = 0, r = list.size() - 1;
        while (l < r) {
            int sum = list.get(l) + list.get(r);
            if (sum == k)
                return true;
            if (sum < k)
                l++;
            else
                r--;
        }
        return false;
    }
    public void inorder(TreeNode root, List < Integer > list) {
        if (root == null)
            return;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}
```

# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

> Given a binary tree, determine if it is a valid binary search tree (BST).
>
> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys **less than** the node's key.
> - The right subtree of a node contains only nodes with keys **greater than** the node's key.
> - Both the left and right subtrees must also be binary search trees.
>
>  
>
> **Example 1:**
>
> ```
>     2
>    / \
>   1   3
> 
> Input: [2,1,3]
> Output: true
> ```
>
> **Example 2:**
>
> ```
>     5
>    / \
>   1   4
>      / \
>     3   6
> 
> Input: [5,1,4,null,null,3,6]
> Output: false
> Explanation: The root node's value is 5 but its right child's value is 4.
> ```

```java
// 错误的解法，BST要求的是根大于左子树，小于右子树，而这个实现中，只检查了根大于左子结点，小于右子结点。
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        if (root.left!=null && root.val<root.left.val) {
            return false;
        }
        
        if (root.right!=null && root.val>root.right.val) {
            return false;
        }
        
        return isValidBST(root.left) && isValidBST(root.right);
    }
}
```

```java
// 传递一个范围，若根为x，则左子树的所有结点应在(lower, x)范围内，右子树所有结点应在(x, upper)范围内。
class Solution {
  public boolean helper(TreeNode node, Integer lower, Integer upper) {
    if (node == null) return true;

    int val = node.val;
    if (lower != null && val <= lower) return false;
    if (upper != null && val >= upper) return false;

    if (! helper(node.right, val, upper)) return false;
    if (! helper(node.left, lower, val)) return false;
    return true;
  }

  public boolean isValidBST(TreeNode root) {
    return helper(root, null, null);
  }
}
```

```java
// 利用BST的性质，中序遍历BST会得到一个非递减序列。
// 如果不是BST，那么中序遍历就不会得到一个有序序列。
class Solution {
  public boolean isValidBST(TreeNode root) {
    Deque<TreeNode> stack = new ArrayDeque<>();
    long prev = Long.MIN_VALUE; // 因为测试用例中有[-2147483648]这种，所以用一个更大范围的数据类型表示负无穷。

    while (!stack.isEmpty() || root != null) {
      while (root != null) {
        stack.addFirst(root);
        root = root.left;
      }
      root = stack.removeFirst();
      // If next element in inorder traversal
      // is smaller than the previous one
      // that's not BST.
      if (prev >= root.val) return false; // 这道题要求的BST不存在相等的元素，所有合法的序列应该是上升序列。
      prev = root.val;
      root = root.right;
    }
    return true;
  }
}
```

# [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

> Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
>
> For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.
>
> **Example:**
>
> ```
> Given the sorted linked list: [-10,-3,0,5,9],
> 
> One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
> 
>        0
>       / \
>     -3   9
>     /   /
>  -10  5
> ```

```java
// 时间复杂度O(NlogN)，对链表每一个结点遍历一次创建对应的树结点，每次会寻找链表的中点，需要遍历当前调用的链表的长度的一半次。
// 空间复杂度是O(logN)，是递归调用栈的开销。不是常见的O(N)，因为建立的是一个高度平衡的BST，不可能出现单链表树的情况。
// 可以先遍历一次链表，转换为数组，然后就能在O(1)内分割数组了，时间复杂度为O(N)。
class Solution {

  private ListNode findMiddleElement(ListNode head) {

    // The pointer used to disconnect the left half from the mid node.
    ListNode prevPtr = null;
    ListNode slowPtr = head;
    ListNode fastPtr = head;

    // Iterate until fastPr doesn't reach the end of the linked list.
    while (fastPtr != null && fastPtr.next != null) {
      prevPtr = slowPtr;
      slowPtr = slowPtr.next;
      fastPtr = fastPtr.next.next;
    }

    // Handling the case when slowPtr was equal to head.
    if (prevPtr != null) {
      prevPtr.next = null; // 把前一段链表的尾巴指向null，这样递归调用才知道在哪里返回。
    }

    return slowPtr;
  }

  public TreeNode sortedListToBST(ListNode head) {

    // If the head doesn't exist, then the linked list is empty
    if (head == null) {
      return null;
    }

    // Find the middle element for the list.
    ListNode mid = this.findMiddleElement(head);

    // The mid becomes the root of the BST.
    TreeNode node = new TreeNode(mid.val);

    // Base case when there is just one element in the linked list
    if (head == mid) {
      return node;
    }

    // Recursively form balanced BSTs using the left and right halves of the original list.
    node.left = this.sortedListToBST(head);
    node.right = this.sortedListToBST(mid.next);
    return node;
  }
}
```

```java
// O(N), O(logN).
class Solution {

  private ListNode head;

  private int findSize(ListNode head) {
    ListNode ptr = head;
    int c = 0;
    while (ptr != null) {
      ptr = ptr.next;  
      c += 1;
    }
    return c;
  }

  // 中序遍历，从一个升序链表创建一个高度平衡的BST。
  private TreeNode convertListToBST(int l, int r) {
    // Invalid case
    if (l > r) {
      return null;
    }

    int mid = (l + r) / 2;

    // First step of simulated inorder traversal. Recursively form
    // the left half
    TreeNode left = this.convertListToBST(l, mid - 1);

    // Once left half is traversed, process the current node
    TreeNode node = new TreeNode(this.head.val);
    node.left = left;

    // Maintain the invariance mentioned in the algorithm
    this.head = this.head.next;

    // Recurse on the right hand side and form BST out of them
    node.right = this.convertListToBST(mid + 1, r);
    return node;
  }

  public TreeNode sortedListToBST(ListNode head) {
    // Get the size of the linked list first
    int size = this.findSize(head);

    this.head = head;

    // Form the BST now that we know the size
    return convertListToBST(0, size - 1);
  }
}
```

# [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

> Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.
>
>  
>
> **Example 1:**
>
> ```
> Input: root = [3,1,4,null,2], k = 1
>    3
>   / \
>  1   4
>   \
>    2
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: root = [5,3,6,2,4,null,null,1], k = 3
>        5
>       / \
>      3   6
>     / \
>    2   4
>   /
>  1
> Output: 3
> ```
>
> **Follow up:**
> What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
>
>  
>
> **Constraints:**
>
> - The number of elements of the BST is between `1` to `10^4`.
> - You may assume `k` is always valid, `1 ≤ k ≤ BST's total elements`.

```java
class Solution {
  public ArrayList<Integer> inorder(TreeNode root, ArrayList<Integer> arr) {
    if (root == null) return arr;
    inorder(root.left, arr);
    arr.add(root.val);
    inorder(root.right, arr);
    return arr;
  }

  public int kthSmallest(TreeNode root, int k) {
    ArrayList<Integer> nums = inorder(root, new ArrayList<Integer>());
    return nums.get(k - 1);
  }
}
```

```java
// 不用数组。
class Solution {
  int k, x=0;
    
  public void inorder(TreeNode root) {
    if (root==null || k<=0) {
        return;
    }
      
    inorder(root.left);
    
    if (--k == 0) {
        x = root.val; // 如果直接作为返回值返回的话，其实不好处理，这里选择放在一个“全局变量”中。
        return;
    }
      
    inorder(root.right);
  }

  public int kthSmallest(TreeNode root, int k) {
    this.k = k;
    inorder(root);
    return x;
  }
}
```

```java
// 迭代版中序遍历。
class Solution {
  public int kthSmallest(TreeNode root, int k) {
    Deque<TreeNode> stack = new ArrayDeque<>();

    while (true) {
      while (root != null) {
        stack.addFirst(root);
        root = root.left;
      }
      root = stack.removeFirst();
      if (--k == 0) return root.val;
      root = root.right;
    }
  }
}
```

> #### Follow up
>
> > What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
>
> [Insert](https://leetcode.com/articles/insert-into-a-bst/) and [delete](https://leetcode.com/articles/delete-node-in-a-bst/) in a BST were discussed last week, the time complexity of these operations is O(*H*), where H*H* is a height of binary tree, and *H*=log*N* for the balanced tree.
>
> Hence without any optimisation insert/delete + search of kth element has O(2*H*+*k*) complexity. How to optimise that?
>
> That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :
>
> - Insert
> - Delete
> - Find kth smallest
>
> **Seems like a database description, isn't it? Let's use here the same logic as for [LRU cache](https://leetcode.com/articles/lru-cache/) design, and combine an indexing structure (we could keep BST here) with a double linked list.**
>
> Such a structure would provide:
>
> - O(*H*) time for the insert and delete.
> - O(*k*) for the search of kth smallest.
>
> ![bla](https://leetcode.com/problems/kth-smallest-element-in-a-bst/Figures/230/linked_list2.png)
>
> The overall time complexity for insert/delete + search of kth smallest is O(*H*+*k*) instead of O(2*H*+*k*).
>
> **Complexity Analysis**
>
> - Time complexity for insert/delete + search of kth smallest: O(*H*+*k*), where *H* is a tree height. O(log*N*+*k*) in the average case, O(*N*+*k*) in the worst case.
> - Space complexity : O(*N*) to keep the linked list.

# [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

> Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
>
> Basically, the deletion can be divided into two stages:
>
> 1. Search for a node to remove.
> 2. If the node is found, delete the node.
>
> 
>
> **Note:** Time complexity should be O(height of tree).
>
> **Example:**
>
> ```
> root = [5,3,6,2,4,null,7]
> key = 3
> 
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> 
> Given key to delete is 3. So we find the node with value 3 and delete it.
> 
> One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
> 
>     5
>    / \
>   4   6
>  /     \
> 2       7
> 
> Another valid answer is [5,2,6,null,4,null,7].
> 
>     5
>    / \
>   2   6
>    \   \
>     4   7
> ```

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }
        if (root.val == key) {
            if (root.left==null && root.right==null) {
                return null;
            } else if (root.left==null || root.right==null) {
                return root.left!=null? root.left: root.right;
            } else {
                // 用右子树最小的结点作为新根。
                int min = findMin(root.right);
                root.val = min;
                root.right = deleteNode(root.right, min);
            }
        } else if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else {
            root.right = deleteNode(root.right, key);
        }
        return root;
    }
    
    private int findMin(TreeNode root) {
        // 最左结点最小。
        while (root.left != null) {
            root = root.left;
        }
        return root.val;
    }
}
```

# 33. 二叉搜索树的后序遍历序列

> 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
>
> 参考以下这颗二叉搜索树：
>
>          5
>         / \
>        2   6
>       / \
>      1   3
>
> 示例 1：
>
> 输入: [1,6,3,2,5]
>
> 输出: false
>
> 示例 2：
>
> 输入: [1,3,2,6,5]
>
> 输出: true
>
>
> 提示：
>
> 数组长度 <= 1000

```java
// 复杂度分析：
// 时间复杂度 O(N^2) ：最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用 O(N) ，对每个结点都会调用一次recur(i,j)，所以总的时间复杂度为O(N^2)。
// 空间复杂度 O(N) ： 最差情况下（即当树退化为链表），递归深度将达到 N 。
class Solution {
    public boolean verifyPostorder(int[] postorder) {
        // 后序序列中，左右根，根在最后。
        return recur(postorder, 0, postorder.length - 1);
    }
    
    boolean recur(int[] postorder, int i, int j) {
        if(i >= j) return true;
        int p = i;
        while(postorder[p] < postorder[j]) p++; // 左子树都小于根。
        int m = p;
        while(postorder[p] > postorder[j]) p++; // 右子树都大于根。
        // `p==j`检查了树[i, j]中，连续的小于根postorder[j]的结点数和连续的大于根的结点数加起来等于j-i个。
        // 体现了bst的性质。
        return p == j && recur(postorder, i, m - 1) && recur(postorder, m, j - 1);
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

# [1373. Maximum Sum BST in Binary Tree](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)

> Given a **binary tree** `root`, the task is to return the maximum sum of all keys of **any** sub-tree which is also a Binary Search Tree (BST).
>
> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys **less than** the node's key.
> - The right subtree of a node contains only nodes with keys **greater than** the node's key.
> - Both the left and right subtrees must also be binary search trees.
>
>  
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2020/01/30/sample_1_1709.png)
>
> ```
> Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
> Output: 20
> Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
> ```
>
> **Example 2:**
>
> ![img](https://assets.leetcode.com/uploads/2020/01/30/sample_2_1709.png)
>
> ```
> Input: root = [4,3,null,1,2]
> Output: 2
> Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
> ```
>
> **Example 3:**
>
> ```
> Input: root = [-4,-2,-5]
> Output: 0
> Explanation: All values are negatives. Return an empty BST.
> ```
>
> **Example 4:**
>
> ```
> Input: root = [2,1,3]
> Output: 6
> ```
>
> **Example 5:**
>
> ```
> Input: root = [5,4,8,3,null,6,3]
> Output: 7
> ```
>
>  
>
> **Constraints:**
>
> - The given binary tree will have between `1` and `40000` nodes.
> - Each node's value is between `[-4 * 10^4 , 4 * 10^4]`.

```java
// 存在bug的实现，这个思路其实采用了98. Validate Binary Search Tree的思路，问题在于，和后者不同的是，这道题在知道某子树不是其根的子BST时，还需要继续往下考察子树是否自己是BST。
// 下面的实现的bug在于，A、B处递归调用的范围参数的问题，如果该子树是其根的右子树，但其根的左子树不是其根的子BST，也就是其根并不是BST，但这里还是采用了基于其根的较窄的范围，而不是[MIN_VALUE, MAX_VALUE]，从而导致错判该子树的左右子树并不是该子树根的子BST，导致错误地没有求出该BST的和，覆盖maxSum，从而导致求出的maxSum偏小。
class Solution {
    private int maxSum=0;
    
    public int maxSumBST(TreeNode root) {
        dfs(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        return maxSum;
    }
    
    // 递归函数的输入是一棵树和一个范围，输出是这棵树的和，如果这棵树是一棵BST的话，否则返回null告诉上层根该子树不是BST，这样上层根就不会采用这棵非BST子树的和。
    // root树的所有结点的值必须在(l, r)范围内。
    private int[] dfs(TreeNode root, int l, int r) {
        if (root == null) {
            return new int[]{0};
        }
        boolean isSubBST = true;
        if (root.val<=l || root.val>=r) {
            // 该树不是上层根的BST子树，故上层输入的范围不再限制这棵树。
            l = Integer.MIN_VALUE;
            r = Integer.MAX_VALUE;
            isSubBST = false;
        }
        int sum = root.val;
        int[] leftSum = dfs(root.left, l, root.val); // A
        int[] rightSum = dfs(root.right, root.val, r); // B
        if (leftSum!=null && rightSum!=null) {
            sum += leftSum[0] + rightSum[0];
            if (sum > maxSum) {
                maxSum = sum;
            }
        } else {
            isSubBST = false;
        }
        return isSubBST? new int[]{sum}: null; // 因为结点值包含负数，所以不能返回-1告诉上层根表示该子树不是BST。
    }
}
```

```java
// 另一个角度，返回树最小值最大值，供上层检查该树是否是其子BST树。
class Solution {
    private int maxSum=0;
    
    public int maxSumBST(TreeNode root) {
        dfs(root);
        return maxSum;
    }
    
    // 递归函数的输入是一棵树，返回[sum, min, max]。如果这棵树是一棵BST的话，返回该树的和，否则返回null告诉上层根该子树不是BST，这样上层根就不会采用这棵非BST子树的和。
    private int[] dfs(TreeNode root) {
        if (root == null) {
            return new int[]{0, Integer.MAX_VALUE, Integer.MIN_VALUE};
        }
        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        // 根据返回值，查看左右子树是否都是BST。
        if (left==null || right==null || left[2]>=root.val || right[1]<=root.val) {
            return null;
        }
        int sum = root.val+left[0]+right[0];
        maxSum = Math.max(maxSum, sum);
        return new int[]{sum, Math.min(left[1], root.val), Math.max(right[2], root.val)};
    }
}
```

