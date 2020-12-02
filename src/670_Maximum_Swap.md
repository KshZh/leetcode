# 670. Maximum Swap

> Given a non-negative integer, you could swap two digits **at most** once to get the maximum valued number. Return the maximum valued number you could get.
>
> **Example 1:**
>
> ```
> Input: 2736
> Output: 7236
> Explanation: Swap the number 2 and the number 7.
> ```
>
> **Example 2:**
>
> ```
> Input: 9973
> Output: 9973
> Explanation: No swap.
> ```
>
> **Note:**
>
> 1. The given number is in the range [0, 10^8]

1. Medium，贪心。
2. 别被例子骗了，以为只是交换相邻元素。
3. 虽然一看就知道可以用贪心，但贪心并不好想和实现。而因为最多有8位数，所以**最多有`C(8, 2)=28`中交换组合，所以可以直接用暴力枚举**。

```cpp
// 时间复杂度O(N^3)，空间复杂度O(N)。
class Solution {
public:
    int maximumSwap(int num) {
        vector<int> v;
        while (num) {
            v.push_back(num%10);
            num /= 10;
        }
        auto n = v.size();
        vector<int> ans(v);
        for (int i=n-1; i>0; i--) {
            for (int j=i-1; j>=0; j--) {
                int temp = v[i];
                v[i] = v[j];
                v[j] = temp;
                for (int k=n-1; k>=0; k--) {
                    if (v[k] != ans[k]) { // 碰到第一个不相等的元素，就该退出循环了。
                        if (v[k] > ans[k])
                            ans = v;
                        break;
                    }
                }
                // restore.
                v[j] = v[i];
                v[i] = temp;
            }
        }
        for (int i=n-1; i>=0; i--) {
            num = num*10 + ans[i];
        }
        return num;
    }
};
```

```cpp
// 贪心+数组。
class Solution {
public:
    int maximumSwap(int num) {
        vector<int> v;
        int temp = num;
        while (num) {
            v.push_back(num%10);
            num /= 10;
        }
        auto n = v.size();
        vector<int> last(10, INT_MAX); // 数字[0, 9]在v中的下标。
        for (int i=n-1; i>=0; i--) {
            last[v[i]] = i; // 如果有v中有两个或以上的元素相等，那么对应的last值是最小的i。到时候交换的时候，代价是比较小的权上的位。（贪心）
        }
        // 从最高有效位开始，因为最高有效位权最大。（贪心）
        for (int i=n-1; i>=0; i--) {
            for (int d=9; d>v[i]; d--) {
                if (last[d] < i) {
                    swap(v[i], v[last[d]]);
                    for (int j=n-1; j>=0; j--)
                        num = num*10 + v[j];
                    return num;
                }
            }
        }
        return temp; // 不需要swap的情况。
    }
};
```

