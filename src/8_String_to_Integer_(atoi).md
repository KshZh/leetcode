# 8. String to Integer (atoi)

1. Medium，判断int溢出。

```cpp
class Solution {
    const string bound = "214748364";
public:
    int myAtoi(string str) {
        auto l = str.find_first_not_of(" "); // left bound.
        if (l == string::npos) return 0;
        if (str[l]!='-' && str[l]!='+' && !isdigit(str[l])) return 0;
        int sign = 1;
        if (!isdigit(str[l])) {
            if (str[l] == '-') sign = -1;
            l++;
        }
        auto r = str.find_first_not_of("0123456789", l); // right bound.
        auto msb = str.find_first_not_of("0", l); // position of most significant bit.
        if (msb==string::npos || msb >= r) return 0; // just `[-+]0*`.
        l = msb;
        if (r == string::npos) r = str.size();
        // 判断是否溢出。
        if (r-l > 10) return sign==1? INT_MAX: INT_MIN;
        if (r-l == 10) {
            int i, j;
            bool flag = true;
            for (i=l, j=0; j<9; i++, j++) {
                if (str[i] > bound[j]) return sign==1? INT_MAX: INT_MIN; // 一定溢出。
                if (str[i] < bound[j]) { // 一定不会溢出。
                    flag = false;
                    break;
                }
                // str[i] == bound[j]，无法下结论，继续遍历。
            }
            if (flag) {
                // 前9位相同，查看最低有效位。
                if (sign==1 && str[i]>'7') return INT_MAX;
                if (sign==-1 && str[i]>'8') return INT_MIN;   
            }
        }
        int ans = 0;
        while (isdigit(str[l])) {
            // 这里注意，不能按正数累加好后，最后才`ans*sign`，
            // 当输入是"-2147483648"时，在循环结束前，最后一位加上8时就会溢出。
            // 这里的处理时，对于正数就累加，对于负数则累减。
            ans = ans*10 + (str[l++]-'0')*sign;
        }
        return ans;
    }
};

// "42"
// "0-1"
// "1095502006p8"
// "2147483648"
// "-2147483648"
// "2147483800"
// "words and 987"
// "-91283472332"
// "4193 with words"
// "   -42"
```

```cpp
int myAtoi(string& str) {
    int sign = 1, base = 0, i = 0;
    while (str[i] == ' ') { i++; }
    if (str[i] == '-' || str[i] == '+') {
        sign = 1 - 2 * (str[i++] == '-'); 
    }
    while (str[i] >= '0' && str[i] <= '9') {
        if (base>INT_MAX/10 || (base==INT_MAX/10 && str[i]-'0'>INT_MAX%10)) { // 判断溢出。
            if (sign == 1) return INT_MAX;
            else return INT_MIN; // 注意这里处理了"-2147483648"这种情况，我们是先忽略符号按照正数累加的，所以无法存放2147483648，那么这里就会溢出，且根据符号返回INT_MIN，结果正确。
        }
        base = 10*base + (str[i++]-'0'); // 前导0可以通过这条语句消除掉，在这条语句中，前导0对base没有贡献。
    }
    return base*sign;
}
```

