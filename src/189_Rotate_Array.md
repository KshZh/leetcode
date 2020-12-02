# 189. Rotate Array

> Given an array, rotate the array to the right by *k* steps, where *k* is non-negative.
>
> **Example 1:**
>
> ```
> Input: [1,2,3,4,5,6,7] and k = 3
> Output: [5,6,7,1,2,3,4]
> Explanation:
> rotate 1 steps to the right: [7,1,2,3,4,5,6]
> rotate 2 steps to the right: [6,7,1,2,3,4,5]
> rotate 3 steps to the right: [5,6,7,1,2,3,4]
> ```
>
> **Example 2:**
>
> ```
> Input: [-1,-100,3,99] and k = 2
> Output: [3,99,-1,-100]
> Explanation: 
> rotate 1 steps to the right: [99,-1,-100,3]
> rotate 2 steps to the right: [3,99,-1,-100]
> ```

1. Medium。

#### Approach #3 Using Cyclic Replacements

![](https://leetcode.com/media/original_images/189_Rotate_Array.png)

```java
// O(N), O(N)。
// 考虑k大于n的边界情况。
public class Solution {
    public void rotate(int[] nums, int k) {
        int[] a = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            a[(i + k) % nums.length] = nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = a[i];
        }
    }
}
```

```cpp
// O(N), O(1)。
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        auto n = nums.size();
        k %= n; // 恶意的边界测试。
        int cnt = 0; // 当前有cnt个元素在正确的位置上。
        for (int start=0; cnt<n; start++) {
            int curr = start;
            int prev = nums[curr];
            do {
                curr = (curr+k)%n;
                int temp = nums[curr];
                nums[curr] = prev;
                prev = temp;
                
                cnt++;
            } while (curr != start);
        }
    }
};
```

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        auto n = nums.size();
        k %= n; // 恶意的边界测试。
        reverse(nums, 0, n); // 也可以用std::reverse。
        reverse(nums, 0, k);
        reverse(nums, k, n);
    }
    
    // [start, end)。
    void reverse(vector<int>& nums, int start, int end) {
        while (start < end) {
            std::swap(nums[start++], nums[--end]);
        }
    }
};
```

