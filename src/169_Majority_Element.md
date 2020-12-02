# 169. Majority Element

> Given an array of size *n*, find the majority element. The majority element is the element that appears **more than** `⌊ n/2 ⌋` times.
>
> You may assume that the array is non-empty and the majority element always exist in the array.
>
> **Example 1:**
>
> ```
> Input: [3,2,3]
> Output: 3
> ```
>
> **Example 2:**
>
> ```
> Input: [2,2,1,1,1,2,2]
> Output: 2
> ```

1. Easy。

#### Approach 6: Boyer-Moore Voting Algorithm

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        auto n = nums.size();
        unordered_map<int, int> cnt;
        for (int num: nums) {
            cnt[num]++;
            if (cnt[num] > n/2)
                return num;
        }
        return -1;
    }
};
```

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        return nums[nums.size()/2]; // 有一个元素超过半数，那么排序后，中间一定也是这个超半数的元素。
    }
};
```

```java
// 分治策略，不重叠的子问题。
class Solution {
    private int countInRange(int[] nums, int num, int lo, int hi) {
        int count = 0;
        for (int i = lo; i <= hi; i++) {
            if (nums[i] == num) {
                count++;
            }
        }
        return count;
    }

    private int majorityElementRec(int[] nums, int lo, int hi) {
        // base case; the only element in an array of size 1 is the majority
        // element.
        if (lo == hi) {
            return nums[lo];
        }

        // recurse on left and right halves of this slice.
        int mid = (hi-lo)/2 + lo;
        int left = majorityElementRec(nums, lo, mid);
        int right = majorityElementRec(nums, mid+1, hi);

        // if the two halves agree on the majority element, return it.
        if (left == right) {
            return left;
        }

        // otherwise, count each element and return the "winner".
        int leftCount = countInRange(nums, left, lo, hi);
        int rightCount = countInRange(nums, right, lo, hi);

        return leftCount > rightCount ? left : right;
    }

    public int majorityElement(int[] nums) {
        return majorityElementRec(nums, 0, nums.length-1);
    }
}
```

```cpp
// Approach 6: Boyer-Moore Voting Algorithm
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt=0, candidate;
        for (int num: nums) {
            if (cnt == 0) candidate = num;
            cnt += (num==candidate)? 1: -1;
        }
        return candidate;
    }
};
```

