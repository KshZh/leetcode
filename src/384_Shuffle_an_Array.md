# 384. Shuffle an Array

> Shuffle a set of numbers without duplicates.
>
> **Example:**
>
> ```
> // Init an array with set 1, 2, and 3.
> int[] nums = {1,2,3};
> Solution solution = new Solution(nums);
> 
> // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
> solution.shuffle();
> 
> // Resets the array back to its original configuration [1,2,3].
> solution.reset();
> 
> // Returns the random shuffling of array [1,2,3].
> solution.shuffle();
> ```

1. Medium。

> https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
>
> **How does this work?**
>
> The probability that ith element (including the last one) goes to last position is 1/n, because we randomly pick an element in first iteration.
>
> The probability that ith element goes to second last position can be proved to be 1/n by dividing it in two cases.
>
> *Case 1: i = n-1 (index of last element)*:
>
> The probability of last element going to second last position is = (probability that last element doesn’t stay at its original position) x (probability that the index picked in previous step is picked again so that the last element is swapped)
>
> So the probability = ((n-1)/n) x (1/(n-1)) = 1/n
>
> *Case 2: 0 < i < n-1 (index of non-last)*:
>
> The probability of ith element going to second position = (probability that ith element is not picked in previous iteration) x (probability that ith element is picked in this iteration)
>
> So the probability = ((n-1)/n) x (1/(n-1)) = 1/n

```java
// Time complexity : O(n^2)，因为从数组中删除一个元素最坏需要O(N)。
// Space complexity : O(n)O(n).
class Solution {
    private int[] array;
    private int[] original;

    private Random rand = new Random();

    private List<Integer> getArrayCopy() {
        List<Integer> asList = new ArrayList<Integer>();
        for (int i = 0; i < array.length; i++) {
            asList.add(array[i]);
        }
        return asList;
    }

    public Solution(int[] nums) {
        array = nums;
        original = nums.clone();
    }
    
    public int[] reset() {
        array = original;
        original = original.clone();
        return array;
    }
    
    public int[] shuffle() {
        List<Integer> aux = getArrayCopy();

        for (int i = 0; i < array.length; i++) {
            int removeIdx = rand.nextInt(aux.size());
            array[i] = aux.get(removeIdx);
            aux.remove(removeIdx); // 删掉已被选中的元素。
        }

        return array;
    }
}
```

```cpp
// 相比上面的解法，时间复杂度降低为O(N)。
// 证明：
// 第i个元素被放到位置0的概率是1/n，因为在第一个循环中，我们从[0, n_)中随机选取一个元素放到位置0。
// 第i个元素被放到位置1的概率，不管i=0还是i∈[1, n_)，元素i在前面的循环中都不能被随机数下标选中，被交换到位置[0, 1)中，从而不在当前循环中随机数生成的范围中，不可能被选中。然后在当前循环中，该元素所在的下标要被选中，从而交换到位置1上，故概率为(n-1)/n * 1/(n-1) = 1/n。
// 继续推广，第i个元素被放到位置k的概率，同理，概率为(n-1)/n * (n-2)/(n-1) * ... * (n-k)/(n-k+1) * 1/(n-k) = 1/n。
class Solution {
    vector<int> nums_, origin_;
    size_t n_;
public:
    // 注意，参数确实是传值参数。
    Solution(vector<int> nums): nums_(nums), origin_(std::move(nums)), n_(nums_.size()) {
        std::srand(std::time(nullptr));
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        nums_ = origin_;
        return nums_;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int idx;
        for (int curr=0; curr<n_; curr++) {
            idx = (rand()*1.0/RAND_MAX)*(n_-curr) + curr; // 随机选择[curr, n_)中的一个下标，然后与curr指向的元素交换。
            std::swap(nums_[curr], nums_[idx]);
        }
        return nums_; // 返回一份深拷贝。（cpp默认深拷贝，只有类显式实现移动语义才可能浅拷贝）
    }
};
```

