# 1052. Grumpy Bookstore Owner

> Today, the bookstore owner has a store open for `customers.length` minutes. Every minute, some number of customers (`customers[i]`) enter the store, and all those customers leave after the end of that minute.
>
> On some minutes, the bookstore owner is grumpy. If the bookstore owner is grumpy on the i-th minute, `grumpy[i] = 1`, otherwise `grumpy[i] = 0`. When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
>
> The bookstore owner knows a secret technique to keep themselves not grumpy for `X` minutes straight, but can only use it once.
>
> Return the maximum number of customers that can be satisfied throughout the day.
>
> **Example 1:**
>
> ```
> Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
> Output: 16
> Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
> The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
> ```

1. 滑动窗口，Medium。
2. 因为在暴躁的分钟里，客人肯定是满意的。也就是我们只需要关注用那个技能来消除暴躁的分钟，使得换得得满意得客人最多。

```cpp
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int satisfied = 0, win = 0, maxWin = INT_MIN;
        for (int i=0; i<customers.size(); i++) { // `i++`隐含地推进窗口的右端点。
            if (grumpy[i] == 0) satisfied += customers[i];
            else win += customers[i];
            if (i>=X && grumpy[i-X]==1) win -= customers[i-X]; // 推进窗口左端点。
            if (win > maxWin) maxWin = win;
        }
        return satisfied+maxWin; // 分为两部分，一部分是肯定满意的客人数，另一部分是用那个技能换得的满意的客人数。
    }
};
```

