# 75. Sort Colors

> Given an array with *n* objects colored red, white or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white and blue.
>
> Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
>
> **Note:** You are not suppose to use the library's sort function for this problem.
>
> **Example:**
>
> ```
> Input: [2,0,2,1,1,0]
> Output: [0,0,1,1,2,2]
> ```

1. Medium，首尾双指针。

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        // sort(nums.begin(), nums.end()); // 偷懒，O(NlogN)。
        // 直接计数，然后赋值。
        vector<int> count(3, 0);
        for (int x: nums)
            count[x]++;
        for (int i=0, j=0; i<nums.size(); i++) {
            while (count[j] == 0)
                j++;
            nums[i] = j;
            count[j]--;
        }
    }
};
```

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
		// 三指针，p0指向可放置0的位置，p2指向可放置2的位置，cur指向当前遍历的元素。
        int p0=0, cur=0, p2=nums.size()-1, temp;
        while (cur <= p2) {
            if (nums[cur] == 0) {
                temp = nums[cur];
                nums[cur++] = nums[p0]; // 自增cur，从左边交换过来的元素已经被扫描过了，必然是1。
                nums[p0++] = temp;
            } else if (nums[cur] == 2) {
                temp = nums[cur];
                nums[cur] = nums[p2]; // 注意这里cur不能自增，因为从右边交换过来的元素还没被扫描过，可能也是2或0。
                nums[p2--] = temp;
            } else {
                cur++;
            }
        }
    }
};
```

