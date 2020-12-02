# 518. Coin Change 2

> You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
>
> **Example 1:**
>
> ```
> Input: amount = 5, coins = [1, 2, 5]
> Output: 4
> Explanation: there are four ways to make up the amount:
> 5=5
> 5=2+2+1
> 5=2+1+1+1
> 5=1+1+1+1+1
> ```
>
> **Example 2:**
>
> ```
> Input: amount = 3, coins = [2]
> Output: 0
> Explanation: the amount of 3 cannot be made up just with coins of 2.
> ```
>
> **Example 3:**
>
> ```
> Input: amount = 10, coins = [10] 
> Output: 1
> ```
>
> **Note:**
>
> You can assume that
>
> - 0 <= amount <= 5000
> - 1 <= coin <= 5000
> - the number of coins is less than 500
> - the answer is guaranteed to fit into signed 32-bit integer

1. Medium，完全背包问题。

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // dp[i][j]表示在前i个coin中选取若干个，使得数额j为0的不同组合有多少个。
        // 若无法找到这样的组合，则dp[i][j]为0。
        vector<int> dp(amount+1);
        dp[0] = 1; // 边界是dp[i][0]为1，因为将数额兑换到0，所以是一条合法的路径。
        // 遍历每一行，每次遍历行都要更新每一列dp[j]。（更新不一定是覆盖，可以累加，看具体问题）
        for (int coin: coins) {
            for (int j=coin; j<=amount; j++) {
                dp[j] += dp[j-coin]; // 使用了coin，然后j-coin有几种兑换组合，j就会多几种，因为只要j-coin的那几种兑换组合都加上一个coin即可得到j。
            }
        }
        return dp[amount];
    }
}
```

```cpp
// 从问题出发/记忆化搜索，比较慢。
class Solution {
    unordered_map<int, unordered_map<int, int>> book;
public:
    int change(int amount, vector<int>& coins) {
        return dfs(amount, 0, coins);
    }
    
    int dfs(int amount, int i, vector<int>& coins) {
        if (amount == 0) return 1;
        if (amount<0 || i>=coins.size()) return 0; // 将amount兑换到负值，说明这不是一条有效的路径。
        if (book.find(amount)!=book.end() && book[amount].find(i)!=book[amount].end()) return book[amount][i];
        int cnt = 0;
        for (int j=i; j<coins.size(); j++) {
            cnt += dfs(amount-coins[j], j, coins);
        }
        book[amount][i] = cnt;
        return cnt;
    }
};
```

