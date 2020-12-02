# 877. Stone Game

> Alex and Lee play a game with piles of stones. There are an even number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.
>
> The objective of the game is to end with the most stones. The total number of stones is odd, so there are no ties.
>
> Alex and Lee take turns, with Alex starting first. Each turn, a player takes the entire pile of stones from either the beginning or the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
>
> Assuming Alex and Lee play optimally, return `True` if and only if Alex wins the game.
>
> **Example 1:**
>
> ```
> Input: [5,3,4,5]
> Output: true
> Explanation: 
> Alex starts first, and can only take the first 5 or the last 5.
> Say he takes the first 5, so that the row becomes [3, 4, 5].
> If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
> If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
> This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
> ```
>
> **Note:**
>
> 1. `2 <= piles.length <= 500`
> 2. `piles.length` is even.
> 3. `1 <= piles[i] <= 500`
> 4. `sum(piles)` is odd.

1. Medium。

```cpp
bool stoneGame(vector<int>& piles) {
    auto n = piles.size();
    int i, j, len;
    // dp[i][j]是在piles[i, j]中，第一个挑选的人比第二个
    // 挑选的人能获得的多出来的石头数，注意不一定为正。
    // 注意，第一个挑选的人并不一定总是Alex。
    vector<vector<int>> dp(n, vector<int>(n));
    // 边界。
    for (i=0; i<n; i++) {
        dp[i][i] = piles[i];
    }
    for (len=1; len<=n; len++) {
        for (i=0; i+len<n; i++) {
            j = i+len;
            dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1]);
            // 两种情况，
            // 一是第一个挑选者X选择了piles[i]，那么第二个挑选者Y
            // 会在piles[i+1, j]中作为第一个挑选者，所以这里的
            // dp[i+1][j]表示Y在piles[i+1, j]中挑选得到的比X多的石头数，
            // 这就是为什么这里要用减。
            // 另一个情况同理。
        }
    }
    // Alex作为第一个挑选者，如果dp[0][n-1]大于0的话，
    // 也就是Alex选的石头数比Lee多，那么Alex就能赢。
    return dp[0][n-1]>0;
}
```

```cpp
// Alex can always take all odd piles or always take all even piles
// Since sum of all piles is odd then sum of all odd piles won't equals sum of all even piles, Alex could just take the bigger ones.
bool stoneGame(vector<int>& piles) {
    return true;
}
```

