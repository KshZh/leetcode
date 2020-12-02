# 378. Kth Smallest Element in a Sorted Matrix

> Given a *n* x *n* matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
>
> Note that it is the kth smallest element in the sorted order, not the kth distinct element.
>
> **Example:**
>
> ```
> matrix = [
>    [ 1,  5,  9],
>    [10, 11, 13],
>    [12, 13, 15]
> ],
> k = 8,
> 
> return 13.
> ```
>
> **Note:**
> You may assume k is always valid, 1 ≤ k ≤ n2.

1. Medium。

```cpp
// 最小堆。
auto cmp = [](int a, int b){ return a>b; };

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int, vector<int>, decltype(cmp)> q(cmp);
        for (auto& r: matrix) {
            for (int x: r) {
                q.push(x);
            }
        }
        for (int i=0; i<k-1; i++)
            q.pop();
        return q.top();
    }
};
```

```cpp
// 基于range的二分查找，虽然这里的序列是有序的，但不是一维的，而不方便映射到一维，所以基于range而不基于index。
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        auto n = matrix.size();
        // [l, r)
        int l=matrix[0][0], r=matrix[n-1][n-1]+1, mid, i, j, cnt;
        while (l < r) {
            mid = l+(r-l)/2;
            cnt=0, j=n-1;
            for (i=0; i<n; i++) { // 注意这里，这里巧妙地利用了输入的矩阵在每一行每一列都是递增序列的性质来计数。
                while (j>=0 && matrix[i][j]>mid) j--;
                cnt += j+1;
            }
            if (cnt < k) l=mid+1;
            else r=mid;
        }
        return l;
    }
};
```

