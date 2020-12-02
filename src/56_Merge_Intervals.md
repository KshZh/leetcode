# 56. Merge Intervals

> Given a collection of intervals, merge all overlapping intervals.
>
> **Example 1:**
>
> ```
> Input: [[1,3],[2,6],[8,10],[15,18]]
> Output: [[1,6],[8,10],[15,18]]
> Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
> ```
>
> **Example 2:**
>
> ```
> Input: [[1,4],[4,5]]
> Output: [[1,5]]
> Explanation: Intervals [1,4] and [4,5] are considered overlapping.
> ```
>
> **NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

1. Medium，排序。

```cpp
class Solution {
public:
    // 区间是左闭右开区间。
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        vector<vector<int>> ans;
        // 按照左闭排序。
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[0]<b[0]; });
        ans.push_back(move(intervals[0]));
        for (int i=1; i<intervals.size(); i++) {
            if (ans.back()[1] < intervals[i][0]) {
                // 不相交。
                ans.push_back(move(intervals[i]));
            } else {
                // 相交。
                ans.back()[1] = max(ans.back()[1], intervals[i][1]);
            }
        }
        return ans;
    }
};
```

