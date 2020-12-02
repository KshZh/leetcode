# 165. Compare Version Numbers

> **Example 1:**
>
> ```
> Input: version1 = "0.1", version2 = "1.1"
> Output: -1
> ```
>
> **Example 2:**
>
> ```
> Input: version1 = "1.0.1", version2 = "1"
> Output: 1
> ```
>
> **Example 3:**
>
> ```
> Input: version1 = "7.5.2.4", version2 = "7.5.3"
> Output: -1
> ```
>
> **Example 4:**
>
> ```
> Input: version1 = "1.01", version2 = "1.001"
> Output: 0
> Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
> ```
>
> **Example 5:**
>
> ```
> Input: version1 = "1.0", version2 = "1.0.0"
> Output: 0
> Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
> ```

1. Medium，字符串处理，istringstream。

2. 将数字字符串转换为int有溢出的风险，如果要完全避免，只能写一个数字字符串的比较函数，去掉前导零，若位数相等，从最低有效位开始比较，否则，位数多的大。

3. ```cpp
   // Corner case 1: '01' vs '1'
   // Corner case 2: '1.0' vs '1'
   // 所以我们不能只遍历完较短的串后就退出循环，而要遍历完较长的串，且较短的串取有效的默认值，这里是0（题目中也说了）。
   ```

```cpp
class Solution {
public:
    int compareVersion(string version1, string version2) {
        for (char& c: version1) { // 注意要取引用，否则修改的就是副本了。
            if (c == '.')
                c = ' ';
        }
        for (char& c: version2) {
            if (c == '.')
                c = ' ';
        }
        istringstream s1(version1), s2(version2);
        int n1, n2;
        while (true) {
            if (!(s1>>n1)) n1=0; // 注意要加括号改变运算次序。
            if (!(s2>>n2)) n2=0;
            if (!s1 && !s2) return 0;
            if (n1 > n2) return 1;
            if (n1 < n2) return -1;
        }
    }
};
```

```cpp
// 朴素的实现。
int compareVersion(string version1, string version2) {
    int i = 0; 
    int j = 0;
    int n1 = version1.size(); 
    int n2 = version2.size();
    
    int num1 = 0;
    int num2 = 0;
    while(i<n1 || j<n2)
    {
        while(i<n1 && version1[i]!='.'){
            num1 = num1*10+(version1[i]-'0');
            i++;
        }
        
        while(j<n2 && version2[j]!='.'){
            num2 = num2*10+(version2[j]-'0');;
            j++;
        }
        
        if(num1>num2) return 1;
        else if(num1 < num2) return -1;
        
        num1 = 0;
        num2 = 0;
        i++;
        j++;
    }
    
    return 0;
}
```

