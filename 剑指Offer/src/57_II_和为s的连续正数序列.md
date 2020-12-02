# 57 - II. 和为s的连续正数序列

> 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
>
> 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
>
> 示例 1：
>
> 输入：target = 9
> 输出：[[2,3,4],[4,5]]
> 示例 2：
>
> 输入：target = 15
> 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
>
>
> 限制：
>
> 1 <= target <= 10^5
>

1. Easy。

```java
// 滑动窗口。
class Solution {
    public int[][] findContinuousSequence(int target) {
        int windowSum = 0;
        List<int[]> list = new ArrayList<>();
        for (int i=1, j=1; j<target; j++) {
            // 缩小窗口。
            while (windowSum+j > target) {
                windowSum -= i;
                i++;
            }
            windowSum += j;
            if (windowSum == target) {
                int[] x = new int[j-i+1];
                for (int k=i; k<=j; k++) {
                    x[k-i] = k;
                }
                list.add(x);
            }
        }
        int[][] ret = new int[list.size()][];
        for (int i=0; i<list.size(); i++) {
            ret[i] = list.get(i);
        }
        return ret;
    }
}
```

```cpp
// 数学。
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> vec;
        vector<int> res;
        int sum = 0, limit = (target - 1) / 2; // (target - 1) / 2 等效于 target / 2 下取整
        for (int x = 1; x <= limit; ++x) {
            long long delta = 1 - 4 * (x - 1ll * x * x - 2 * target);
            if (delta < 0) continue;
            int delta_sqrt = (int)sqrt(delta + 0.5);
            if (1ll * delta_sqrt * delta_sqrt == delta && (delta_sqrt - 1) % 2 == 0){
                int y = (-1 + delta_sqrt) / 2; // 另一个解(-1-delta_sqrt)/2必然小于0，不用考虑
                if (x < y) {
                    res.clear();
                    for (int i = x; i <= y; ++i) res.emplace_back(i);
                    vec.emplace_back(std::move(res));
                }
            }
        }
        return vec;
    }
};

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/mian-shi-ti-57-ii-he-wei-sde-lian-xu-zheng-shu-x-2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

