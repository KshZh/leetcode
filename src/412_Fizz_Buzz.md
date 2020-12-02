# 412. Fizz Buzz

> Write a program that outputs the string representation of numbers from 1 to *n*.
>
> But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
>
> **Example:**
>
> ```
> n = 15,
> 
> Return:
> [
>     "1",
>     "2",
>     "Fizz",
>     "4",
>     "Buzz",
>     "Fizz",
>     "7",
>     "8",
>     "Fizz",
>     "Buzz",
>     "11",
>     "Fizz",
>     "13",
>     "14",
>     "FizzBuzz"
> ]
> ```

1. Easy。

```cpp
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        // 这里要用红黑树保证顺序，而不是哈希表。
        // "FizzBuzz"和"BuzzFizz"不等。
        map<int, string> dict{{3, "Fizz"}, {5, "Buzz"}};
        for (int i=1; i<=n; i++) {
            // 第一种方式，如果要求7的倍数用"Kizz"代替呢，就要加更多代码。
            // if (i%3==0 && i%5==0) res.push_back("FizzBuzz");
            // if (i%3 == 0) res.push_back("Fizz");
            // if (i%5 == 0) ...
            // 第二种方式，字符串拼接。扩展时要加的代码少了。
            // string s;
            // if (i%3 == 0) s+="Fizz";
            // if (i%5 == 0) s+="Buzz";
            // 第三种方式，结合键值对容器和字符串拼接。
            string s;
            for (auto& p: dict) {
                if (i%p.first == 0) s+=p.second;
            }
            if (s.empty()) res.push_back(std::to_string(i));
            else res.push_back(std::move(s));
        }
        return res;
    }
};
```

```java
// 避免使用大量模运算操作。
// https://leetcode.com/problems/fizz-buzz/discuss/89931/Java-4ms-solution-Not-using-%22%22-operation
public class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ret = new ArrayList<String>(n);
        for(int i=1,fizz=0,buzz=0;i<=n ;i++){
            fizz++;
            buzz++;
            if(fizz==3 && buzz==5){ // 跳到同一个点。
                ret.add("FizzBuzz");
                fizz=0;
                buzz=0; 
            }else if(fizz==3){
                ret.add("Fizz");
                fizz=0; // 3步一个循环。
            }else if(buzz==5){
                ret.add("Buzz");
                buzz=0; // 5步一个循环。
            }else{
                ret.add(String.valueOf(i));
            }
        } 
        return ret;
    }
}
```

