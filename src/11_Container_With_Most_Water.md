# 11. Container With Most Water

> Given *n* non-negative integers *a1*, *a2*, ..., *an* , where each represents a point at coordinate (*i*, *ai*). *n* vertical lines are drawn such that the two endpoints of line *i* is at (*i*, *ai*) and (*i*, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
>
> **Note:** You may not slant the container and *n* is at least 2.
>
>  
>
> ![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
>
> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
>
>  
>
> **Example:**
>
> ```
> Input: [1,8,6,2,5,4,8,3,7]
> Output: 49
> ```

1. Medium，首尾双指针，贪心（先让底边最大，每次先移动短板）。

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int p=0, q=height.size()-1, ans=INT_MIN;
        while (p < q) {
            ans = max(ans, (q-p)*min(height[p], height[q]));
            if (height[p] < height[q]) p++;
            else q--;
        }
        return ans;
    }
};
```

