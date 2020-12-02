# 344. Reverse String

1. Easy。

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        auto n=s.size(), end=n/2;
        for (int i=0; i<end; i++) {
            std::swap(s[i], s[n-1-i]); // 隐含的双指针。
        }
    }
};
```

