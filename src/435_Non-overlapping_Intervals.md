# 435. Non-overlapping Intervals

> Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
>
> **Example 1:**
>
> ```
> Input: [[1,2],[2,3],[3,4],[1,3]]
> Output: 1
> Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
> ```
>
> **Example 2:**
>
> ```
> Input: [[1,2],[1,2],[1,2]]
> Output: 2
> Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
> ```
>
> **Example 3:**
>
> ```
> Input: [[1,2],[2,3]]
> Output: 0
> Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
> ```
>
> **Note:**
>
> 1. You may assume the interval's end point is always bigger than its start point.
> 2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

1. Medium。

2. 类似问题[56. Merge Intervals](./56_Merge_Intervals.md).

3. [思路](https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization)：

   > Several algorithms, that may look promising at first sight, actually do not find the optimal solution:
   >
   > - Selecting the intervals that start earliest is not an optimal solution, because if the earliest interval happens to be very long, accepting it would make us reject many other shorter requests.
   > - Selecting the shortest intervals or selecting intervals with the fewest conflicts is also not optimal.
   >
   > ### Greedy polynomial solution
   >
   > ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/IntervalSelection.svg/30px-IntervalSelection.svg.png)
   >
   > The following [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm) does find the optimal solution:
   >
   > 1. Select the interval, *x*, with the earliest **finishing time**.
   > 2. Remove *x*, and all intervals intersecting *x*, from the set of candidate intervals.
   > 3. Repeat until the set of candidate intervals is empty.
   >
   > Whenever we select an interval at step 1, we may have to remove many intervals in step 2. However, all these intervals necessarily cross the finishing time of *x*, and thus they all cross each other (see figure). Hence, at most 1 of these intervals can be in the optimal solution. Hence, for every interval in the optimal solution, there is an interval in the greedy solution. This proves that the greedy algorithm indeed finds an optimal solution.
   >
   > A more formal explanation is given by a [Charging argument](https://en.wikipedia.org/wiki/Charging_argument).
   >
   > The greedy algorithm can be executed in time O(*n* log *n*), where *n* is the number of tasks, using a preprocessing step in which the tasks are sorted by their finishing times.

```cpp
class Solution {
public:
    // 区间是左闭右开区间。
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b){
                 // if (a[0] != b[0]) return a[0]<b[0];
                 return a[1]<b[1]; });
        int right = intervals[0][1];
        int n = 0;
        // 注意是`it!=intervals.end()`，即每次循环都要重新计算内存地址，
        // 因为在循环中删除中间元素可能导致元素前移。
        // 还要注意`it++`不能放在for中。
        for (auto it=intervals.begin()+1; it!=intervals.end(); ) {
            if ((*it)[0] >= right) {
                // 不相交。
                right = (*it)[1];
                it++;
            } else {
                // 相交。
                // 返回的it指向被删除元素后的元素，如果被删除元素就是最后一个元素，那么返回end()。
                it = intervals.erase(it);
                n++;
            }
        }
        return n;
    }
};
```

```cpp
class Solution {
public:
    // 区间是左闭右开区间。
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b){
                 // if (a[0] != b[0]) return a[0]<b[0];
                 return a[1]<b[1]; });
        int right = intervals[0][1];
        int n = 0;
        for (int i=1; i<intervals.size(); i++) {
            if (intervals[i][0] >= right) {
                // 不相交。
                right = intervals[i][1];
            } else {
                // 相交，删掉，实际上并不需要真的删掉，只要不更新right并跳过它即可。
                n++;
            }
        }
        return n;
    }
};
```

