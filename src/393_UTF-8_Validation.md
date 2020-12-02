# 393. UTF-8 Validation

> A character in UTF8 can be from **1 to 4 bytes** long, subjected to the following rules:
>
> 1. For 1-byte character, the first bit is a 0, followed by its unicode code.
> 2. For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
>
> This is how the UTF-8 encoding would work:
>
> ```
>    Char. number range  |        UTF-8 octet sequence
>       (hexadecimal)    |              (binary)
>    --------------------+---------------------------------------------
>    0000 0000-0000 007F | 0xxxxxxx
>    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
>    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
>    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
> ```
>
> Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
>
> **Note:**
> The input is an array of integers. Only the **least significant 8 bits** of each integer is used to store the data. This means each integer represents only 1 byte of data.

1. Medium。

```cpp
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int i, j, k, mask;
        for (i=0; i<data.size(); i++) {
            if ((data[i]&128) == 0) {
                continue;
            } else {
                // 最高有效位不是0，那肯定是1，不必检查。
                mask = 64;
                for (j=0; (data[i]&mask)!=0; j++, mask>>=1)
                    ;
                if (j>3 || j<1 || i+j>=data.size()) return false;
                i += j;
                for (k=0; k<j; k++) {
                    if ((data[i-k]&192) != 128)
                        return false;
                }
            }
        }
        return true;
    }
};
```

```cpp
// 大佬的代码：https://leetcode.com/problems/utf-8-validation/discuss/87462/Concise-C%2B%2B-implementation
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int count = 0;
        for (auto c : data) {
            if (count == 0) {
                if ((c >> 5) == 0b110) count = 1;
                else if ((c >> 4) == 0b1110) count = 2;
                else if ((c >> 3) == 0b11110) count = 3;
                else if ((c >> 7)) return false;
            } else {
                if ((c >> 6) != 0b10) return false;
                count--;
            }
        }
        return count == 0;
    }
};
```

