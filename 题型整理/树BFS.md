# [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

> You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
>
> ```
> struct Node {
>   int val;
>   Node *left;
>   Node *right;
>   Node *next;
> }
> ```
>
> Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.
>
> Initially, all next pointers are set to `NULL`.
>
>  
>
> **Follow up:**
>
> - You may only use constant extra space.
> - Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
>
>  
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)
>
> ```
> Input: root = [1,2,3,4,5,6,7]
> Output: [1,#,2,3,#,4,5,6,7,#]
> Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
> ```
>
>  
>
> **Constraints:**
>
> - The number of nodes in the given tree is less than `4096`.
> - `-1000 <= node.val <= 1000`

```java
class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        Queue<Node> queue = new LinkedList<>();
        Node prev, x;
        queue.add(root);
        while (!queue.isEmpty()) {
            prev = null;
            for (int i=queue.size()-1; i>=0; i--) {
                x = queue.remove();
                if (prev != null) {
                    prev.next = x;
                }
                if (x.left != null) {
                    queue.add(x.left);
                    queue.add(x.right);
                }
                prev = x;
            }
        }
        return root;
    }
}
```

```java
// XXX O(1)空间复杂度。
class Solution {
    public Node connect(Node root) {
        Node p=root, temp;
        while (p!=null && p.left!=null) {
            temp = p;
            while (p != null) {
                p.left.next = p.right;
                p.right.next = p.next==null? null: p.next.left;
                p = p.next;
            }
            p = temp.left;
        }
        return root;
    }
}
```

```java
// 递归，先序遍历。
public void connect(TreeLinkNode root) {
    if(root == null)
        return;
        
    if(root.left != null){
        root.left.next = root.right;
        if(root.next != null)
            root.right.next = root.next.left;
    }
    
    connect(root.left);
    connect(root.right);
}
```

# [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

> Given a binary tree, return the *bottom-up level order* traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
>
> For example:
> Given binary tree `[3,9,20,null,null,15,7]`,
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> 
>
> return its bottom-up level order traversal as:
>
> ```
> [
>   [15,7],
>   [9,20],
>   [3]
> ]
> ```

```java
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        TreeNode x;
        queue.add(root);
        while (!queue.isEmpty()) {
            List<Integer> l = new ArrayList<>();
            for (int i=queue.size()-1; i>=0; i--) {
                x = queue.remove();
                l.add(x.val);
                if (x.left != null) {
                    queue.add(x.left);
                }
                if (x.right != null) {
                    queue.add(x.right);
                }
            }
            res.add(l);
        }
        Collections.reverse(res);
        return res;
    }
}
```

```java
// dfs，避免使用reverse。
public class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
        levelMaker(wrapList, root, 0);
        return wrapList;
    }

    public void levelMaker(List<List<Integer>> list, TreeNode root, int level) {
        if(root == null) return;
        if(level >= list.size()) {
            list.add(0, new LinkedList<Integer>());
        }
        levelMaker(list, root.left, level+1);
        levelMaker(list, root.right, level+1);
        list.get(list.size()-level-1).add(root.val);
    }
}
```

# [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

> Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
>
> For example:
> Given binary tree `[3,9,20,null,null,15,7]`,
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> 
>
> return its zigzag level order traversal as:
>
> ```
> [
>   [3],
>   [20,9],
>   [15,7]
> ]
> ```

```java
// 顺序、逆序填充数组。
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        queue.add(root);
        TreeNode x;
        boolean flag = true;
        while (!queue.isEmpty()) {
            int n = queue.size();
            // List<Integer> l = new ArrayList<>(n); // XXX 构造函数中的参数是容器的容量，而不是size。
            Integer[] l = new Integer[n];
            for (int i=0; i<n; i++) {
                x = queue.remove();
                // l.add(flag? i: n-i-1, x.val); // java.lang.IndexOutOfBoundsException: Index: 1, Size: 0
                l[flag? i: n-i-1] = x.val;
                if (x.left != null) {
                    queue.add(x.left);
                }
                if (x.right != null) {
                    queue.add(x.right);
                }
            }
            flag = !flag;
            res.add(Arrays.asList(l));
        }
        return res;
    }
}
```

