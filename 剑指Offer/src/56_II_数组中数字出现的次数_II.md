# 56 - II. 数组中数字出现的次数 II

> 在一个数组 `nums` 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

1. Medium。

```cpp
// 因为没有限制时空复杂度，所以可以用哈希表计数。
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++){
            int count = 0;
            for (auto n : nums){
                if ((1 << i ) & n) count++;
            }
            // 因为其他数字都是成三出现的，所以如果模3剩下一，就说明出现一次的那个数字在第i位上为1，那就把这一位乘上权重累加起来。
            if ((count%3) == 1) ans += (1 << i);
        }
        return ans;
    }
};

// 作者：muyids
// 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/san-jin-zhi-zhuang-tai-ji-by-muyids/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

