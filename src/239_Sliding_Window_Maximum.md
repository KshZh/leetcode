# 239. Sliding Window Maximum

> Given an array *nums*, there is a sliding window of size *k* which is moving from the very left of the array to the very right. You can only see the *k* numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
>
> **Example:**
>
> ```
> Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
> Output: [3,3,5,5,6,7] 
> Explanation: 
> 
> Window position                Max
> ---------------               -----
> [1  3  -1] -3  5  3  6  7       3
>  1 [3  -1  -3] 5  3  6  7       3
>  1  3 [-1  -3  5] 3  6  7       5
>  1  3  -1 [-3  5  3] 6  7       5
>  1  3  -1  -3 [5  3  6] 7       6
>  1  3  -1  -3  5 [3  6  7]      7
> ```
>
> **Note:**
> You may assume *k* is always valid, 1 ≤ k ≤ input array's size for non-empty array.
>
> **Follow up:**
> Could you solve it in linear time?

1. Hard。

```cpp
// 朴素的下标滑动窗口解法。
// 时间复杂度为O(N*k)。
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    auto n = nums.size();
    vector<int> ret;
    int i, j, a, max=INT_MIN;
    for (i=j=0; i<n; i++) {
        if (i-j==k && nums[j++]==max) {
            max = INT_MIN;
            for (a=j; a<i; a++) {
                if (nums[a] > max) {
                    max = nums[a];
                }
            }
        }
        if (nums[i] > max) {
            max = nums[i];
        }
        if (i+1 >= k) {
            ret.push_back(max);
        }
    }
    return ret;
}
```

```cpp
// 滑动窗口+双端队列。
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> windowMax;
    deque<int> dq;
    for (int i = 0; i < n; i++) {
        while (!dq.empty() && dq.front() < i - k + 1) // 窗口大小超了k，缩小窗口。
            dq.pop_front();
        while (!dq.empty() && nums[dq.back()] < nums[i]) // 去掉窗口中比nums[i]小的值，这些值永远不会再被用到了。这些值位置上在i之前，那么肯定比nums[i]先被淘汰，所以若nums[i]是窗口中最大值，即使nums[i]被淘汰，需要找窗口中另一个最大值也轮不到这些位置上的元素。
            dq.pop_back();  
        dq.push_back(i);
        if (i >= k - 1) windowMax.push_back(nums[dq.front()]);
    }
    return windowMax;
}
```

