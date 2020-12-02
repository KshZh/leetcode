# 1449. Form Largest Integer With Digits That Add up to Target

> Given an array of integers `cost` and an integer `target`. Return the **maximum** integer you can paint under the following rules:
>
> - The cost of painting a digit (i+1) is given by `cost[i]` (0 indexed).
> - The total cost used must be equal to `target`.
> - Integer does not have digits 0.
>
> Since the answer may be too large, return it as string.
>
> If there is no way to paint any integer given the condition, return "0".
>
>  
>
> **Example 1:**
>
> ```
> Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
> Output: "7772"
> Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
> Digit    cost
>   1  ->   4
>   2  ->   3
>   3  ->   2
>   4  ->   5
>   5  ->   6
>   6  ->   7
>   7  ->   2
>   8  ->   5
>   9  ->   5
> ```
>
> **Example 2:**
>
> ```
> Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
> Output: "85"
> Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
> ```
>
> **Example 3:**
>
> ```
> Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
> Output: "0"
> Explanation: It's not possible to paint any integer with total cost equal to target.
> ```
>
> **Example 4:**
>
> ```
> Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
> Output: "32211"
> ```
>
>  
>
> **Constraints:**
>
> - `cost.length == 9`
> - `1 <= cost[i] <= 5000`
> - `1 <= target <= 5000`

```java
class Solution {
    public String largestNumber(int[] cost, int target) {
        // 对于这个问题，要认识到位数越多，组成的数越大。
        // 所以转换一下问题，先求解在cost中选取尽可能多的元素，使得和为target。
        // 这里dp数组有两个维度，一个是cost[0, i]，一个是target，然后在横竖定位到的那个坑上的就是最值。
        // 状态转移方程是dp[i][j]=max(dp[i-1][j], dp[i][j-cost[i]]+1)，是一个完全背包问题。
        // 滚动数组。
        int[] dp = new int[target+1];
        // 边界：dp[0]=0;和dp[-1][j]=Integer.MIN_VALUE;（也就是表格中第一行的“上一虚拟的行”）
        for (int i=1; i<=target; i++) {
            // 之所以要初始化负值，是因为如果target不能被减为0的话，也就是选取的元素的cost和不正好等于target的话，
            // 这就是一种非法的选法/路径，不能被dp[j] = Math.max(dp[j], dp[j-cost[i]]+1);的取较大值函数选中。
            dp[i] = Integer.MIN_VALUE;
        }
        for (int i=0; i<9; i++) {
            for (int j=1; j<=target; j++) {
                if (j >= cost[i]) {
                    dp[j] = Math.max(dp[j], dp[j-cost[i]]+1); // （选或不选）
                }
            }
        }
        if (dp[target] < 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        // 尽量让最大的数做高位。
        for (int i=8; i>=0; i--) {
            while (target>=cost[i] && dp[target]==dp[target-cost[i]]+1) {
                sb.append(i+1);
                target -= cost[i];
            }
        }
        return sb.toString();
    }
}
```

