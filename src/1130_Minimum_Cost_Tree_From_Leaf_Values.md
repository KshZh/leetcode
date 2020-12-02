# 1130. Minimum Cost Tree From Leaf Values

> Given an array `arr` of positive integers, consider all binary trees such that:
>
> - Each node has either 0 or 2 children;
> - The values of `arr` correspond to the values of each **leaf** in an in-order traversal of the tree. *(Recall that a node is a leaf if and only if it has 0 children.)*
> - The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
>
> Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.
>
> ```
> Input: arr = [6,2,4]
> Output: 32
> Explanation:
> There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.
> 
>     24            24
>    /  \          /  \
>   12   4        6    8
>  /  \               / \
> 6    2             2   4
> ```

1. Medium，DP。

2. 记住，对于二叉树的中序遍历序列，对于区间a[k, j]，其中的每一个元素都可以是根（在二叉树无法唯一确定的情况下），而a[k, i]就是其左子树，a[i+1, j]就是其右子树。

3. 注意递归边界的定义。

4. [O(N)非DP解法](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space)，一个点是b只能是左边/左子树**第一个**比a大的元素，或者右边/右子树**第一个**比a大的元素，这是因为题目给出的序列是一棵树的叶子的中序序列，如果不这么限制，盲目地每次都选择所有叶子中最小的两个，然后去掉较小的那一个，如第四份代码，就错了，因为这样生成的树的叶子的中序序列和输入不符，即使它产生的非叶结点的权和更小。其中找到第一个比a大的元素和题目[496. Next Greater Element I](./src/496_Next_Greater_Element_I.md)和[503. Next Greater Element II](./src/503_Next_Greater_Element_II.md)算法类似。

   > **Intuition**
   >
   > When we build a node in the tree, we compared the two numbers `a` and `b`. In this process, the smaller one is removed and we won't use it anymore, and the bigger one actually stays.
   >
   > The problem can translated as following: Given an array `A`, choose two neighbors in the array `a` and `b`, we can remove the smaller one `min(a,b)` and the cost is `a * b`. What is the minimum cost to remove the whole array until only one left?
   > 
   > To remove a number `a`, it needs a cost `a * b`, where `b >= a`. So `a` has to be removed by a bigger number. We want minimize this cost, so we need to minimize `b`.
   > 
   >`b` has two candidates, the first bigger number on the left, the first bigger number on the right.
   > 
   >The cost to remove `a` is `a * min(left, right)`.
   
5. 第二种解法需要对题目有较好的理解，虽然题目要求返回所有非叶结点的最小权和，但非叶结点从来都是从左右子树中最大的两个叶子结点构造出来的，与左右子树中的非叶节点和非最大的两个叶结点无关。

6. 遍历中序序列，相当于中序遍历二叉树，左根右。虽然这只是叶子的中序序列，但也是一样的。

```cpp
class Solution {
    int memo[41][41];
    int max_[41][41]; // max_[i][j]表示arr[i, j]最大的元素，双闭区间。
public:
    int mctFromLeafValues(vector<int>& arr) {
        memset(memo, -1, sizeof(memo));
        int i, j;
        for (i=0; i<arr.size(); i++) {
            max_[i][i] = arr[i];
            for (j=i+1; j<arr.size(); j++) {
                max_[i][j] = max(max_[i][j-1], arr[j]);
            }
        }
        return dp(0, arr.size()-1); // 双闭区间。
    }
    
    // dp[i][j]表示区间/子树[i, j]的非叶结点的最小权和。
    int dp(int left, int right) {
        if (left == right)
            return 0; // XXX 递归/DP边界，因为只计算非叶子结点权的和，故叶子结点的权认为是0。
        if (memo[left][right] != -1) return memo[left][right];
        int sum = INT_MAX;
        // 枚举根。
        for (int i=left; i<right; i++) { // 虽然是双闭区间，但还是`i<right`，因为这棵树结点的度为0或2，不为1。
            sum = min(sum, max_[left][i]*max_[i+1][right]+dp(left, i)+dp(i+1, right));
        }
        memo[left][right] = sum;
        return sum;
    }
};
```

```cpp
class Solution {
    int dp[41][41];
    int max_[41][41]; // max_[i][j]表示arr[i, j]最大的元素，双闭区间。
public:
    int mctFromLeafValues(vector<int>& arr) {
        // 从边界出发，但这份代码是错误的，因为`dp[i][j] = min(dp[i][j], max_[i][k]*max_[k+1][j]+dp[i][k]+dp[k+1][j]);`会用到还未计算出来的dp[k+1][j]，要么只能先算出区间长度为2的dp，然后算出区间长度为3的dp，……，要么用递归，从问题出发。
        memset(dp, INT_MAX, sizeof(dp));
        int i, j, k;
        for (i=0; i<arr.size(); i++) {
            max_[i][i] = arr[i];
            dp[i][i] = 0;
            for (j=i+1; j<arr.size(); j++) {
                max_[i][j] = max(max_[i][j-1], arr[j]);
            }
        }
        for (i=0; i<arr.size(); i++) {
            for (j=i+1; j<arr.size(); j++) {
                // 双闭区间。
                for (k=i; k<j; k++) {
                    dp[i][j] = min(dp[i][j], max_[i][k]*max_[k+1][j]+dp[i][k]+dp[k+1][j]);
                }
            }
        }
        return dp[0][arr.size()-1];
    }
};
```

```cpp
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        vector<int> stack;
        stack.push_back(INT_MAX); // 哨兵，这样循环中就不必处理栈为空的情况了。
        int i, res=0;
        for (int a: arr) {
            while (stack.back() <= a) {
                i = stack.back();
                stack.pop_back(); // 删掉较小的叶子，不会再被用到了，因为题目说了总是选择左右子树中各自最大的叶子。
                res += i * min(a, stack.back()); // 注意取min，为了得到更小的非叶结点。
            }
            stack.push_back(a);
        }
        // for (i=0; i<stack.size()-1; i++) { // 别忘了栈底是哨兵。
        for (i=1; i<stack.size()-1; i++) {
            res += stack[i]*stack[i+1];
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        priority_queue<int, vector<int>, greater<int>> q;
        for (int a: arr)
            q.push(a);
        int res = 0, a, b;
        while (q.size()>1) {
            a = q.top();
            q.pop();
            b = q.top();
            q.pop();
            res += a*b;
            q.push(a>b? a: b);
        }
        return res;
    }
};
// [7,12,8,10]
// 7*8+8*10+12*10=256 错误
// 7*12+8*10+12*10=284
```

