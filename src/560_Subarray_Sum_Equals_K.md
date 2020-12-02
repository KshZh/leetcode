# 560. Subarray Sum Equals K

> Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.
>
> **Example 1:**
>
> ```
> Input:nums = [1,1,1], k = 2
> Output: 2
> ```
>
> **Note:**
>
> 1. The length of the array is in range [1, 20,000].
> 2. The range of numbers in the array is [-1000, 1000] and the range of the integer **k** is [-1e7, 1e7].

1. Medium。

```cpp
// 暴力破解。
int subarraySum(vector<int>& nums, int k) {
    auto n = nums.size();
    int cnt=0, sum;
    // 枚举连续子序列的起点。
    for (int i=0; i<n; i++) {
        // 枚举连续子序列的终点。
        sum = 0;
        for (int j=i; j<n; j++) {
            sum += nums[j];
            if (sum == k) {
                cnt++;
                // 不能break，因为可能扩展当前的连续子序列，又可以得到一个子序列，其和为k。
                // break;
            }
        }
    }
    return cnt;
}
```

```cpp
// 时空为O(N)的解法。
// 哈希表中的key是目前出现过的前缀和（前缀和从下标0开始），value是出现次数。
// 若map[sum-k]为2，说明出现过两个前缀和sumX，使得sumX+k=sum，也就是有两段连续子序列的和为k。（从前缀和结束的下标后的下标开始，到当前下标的这段连续子序列）
int subarraySum(vector<int>& nums, int k) {
    auto n = nums.size();
    int cnt=0, sum=0;
    unordered_map<int, int> prefixSum{{0, 1}};
    for (int i=0; i<n; i++) {
        sum += nums[i];
        if (prefixSum.find(sum-k) != prefixSum.end()) {
            cnt += prefixSum[sum-k];
        }
        prefixSum[sum]++;
    }
    return cnt;
}
```

