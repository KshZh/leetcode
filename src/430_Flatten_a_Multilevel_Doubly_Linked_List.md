# 430. Flatten a Multilevel Doubly Linked List

> You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
>
> Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
>
> **Example 1:**
>
> ```
> Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
> Output: [1,2,3,7,8,11,12,9,10,4,5,6]
> Explanation:
> 
> The multilevel linked list in the input is as follows:
> 
> 
> 
> After flattening the multilevel linked list it becomes:
> ```
>
> **Example 2:**
>
> ```
> Input: head = [1,2,null,3]
> Output: [1,3,2]
> Explanation:
> 
> The input multilevel linked list is as follows:
> 
>   1---2---NULL
>   |
>   3---NULL
> ```
>
> **Example 3:**
>
> ```
> Input: head = []
> Output: []
> ```
>
> **How multilevel linked list is represented in test case:**
>
> We use the multilevel linked list from **Example 1** above:
>
> ```
>  1---2---3---4---5---6--NULL
>          |
>          7---8---9---10--NULL
>              |
>              11--12--NULL
> ```
>
> The serialization of each level is as follows:
>
> ```
> [1,2,3,4,5,6,null]
> [7,8,9,10,null]
> [11,12,null]
> ```
>
> To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
>
> ```
> [1,2,3,4,5,6,null]
> [null,null,7,8,9,10,null]
> [null,11,12,null]
> ```
>
> Merging the serialization of each level and removing trailing nulls we obtain:
>
> ```
> [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
> ```
>
> **Constraints:**
>
> - Number of Nodes will not exceed 1000.
> - `1 <= Node.val <= 10^5`

1. Medium。

```cpp
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/152066/c%2B%2B-about-10-lines-solution
Node* flatten(Node* head) {
	for (Node* h = head; h; h = h->next)
	{
		if (h->child)
		{
			Node* next = h->next;
			h->next = h->child;
			h->next->prev = h;
			h->child = NULL;
			Node* p = h->next;
			while (p->next) p = p->next;
			p->next = next;
			if (next) next->prev = p;
		}
	}
	return head;
}
```

```cpp
// 递归版本。
class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return head;
        return doFlatten(head).first;
    }
    
    pair<Node*, Node*> doFlatten(Node* head) {
        // if (!head->next) return head; // 错误，这样就没有考察head->child存在的情况。
        Node *p=head, *q;
        while (p) {
            if (p->child) {
                auto child = doFlatten(p->child);
                child.second->next = p->next;
                if (p->next)
                    p->next->prev = child.second;
                p->next = child.first;
                child.first->prev = p;
                p->child = nullptr;
            }
            // XXX 一个不容易发现的bug。
            // 如果都按照这样更新的话，当p->child存在时，那么又会在这里再遍历处理一遍p->child这个链表，显然，这是无意义的多余计算。
            q = p;
            p = p->next;
        }
        return {head, q};
    }
};
```

```cpp
// fixed
class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return head;
        return doFlatten(head).first;
    }
    
    pair<Node*, Node*> doFlatten(Node* head) {
        // if (!head->next) return head; // 错误，这样就没有考察head->child存在的情况。
        Node *p=head, *q;
        while (p) {
            if (p->child) {
                auto child = doFlatten(p->child);
                child.second->next = p->next;
                if (p->next)
                    p->next->prev = child.second;
                p->next = child.first;
                child.first->prev = p;
                p->child = nullptr;
                
                q = child.second;
                p = child.second->next;
            } else {
                q = p;
                p = p->next;   
            }
        }
        return {head, q};
    }
};
```

