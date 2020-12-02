# 590. N-ary Tree Postorder Traversal

> Given an n-ary tree, return the *postorder* traversal of its nodes' values.
>
> *Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*
>
> **Follow up:**
>
> Recursive solution is trivial, could you do it iteratively?

1. Easy。

```cpp
class Solution {
    vector<int> v;
public:
    vector<int> postorder(Node* root) {
        dfs(root);
        return v;
    }
    
    void dfs(Node* root) {
        if (!root) return;
        for (Node* child: root->children)
            dfs(child);
        v.push_back(root->val);
    }
};
```

```cpp
// 后序遍历的迭代实现。
vector<int> postorder(Node* root) {
    if (!root) return {};
    vector<int> v;
    // first是结点的地址，
    // second是当前应该访问该结点的哪个子树。
    stack<pair<Node*, int>> s;
    s.push({root, 0});
    while (!s.empty()) {
        auto& p = s.top();
        if (p.second == p.first->children.size()) {
            s.pop();
            v.push_back(p.first->val);
        } else {
            // 结点p.first的子树还没遍历完，因为是后序遍历，所以还不能访问当前结点，故当前结点还留在栈中，等子树遍历完再回到当前结点访问下一棵子树或子树访问完后访问当前结点。
            s.push({p.first->children[p.second++], 0});
        }
    }
    return v;
}
```

