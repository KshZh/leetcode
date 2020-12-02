# 215. Kth Largest Element in an Array

> Find the **k**th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
>
> **Example 1:**
>
> ```
> Input: [3,2,1,5,6,4] and k = 2
> Output: 5
> ```
>
> **Example 2:**
>
> ```
> Input: [3,2,3,1,2,4,5,5,6] and k = 4
> Output: 4
> ```
>
> **Note:**
> You may assume k is always valid, 1 ≤ k ≤ array's length.

1. Medium。

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), std::greater<int>());
        return nums[k-1];
    }
};
```

```cpp
// 维护一个大小为k的最小堆，之后堆顶就是第k个最大的数。
// 也可以维护一个大小为N的最大堆，然后pop()k次。
// 但第一个思路比较好，时间复杂度是O(Nlogk)。
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // priority_queue的默认构造函数是最大堆。
        priority_queue<int, vector<int>, greater<int>> q;
        for (int num: nums) {
            q.push(num);
            if (q.size() > k)
                q.pop();
        }
        return q.top();
    }
};
```

```cpp
// O(N)，最坏O(N^2)。
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int l=0, r=nums.size()-1, pivot;
        while (l < r) {
            pivot = partition(nums, l, r);
            if (pivot == k-1) return nums[pivot];
            else if (pivot < k-1) l = pivot+1; // 说明需要纳入更多的比较大的元素，让l往右缩小范围，然后除了pivot及左边的比较大的元素，再纳入一些。
            else r = pivot-1;
        }
        return nums[l];
    }
    
    // [l, r];
    int partition(vector<int>& nums, int l, int r) {
        int x=nums[r], i, j;
        for (i=j=0; j<r; j++) {
            // 这里要>=，这样[3, 3, 3, 3, 3]这样的测试用例才能过，否则i一直不动。
            if (nums[j] >= x) { // 如果是<x，那么j就直接走过去，留下这些slot让i存储>=x的元素。
                swap(nums[i++], nums[j]);
            }
        }
        swap(nums[i], nums[r]);
        return i;
    }
};
```

