# 1394. Find Lucky Integer in an Array

> Given an array of integers `arr`, a lucky integer is an integer which has a frequency in the array equal to its value.
>
> Return *a lucky integer* in the array. If there are multiple lucky integers return the **largest** of them. If there is no lucky integer return **-1**.

1. Easy。

```cpp
// 哈希表计数/reduce。
int findLucky(vector<int>& arr) {
    unordered_map<int, int> cnt;
    for (int x: arr)
        cnt[x]++;
    int max = -1;
    for (auto& p: cnt) {
        if (p.first==p.second && p.first>max)
            max = p.first;
    }
    return max;
}
```

