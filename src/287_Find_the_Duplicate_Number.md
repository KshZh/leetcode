# 287. Find the Duplicate Number

> Given an array *nums* containing *n* + 1 integers where each integer is between 1 and *n* (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
>
> **Example 1:**
>
> ```
> Input: [1,3,4,2,2]
> Output: 2
> ```
>
> **Example 2:**
>
> ```
> Input: [3,1,3,4,2]
> Output: 3
> ```
>
> **Note:**
>
> 1. You **must not** modify the array (assume the array is read only).
> 2. You must use only constant, *O*(1) extra space.
> 3. Your runtime complexity should be less than *O*(*n*^2).
> 4. There is only one duplicate number in the array, but it could be repeated more than once.

1. Medium。
2. \[1, n\]有n个元素，而nums包含n+1个元素，有且仅有一个元素重复了一次，那么隐含地说明\[1, n\]中每个元素都会出现。
3. 因为要求常数空间复杂度，所以不能用哈希表。因为不能修改输入数组，所以不能用排序。

#### Approach #3 Floyd's Tortoise and Hare (Cycle Detection) [Accepted]

**Intuition**

If we interpret `nums` such that for each pair of index i and value vi, the "next" value v_j is at index v_i, we can reduce this problem to cycle detection. See the solution to [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/solution/) for more details.

```cpp
// 基于range的二分查找，适用于非有序序列。
// 比如[3,1,3,4,2]，
// 第一轮，mid=2，nums中小于等于mid的元素个数为2，说明重复的元素不在[l, mid]中，往[mid+1, r]中找。
// 第二轮，mid=3，nums中小于等于mid的元素个数为4，说明重复的元素在[l, mid]中，往[l, mid-1]中找。
// 此时`l==r`，循环结束。
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int l=1, r=nums.size(), mid, cnt;
        while (l < r) {
            mid = l+(r-l)/2;
            cnt = 0;
            for (int x: nums) {
                if (x <= mid)
                    cnt++;
            }
            if (cnt <= mid) l = mid+1;
            else r = mid;
        }
        return l;
    }
};
```

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        vector<int>& next = nums; // next[i]是结点i的next值，指向下一个结点。
        int tortoise=next[0], hare=next[0];
        do {
            tortoise = next[tortoise];
            hare = next[next[hare]];
        } while (tortoise != hare);
        int p1=next[0], p2=tortoise;
        while (p1 != p2) {
            p1 = next[p1];
            p2 = next[p2];
        }
        return p1;
    }
};
```

