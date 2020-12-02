# 326. Power of Three

> Given an integer, write a function to determine if it is a power of three.
>
> **Example 1:**
>
> ```
> Input: 27
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: 0
> Output: false
> ```
>
> **Example 3:**
>
> ```
> Input: 9
> Output: true
> ```
>
> **Example 4:**
>
> ```
> Input: 45
> Output: false
> ```
>
> **Follow up:**
> Could you do it without using any loop / recursion?

1. Easy。

```java
public class Solution {
    public boolean isPowerOfThree(int n) {
        // 十进制中，十的次幂为1, 10, 100，...
        // 二进制中，二的次幂为1, 10, 100, ...
        // 三进制同理。
        return Integer.toString(n, 3).matches("^10*$");
    }
}
```

```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        // 1162261467 is 3^19,  3^20 is bigger than int  
        return (n>0 && 1162261467%n==0);
        // 模运算相当于不停地减，如果n是3的n次幂的话，那么减(19-n)次，会得到0。
        // 3^n*3^(19-n)=3^19。
    }
};
```

