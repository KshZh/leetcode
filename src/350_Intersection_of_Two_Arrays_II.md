# 350. Intersection of Two Arrays II

> Given two arrays, write a function to compute their intersection.
>
> **Example 1:**
>
> ```
> Input: nums1 = [1,2,2,1], nums2 = [2,2]
> Output: [2,2]
> ```
>
> **Example 2:**
>
> ```
> Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
> Output: [4,9]
> ```
>
> **Note:**
>
> - Each element in the result should appear as many times as it shows in both arrays.
> - The result can be in any order.
>
> **Follow up:**
>
> - What if the given array is already sorted? How would you optimize your algorithm?
>
> - What if *nums1*'s size is small compared to *nums2*'s size? Which algorithm is better?
>
> - What if elements of *nums2* are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
>
>   - 先将nums1中的元素放入哈希表中，然后一块一块地将nums2读入内存处理。
>
>   - 如果两个数组都无法一次性放入内存中，那就先外部排序，然后一块一块地读入nums1和nums2，使用双指针处理。（似乎也可以先一块一块地读入nums1，放入哈希表中，然后再一块一块地读入nums2）
>
>     > It is a classical question in database perspective. External sort is a trick used to implement `JOIN`, basically called `sort-merge join`.
>
>   - 多机处理，mapreduce。

1. Easy。

```cpp
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> cnt;
        vector<int> res;
        for (int num: nums1)
            cnt[num]++;
        for (int num: nums2) {
            // Based on C++ map mechanism, if a key is not exist, access the key will assign a default value to the key. so if you simply test if map[key] is 0 or not by using "if (map[key] == 0)" without testing if the key is in the map. you will consume extra space....
            if (cnt.find(num)!=cnt.end() && cnt[num]-->0)
                res.push_back(num);
        }
        return res;
    }
};
```

```cpp
// 双指针，O(NlogN)。
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int n1 = (int)nums1.size(), n2 = (int)nums2.size();
        int i1 = 0, i2 = 0;
        vector<int> res;
        while(i1 < n1 && i2 < n2){
            if(nums1[i1] == nums2[i2]) {
                res.push_back(nums1[i1]);
                i1++;
                i2++;
            }
            else if(nums1[i1] > nums2[i2]){
                i2++;
            }
            else{
                i1++;
            }
        }
        return res;
    }
};
```

