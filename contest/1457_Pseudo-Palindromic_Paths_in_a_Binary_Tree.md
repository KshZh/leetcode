# 1457. Pseudo-Palindromic Paths in a Binary Tree

> Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be **pseudo-palindromic** if at least one permutation of the node values in the path is a palindrome.
>
> *Return the number of **pseudo-palindromic** paths going from the root node to leaf nodes.*
>
>  
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2020/05/06/palindromic_paths_1.png)
>
> ```
> Input: root = [2,3,1,3,1,null,1]
> Output: 2 
> Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
> ```
>
> **Example 2:**
>
> **![img](https://assets.leetcode.com/uploads/2020/05/07/palindromic_paths_2.png)**
>
> ```
> Input: root = [2,1,1,1,3,null,null,null,null,null,1]
> Output: 1 
> Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
> ```
>
> **Example 3:**
>
> ```
> Input: root = [9]
> Output: 1
> ```
>
>  
>
> **Constraints:**
>
> - The given binary tree will have between `1` and `10^5` nodes.
> - Node values are digits from `1` to `9`.

```java
class Solution {
    // 对路径上的结点值进行计数，如果所有数字出现次数都为偶数，或者仅有一个数字出现奇数次，
    // 那么该路径上的结点值就可以被重新组织成一个回文数，该路径就是题目说的伪回文路径。
    
    // 因为结点值是可枚举的1-9，所以可以直接用数组来计数，而不必用哈希表。
    private int[] cnt = new int[10];
    
    public int pseudoPalindromicPaths(TreeNode root) {
        if (root == null) {
            return 0;
        }
        cnt[root.val]++;
        if (root.left==null && root.right==null) {
            int numOdd = 0;
            for (int i=1; i<=9; i++) {
                if (cnt[i]%2 == 1) {
                    numOdd++;
                    if (numOdd > 1) {
                        cnt[root.val]--;
                        return 0;
                    }
                }
            }
            cnt[root.val]--;
            return 1;
        }
        int res = pseudoPalindromicPaths(root.left)+pseudoPalindromicPaths(root.right);
        cnt[root.val]--;
        return res;
    }
}
```

```java
// 不用数组的解法，用位向量，以及利用偶数个相等的数异或为0的性质。
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/648534/JavaC%2B%2BPython-At-most-one-odd-occurrence
public int pseudoPalindromicPaths (TreeNode root) {
    return dfs(root, 0);
}

private int dfs(TreeNode root, int count) {
    if (root == null) return 0;
    count ^= 1 << (root.val - 1);
    int res = dfs(root.left, count) + dfs(root.right, count);
    // 叶子结点，检查count向量中是否没有1或者仅有一个1，x&(x-1)可以清除x中低位上的第一个1，-1相当于+全1，若x为1010，则x-1为1001，相与得到1000。如果返回的是0，那说明原x中只有一个1或者没有1，被清除后，得到0。
    if (root.left == root.right && (count & (count - 1)) == 0) res++;
    count ^= 1 << (root.val - 1);
    return res;
}
```

