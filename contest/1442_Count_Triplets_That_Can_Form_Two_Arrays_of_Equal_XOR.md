# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

> Given an array of integers `arr`.
>
> We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k < arr.length)`.
>
> Let's define `a` and `b` as follows:
>
> - `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`
> - `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`
>
> Note that **^** denotes the **bitwise-xor** operation.
>
> Return *the number of triplets* (`i`, `j` and `k`) Where `a == b`.
>
>  
>
> **Example 1:**
>
> ```
> Input: arr = [2,3,1,6,7]
> Output: 4
> Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
> ```
>
> **Example 2:**
>
> ```
> Input: arr = [1,1,1,1,1]
> Output: 10
> ```
>
> **Example 3:**
>
> ```
> Input: arr = [2,3]
> Output: 0
> ```
>
> **Example 4:**
>
> ```
> Input: arr = [1,3,5,7,9]
> Output: 3
> ```
>
> **Example 5:**
>
> ```
> Input: arr = [7,11,12,9,5,2,7,17,22]
> Output: 8
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= arr.length <= 300`
> - `1 <= arr[i] <= 10^8`

```java
class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        if (n < 2) {
            return 0;
        }
        // prefix[i]=arr[0]^...^arr[i-1];
        // prefix[0]=0;
        int[] prefix = new int[n+1];
        for (int i=1; i<=n; i++) {
            prefix[i] = prefix[i-1] ^ arr[i-1];
        }
        // arr[i]^...^arr[j]=prefix[j+1]^prefix[i];
        // 因为相等异或为0，所以就把公共前缀去掉了。
        
        int res = 0;
        // 枚举三个点。
        // 注意题目中提到的三个点的关系：(0 <= i < j <= k < arr.length)。
        for (int i=0; i<n-1; i++) {
            for (int j=i+1; j<n; j++) {
                for (int k=j; k<n; k++) {
                    if ((prefix[j]^prefix[i]) == (prefix[k+1]^prefix[j])) {
                        res++;
                    }
                }
            }
        }
        return res;
    }
}
```

```java
class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        if (n < 2) {
            return 0;
        }
        // prefix[i]=arr[0]^...^arr[i-1];
        // prefix[0]=0;
        int[] prefix = new int[n+1];
        for (int i=1; i<=n; i++) {
            prefix[i] = prefix[i-1] ^ arr[i-1];
        }
        // arr[i]^...^arr[j]=prefix[j+1]^prefix[i];
        // 因为相等异或为0，所以就把公共前缀去掉了。
        
        // a = arr[i]^arr[i + 1]^...^arr[j - 1]
        // b = arr[j]^arr[j + 1]^...^arr[k]
        // a == b
        // 那么arr[i]^arr[i + 1]^...^arr[j - 1]==arr[j]^arr[j + 1]^...^arr[k]
        // 相等异或为0，那么arr[i]^...^arr[k]==0
        // 那么prefix[k+1]^prefix[i]==0，那么prefix[k+1]==prefix[i]。
        // 而在arr[i, k]中可以插入k-i个j（只是把对应地arr[]在等号两边移动而已，等式还是不变的）。
        
        int res = 0;
        // 注意prefix[0]并不包含arr[0]。所以循环从0开始。
        for (int i=0; i<=n-1; i++) {
            for (int j=i+1; j<=n; j++) {
                if (prefix[i] == prefix[j]) {
                    // 再要减掉1，因为第一个是arr[i]。（此i指题目中的i）
                    res += j-i-1;
                }
            }
        }
        return res;
    }
}
```

```java
// 对于计算prefix数组中两个相等的元素之间的距离的算法，下面的实现的时间复杂度是O(N)。
class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        if (n < 2) {
            return 0;
        }
        int[] prefix = new int[n+1];
        for (int i=1; i<=n; i++) {
            prefix[i] = prefix[i-1] ^ arr[i-1];
        }
        
        int res = 0;
        Map<Integer, Integer> startPosSum = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int i=0; i<=n; i++) {
            res += count.getOrDefault(prefix[i], 0)*(i-1)-startPosSum.getOrDefault(prefix[i], 0); // 右闭减左开等于区间长度。注意prefix[i]不包括arr[i]。
            
            count.put(prefix[i], count.getOrDefault(prefix[i], 0)+1);
            startPosSum.put(prefix[i], startPosSum.getOrDefault(prefix[i], 0)+i);
        }
        return res;
    }
}
```

