# 698. Partition to K Equal Sum Subsets

> Given an array of integers `nums` and a positive integer `k`, find whether it's possible to divide this array into `k` non-empty subsets whose sums are all equal.
>
> **Example 1:**
>
> ```
> Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
> Output: True
> Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
> ```
>
> **Note:**
>
> - `1 <= k <= len(nums) <= 16`.
> - `0 < nums[i] < 10000`.

1. Medium。
2. TODO：dp解法没看懂。

```cpp
bool canPartitionKSubsets(vector<int>& nums, int K) {
    int N = nums.size();
    if (K == 1) return true;
    if (N < K) return false;
    int sum = 0;
    for (int i = 0; i < N; i++) sum += nums[i];
    if (sum % K != 0) return false;

    int subset = sum / K;
    int subsetSum[K];
    bool taken[N];

    for (int i = 0; i < K; i++) subsetSum[i] = 0;
    for (int i = 0; i < N; i++) taken[i] = false;

    subsetSum[0] = nums[N - 1];
    taken[N - 1] = true;

    return canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, 0, N - 1);
}

bool canPartitionKSubsets(vector<int>& nums, int subsetSum[], bool taken[], int subset, int K, int N, int curIdx, int limitIdx) {
    if (subsetSum[curIdx] == subset) {
        if (curIdx == K - 2) return true;
        // 注意这里直接继续递归调用匹配下一个子集，
        // 也就是没有沿路径先返回，那么taken的某些位还是true。
        // 即后面的子集不会用到前面子集用到的元素。
        return canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, curIdx + 1, N - 1);
    }

    // 当前由limitIdx+1种选择。
    for (int i = limitIdx; i >= 0; i--) {
        if (taken[i]) continue;
        int tmp = subsetSum[curIdx] + nums[i];

        if (tmp <= subset) {
            taken[i] = true;
            subsetSum[curIdx] += nums[i];
            bool nxt = canPartitionKSubsets(nums, subsetSum, taken, subset, K, N, curIdx, i - 1);
			if (nxt) return true;
            // 否则，尝试当前的另一种选择。
            taken[i] = false;
            subsetSum[curIdx] -= nums[i];
        }
    }
    return false;
}
```

```java
// 整体就是一个暴力的解法，先算出子集的和是多少，并抽象成k个桶，每个桶的值是子集的和。然后尝试所有不同的组合（即放数到桶中），如果存在一种组合可以使每个桶都正好放下，那么返回可以。如果不存在，返回不可以。
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        //因为题目限制条件不用担心溢出
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
        }
        if(sum % k != 0){
            return false;
        }
        //求出子集的和
        sum = sum / k;
        //排序 小的放最前面大的放最后面
        Arrays.sort(nums);
        //如果子集的和小于数组最大的直接返回false
        if(nums[nums.length - 1] > sum){
            return false;
        }
        //建立一个长度为k的桶
        int[] arr = new int[k];
        //桶的每一个值都是子集的和
        Arrays.fill(arr, sum);
        //从数组最后一个数开始进行递归
        return help(nums, nums.length - 1, arr, k);
    }
    
    boolean help(int[] nums, int cur, int[] arr, int k){
        //已经遍历到了-1说明前面的所有数都正好可以放入桶里，那所有桶的值此时都为0，说明找到了结果，返回true
        if(cur < 0){
            return true;
        }
        //遍历k个桶
        for(int i = 0; i < k; i++){
            //如果正好能放下当前的数或者放下当前的数后，还有机会继续放前面的数（剪枝）
            if(arr[i] == nums[cur] || (cur > 0 && arr[i] - nums[cur] >= nums[0])){
                //放当前的数到桶i里
                arr[i] -= nums[cur];
                //开始放下一个数
                if(help(nums, cur - 1, arr, k)){
                    return true;
                }
                //这个数不该放在桶i中
                //从桶中拿回当前的数
                arr[i] += nums[cur];
            }
        }
        return false;
    }
}
```

