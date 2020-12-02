# 1025. Divisor Game

> Alice and Bob take turns playing a game, with Alice starting first.
>
> Initially, there is a number `N` on the chalkboard. On each player's turn, that player makes a *move* consisting of:
>
> - Choosing any `x` with `0 < x < N` and `N % x == 0`.
> - Replacing the number `N` on the chalkboard with `N - x`.
>
> Also, if a player cannot make a move, they lose the game.
>
> Return `True` if and only if Alice wins the game, assuming both players play optimally.

1. Easy，DP。

```cpp
class Solution {
public:
    bool divisorGame(int N) {
        int i, j;
        // dp[i]表示拿到i的人的输赢。
        // 错。
        // dp[i]表示Alice拿到i时的输赢。
        vector<bool> dp(N+1, false);
        dp[2] = true; // 边界，注意题目`0<x<N`，故`dp[1]==False`。
        for (i=3; i<=N; i++) {
            for (j=1; j<i; j++) {
                // 如果Alice选择了j，那么若Bob拿到了i-j且输的话，那么Alice就赢。
                if (i%j==0 && dp[i-j]==false) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[N];
    }
};
```

```cpp
class Solution {
    vector<int> dp;
public:
    bool divisorGame(int N) {
        // dp.resize(N+1); // 错误，我们想要初始化为-1。
        dp = vector<int>(N+1, -1);
        return dfs(N);
    }
    
    // 不缓存会超时，因为重复计算了很多相同的子问题。
    bool dfs(int N) {
        if (dp[N]!=-1) return dp[N];
        for (int i=1; i<N; i++) { // 树形递归，树形展开，并不是并行展开的，而是串行。
            if (N%i == 0) {
                if (!dfs(N-i)) { // 有一条路径能赢即可。
                    dp[N] = 1;
                    return true;
                }
            }
        }
        dp[N] = 0;
        return false;
    }
};
```

```cpp
class Solution {
public:
    bool divisorGame(int N) {
        // 拿1的人输，拿2的人赢，因为它可以选1，然后另一个人拿到1就会输。
        // 拿3输，拿4赢，拿5输，拿6赢，……
        return !(N%2);
    }
};
```

