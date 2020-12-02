# 347. Top K Frequent Elements

> Given a non-empty array of integers, return the ***k\*** most frequent elements.
>
> **Example 1:**
>
> ```
> Input: nums = [1,1,1,2,2,3], k = 2
> Output: [1,2]
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1], k = 1
> Output: [1]
> ```
>
> **Note:**
>
> - You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
> - Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.

1. Medium。

```cpp
// 用哈希表统计频率需要O(N)，最终要好于O(NlogN)，那么不能使用排序提取前k个元素，也不能用红黑树提取，因为插入和查找都是O(logN)，总的还是O(NlogN)，
// 这里考虑最小堆，一般建堆有两种方法，一是一个一个插入，需要O(NlogN)，另一种是建立一个包含全部元素的没有堆性质的堆，然后从最后一个有孩子的结点开始向根逐个调整出堆的性质，这种需要O(N)。因为用了标准库的优先队列，所以只能是第一种。然后只要维持堆的大小是k，就可以达到查找和删除是O(logk)，最终是O(Nlogk)。
// 那为什么不能控制红黑树的大小为k呢？因为红黑树是在统计阶段就要建立的，此时还无法确定那些结点可以删掉。
auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
    return a.second > b.second;
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;
        for (int x: nums) frequency[x]++;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> q(cmp);
        for (auto& p: frequency) {
            q.push(p); // 一定要先插入堆，然后挤出最小的那个到堆根，之后删掉最小的元素。
            if (q.size() > k)
                q.pop();
        }
        vector<int> ans(k);
        for (int i=0; i<k; i++) {
            ans[i] = q.top().first;
            q.pop();
        }
        return ans;
    }
};
```

