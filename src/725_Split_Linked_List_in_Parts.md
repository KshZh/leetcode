# 725. Split Linked List in Parts

> Given a (singly) linked list with head node `root`, write a function to split the linked list into `k` consecutive linked list "parts".
>
> The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.
>
> The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
>
> Return a List of ListNode's representing the linked list parts that are formed.
>
> Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
>
> **Example 1:**
>
> ```
> Input:
> root = [1, 2, 3], k = 5
> Output: [[1],[2],[3],[],[]]
> Explanation:
> The input and each element of the output are ListNodes, not arrays.
> For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
> The first element output[0] has output[0].val = 1, output[0].next = null.
> The last element output[4] is null, but it's string representation as a ListNode is [].
> ```
>
> **Example 2:**
>
> ```
> Input: 
> root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
> Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
> Explanation:
> The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
> ```

1. Medium。

```cpp
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int n = 0, i, j;
        ListNode* p = root;
        for (; p; p=p->next, n++)
            ;
        vector<ListNode*> ans(k, nullptr);
        int len = n/k; // 最小子串长度。
        int X = n%k; // 前X个字串的长度为len+1。
        for (i=0; i<k; i++) {
            if (i >= n) { // if (!root)
                break; // n<k的情况，剩下的默认为nullptr即可。
            }
            ans[i] = root;
            int Len = i<X? len+1: len;
            for (j=0; j<Len-1; j++, root=root->next)
                ;
            p = root->next;
            root->next = nullptr;
            root = p;
        }
        return ans;
    }
};
```

