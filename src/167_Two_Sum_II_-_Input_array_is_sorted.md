# 167_Two_Sum_II_-_Input_array_is_sorted

> Given an array of integers that is already ***sorted in ascending order\***, find two numbers such that they add up to a specific target number.
>
> The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
>
> **Note:**
>
> - Your returned answers (both index1 and index2) are not zero-based.
> - You may assume that each input would have *exactly* one solution and you may not use the *same* element twice.
>
> **Example:**
>
> ```
> Input: numbers = [2,7,11,15], target = 9
> Output: [1,2]
> Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
> ```

1. Easy。

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        auto n = numbers.size();
        if (n < 2) return {};
        int sum;
        for (int i=0, j=n-1; i<j; ) {
            sum = numbers[i]+numbers[j];
            if (sum == target) {
                return {i+1, j+1};
            } else if (sum > target) {
                // 跳过相等的元素。
                // j--;
                // while (i<j && numbers[j]==numbers[j+1])
                //    j--;
                do {
                    j--;
                } while (i<j && numbers[j]==numbers[j+1]);
            } else {
                do {
                    i++;
                } while (i<j && numbers[i]==numbers[i-1]);
            }
        }
        return {};
    }
};
```

