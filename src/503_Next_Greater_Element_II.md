# 503. Next Greater Element II

> Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
>
> **Example 1:**
>
> ```
> Input: [1,2,1]
> Output: [2,-1,2]
> Explanation: The first 1's next greater number is 2; The number 2 can't find next greater number; The second 1's next greater number needs to search circularly, which is also 2.
> ```

1. Medium，栈。
2. 两个选择，存储下标或者存储元素，这里因为要填充另一个数组的下标相同的位置，所以在栈中存储下标。

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        // 暴力破解。
        int i, j, n=nums.size();
        vector<int> res(n);
        for (i=0; i<n; i++) {
            for (j=1; j<n; j++) { // 去掉0和n，因为`(i+0)%n`和`(i+n)%n`都等于i本身。
                if (nums[(i+j)%n] > nums[i]) {
                    res[i] = nums[(i+j)%n];
                    break;
                }
            }
            if (j == n)
                res[i] = -1;
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int i, n=nums.size();
        vector<int> res(n, -1), stack;
        for (i=0; i<n*2; i++) { // 切开环形数组，铺平，所以是n*2。
            while (!stack.empty() && nums[stack.back()]<nums[i%n]) {
                res[stack.back()] = nums[i%n];
                stack.pop_back();
            }
            if (i < n) stack.push_back(i); // 注意用`i<n`使得推入一遍就够了。
        }
        return res;
    }
};
```

