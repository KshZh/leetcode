# 817. Linked List Components

> We are given `head`, the head node of a linked list containing **unique integer values**.
>
> We are also given the list `G`, a subset of the values in the linked list.
>
> Return the number of connected components in `G`, where two values are connected if they appear consecutively in the linked list.
>
> **Example 2:**
>
> ```
> Input: 
> head: 0->1->2->3->4
> G = [0, 3, 1, 4]
> Output: 2
> Explanation: 
> 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
> ```

1. Medium。

2. 一开始很容易被题目所问引导或限制，主要从数组G的角度来思考。其实换个角度考虑链表会容易一些：

   > Instead of thinking about connected components in `G`, think about them in the linked list. Connected components in `G` must occur consecutively in the linked list.

```cpp
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& G) {
        unordered_set<int> book(G.begin(), G.end()); // 转换成哈希表，提高查询效率。
        int num = 0;
        bool flag = false; // 做一下优化，缓存一下查询结果。
        while (head) {
            if (flag || book.find(head->val) != book.end()) {
                if (!head->next || book.find(head->next->val) == book.end()) {
                    num++;
                    flag = false;
                } else
                    flag = true;
            }
            head = head->next;
        }
        return num;
    }
};
```

