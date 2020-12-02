# 121. Best Time to Buy and Sell Stock

> Say you have an array for which the *i*th element is the price of a given stock on day *i*.
>
> If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
>
> Note that you cannot sell a stock before you buy one.
>
> **Example 1:**
>
> ```
> Input: [7,1,5,3,6,4]
> Output: 5
> Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
>              Not 7-1 = 6, as selling price needs to be larger than buying price.
> ```

1. Easy。

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // if (prices.size() < 1)
        //    return 0;
        int maxprofit = 0;
        // int minprice = prices[0]; // 恰当设置初始值，就不必检查输入是否为空。
        int minprice = INT_MAX;
        // for (int i=1; i<prices.size(); i++) {
        for (int i=0; i<prices.size(); i++) {
            if (prices[i] < minprice) {
                minprice = prices[i];
                continue;
            }
            if (prices[i]-minprice > maxprofit) {
                maxprofit = prices[i]-minprice;
            }
        }
        return maxprofit;
    }
};
```

