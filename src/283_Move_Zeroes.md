# 283. Move Zeroes

> Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
>
> **Example:**
>
> ```
> Input: [0,1,0,3,12]
> Output: [1,3,12,0,0]
> ```
>
> **Note**:
>
> 1. You must do this **in-place** without making a copy of the array.
> 2. Minimize the total number of operations.

1. Easy。

```cpp
// 先把所有非零元素移动到最前面，然后将剩余元素填充0。
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int p=0, q=0;
        auto n = nums.size();
        for (; p<n; p++) {
            if (nums[p]!=0) {
                nums[q++] = nums[p];
            }
        }
        for (; q<n; q++)
            nums[q] = 0;
    }
};
```

```cpp
// 双指针。
// 写操作比上一个实现少。
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int p=0, q=0;
        auto n = nums.size();
        while (p<n && q<n) {
            if (nums[q] == 0) { // q先走到一个非零元素处，这时p和q之间都是0，q指向一个0元素。
                q++;
            } else {
                std::swap(nums[p++], nums[q++]); // 可能p和q指向同一个元素，这时p和q一起走。
            }
        }
    }
};
```

