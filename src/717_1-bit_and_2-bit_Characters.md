# 717. 1-bit and 2-bit Characters

> We have two special characters. The first character can be represented by one bit `0`. The second character can be represented by two bits (`10` or `11`).
>
> Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
>
> **Example 1:**
>
> ```
> Input: 
> bits = [1, 0, 0]
> Output: True
> Explanation: 
> The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
> ```
>
> **Example 2:**
>
> ```
> Input: 
> bits = [1, 1, 1, 0]
> Output: False
> Explanation: 
> The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
> ```
>
> **Note:**
>
> `1 <= len(bits) <= 1000`.
>
> `bits[i]` is always `0` or `1`.

1. Easy。

```cpp
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i;
        for (i=0; i<bits.size()-1; i++) {
            if (bits[i] == 1) // 1开头就是一对，直接跳过。
                i++;
        }
        return i==bits.size()-1; // 如果最后是以对结尾，那么i会多加一次跳过这个对，那么i就等于bits.size()了。
    }
};
```

```cpp
// 大佬的解法是找规律，直接检查末尾的几个元素，不必遍历。
// https://leetcode.com/problems/1-bit-and-2-bit-characters/discuss/108967/JAVA-check-only-the-end-of-array
// We don't need to traverse the whole array, just check the last part of it.
// if there is only one symbol in array the answer is always true (as last element is 0)
// if there are two 0s at the end again the answer is true no matter what the rest symbols are( ...1100, ...1000,)
// if there is 1 right before the last element(...10), the outcome depends on the count of sequential 1, i.e.
//    a) if there is odd amount of 1(10, ...01110, etc) the answer is false as there is a single 1 without pair
// 	  b) if it's even (110, ...011110, etc) the answer is true, as 0 at the end doesn't have anything to pair with
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int ones = 0;
        // Starting from one but last, as last one is always 0.
        for (int i = bits.length - 2; i >= 0 && bits[i] != 0 ; i--) { 
            ones++;
        }
        if (ones % 2 > 0) return false; 
        return true;
    }
}
```

