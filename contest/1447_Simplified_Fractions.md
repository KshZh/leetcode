# 1447. Simplified Fractions

> Given an integer `n`, return a list of all **simplified** fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to `n`. The fractions can be in **any** order.
>
> 
>
> **Example 1:**
>
> ```
> Input: n = 2
> Output: ["1/2"]
> Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 3
> Output: ["1/2","1/3","2/3"]
> ```
>
> **Example 3:**
>
> ```
> Input: n = 4
> Output: ["1/2","1/3","1/4","2/3","3/4"]
> Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
> ```
>
> **Example 4:**
>
> ```
> Input: n = 1
> Output: []
> ```
>
> 
>
> **Constraints:**
>
> - `1 <= n <= 100`

```java
// 这道题容易忽略的地方就是重复加同一个实数的不同分数形式。
// 可能最先想到的就是用哈希表记住加入过的实数，然后遍历到一个分数时，先求出实数，看该实数是否在哈希表中。
// 但其实不必，这是一个数学问题，我们的代码只需从最简的分数开始添加，然后后面的分数，我们判断该分数是否最简，
// 即判断分子分母的最大公约数是否为1，如果不是最简，说明之前肯定添加过了，就不再添加到结果中。
class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> res = new ArrayList<>();
        for (int i=2; i<=n; i++) {
            String denominator = Integer.toString(i);
            for (int j=1; j<i; j++) {
                if (gcd(i, j) == 1) {
                    res.add(Integer.toString(j)+"/"+denominator);
                }
            }
        }
        return res;
    }
    
    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a%b);
    }
}
```

