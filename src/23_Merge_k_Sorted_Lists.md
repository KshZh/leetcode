# 23. Merge k Sorted Lists

> Merge *k* sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
>
> **Example:**
>
> ```
> Input:
> [
>   1->4->5,
>   1->3->4,
>   2->6
> ]
> Output: 1->1->2->3->4->4->5->6
> ```

1. Hard。

2. 分治策略，

   ![](https://leetcode.com/problems/merge-k-sorted-lists/Figures/23/23_divide_and_conquer_new.png)

3. 最小堆/优先队列。

4. 顺序遍历这些链表，增量地两两合并。时间复杂度O(KN)。

5. 维护K个指针，每一趟从这K个指针中找到一个最小的结点，时间复杂度同上。

6. 将所有结点收集到数组中，排序，再创建新的链表返回，时间复杂度O(NlogN)。

```cpp
// 时间复杂度同归并排序，是O(NlogK)，其中K是链表数，其中log在这里以2为底。
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return divideAndConquer(lists, 0, lists.size());
    }
    
    // [left, right)
    ListNode* divideAndConquer(vector<ListNode*>& lists, int left, int right) {
        if (left == right) return nullptr;
        if (left == right - 1) return lists[left];
        
        int mid = (left+right)/2;
        ListNode* l = divideAndConquer(lists, left, mid);
        ListNode* r = divideAndConquer(lists, mid, right);
        return merge2(l, r);
    }
    
    ListNode* merge2(ListNode* l1, ListNode* l2) {
        ListNode* head=nullptr;
        ListNode** pp = &head;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                *pp = l1;
                l1 = l1->next;
            } else {
                *pp = l2;
                l2 = l2->next;
            }
            pp = &((*pp)->next);
        }
        if (l1) *pp = l1;
        if (l2) *pp = l2;
        return head;
    }
};
```

```cpp
// 堆的插入和删除时间复杂度都是O(logK)，故总的时间复杂度是O(NlogK)。
using Pair = pair<ListNode*, int>;
auto cmp = [](const Pair& a, const Pair& b) { return a.second>b.second; };
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<Pair, vector<Pair>, decltype(cmp)> q(cmp);
        for (const auto l: lists) {
            if (l) // lists中可能有空链表，这太坑了。
                q.push({l, l->val});
        }
        ListNode* head = nullptr;
        ListNode** pp = &head;
        while (!q.empty()) {
            auto p = q.top();
            q.pop();
            *pp = p.first;
            pp = &((*pp)->next);
            if (*pp)
                q.push({*pp, (*pp)->val});
        }
        return head;
    }
};
```

