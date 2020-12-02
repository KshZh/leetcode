# 496. Next Greater Element I

> You are given two arrays **(without duplicates)** `nums1` and `nums2` where `nums1`’s elements are subset of `nums2`. Find all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`.
>
> The Next Greater Number of a number **x** in `nums1` is the first greater number to its right in `nums2`. If it does not exist, output -1 for this number.
>
> **Example 1:**
>
> ```
> Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
> Output: [-1,3,-1]
> ```

1. Easy，栈。
2. 本质上，我们需要一个容器存储未确定比它大的元素的元素，不能使用队列，否则无法处理`[9, 6, 5, 7, 10]`这种输入，会误判比5和6大的元素是10。这里栈是理想的容器，配合下面的算法，我们总是在栈中维护了一段**降序的序列**。

```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> stack, res;
        stack.push_back(INT_MAX); // 哨兵，这样循环中就不必判断栈是否未空。
        unordered_map<int, int> m;
        for (int i=0; i<nums2.size(); i++) {
            while (stack.back() < nums2[i]) {
                m[stack.back()] = nums2[i];
                stack.pop_back(); // 已确定比该元素大的元素，故从栈中弹出。
            }
            stack.push_back(nums2[i]);
        }
        for (int i=0; i<nums1.size(); i++) {
            if (m.find(nums1[i]) == m.end())
                res.push_back(-1);
            else
                res.push_back(m[nums1[i]]);
        }
        return res;
    }
};
```

