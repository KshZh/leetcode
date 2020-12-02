# 559. Maximum Depth of N-ary Tree

> Given a n-ary tree, find its maximum depth.
>
> The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
>
> *Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

1. Easy。

```cpp
int maxDepth(Node* root) {
    if (!root) return 0;
    int max = 0; // 不能初始化为INT_MIN，这样如果当前结点是叶子，不注意的就返回了INT_MIN+1了。
    int childMax;
    for (Node* child: root->children) {
        if (child && (childMax=maxDepth(child))>max)
            max = childMax;
    }
    return max+1;
}
```

