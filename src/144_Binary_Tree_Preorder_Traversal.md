# 144. Binary Tree Preorder Traversal

> Given a binary tree, return the *preorder* traversal of its nodes' values.

1. 树，先序遍历，Medium。
2. [Morris Traversal方法遍历二叉树（非递归，不用栈，O(1)空间）](https://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html)

```cpp
class Solution {
private:
    vector<int> v;
public:
    vector<int> preorderTraversal(TreeNode* root) {
        dfs(root);
        return v;
    }
    
    void dfs(TreeNode* root) {
        if (root == nullptr) return;
        v.push_back(root->val);
        dfs(root->left);
        dfs(root->right);
    }
};
```

```cpp
class Solution {
private:
    vector<int> v;
public:
    vector<int> preorderTraversal(TreeNode* root) {
        TreeNode* p = root;
        stack<TreeNode*> s;
        while (p || !s.empty()) {
            while (p) {
                s.push(p);
                v.push_back(p->val); // 先序
                p = p->left;
            }
            // if (!s.empty()) { // 不需要做这个检查，因为while的谓词，如果s为空，则p必定不为nullptr才进入循环，然后一定会填入s，到这里，s必定不为空。
            p = s.top();
            s.pop();
            // v.push_back(p->val); // 中序
            p = p->right;
        }
        return v;
    }
};
```

```cpp
// Morris算法，O(1)空间复杂度，O(N)时间复杂度。
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        TreeNode* curr = root;
        TreeNode* prev;
        while (curr) {
            if (!curr->left) { // 没有左子树，在先序遍历中，就轮到访问当前结点/根了。
                ans.push_back(curr->val);
                curr = curr->right;
                continue;
            }
            // 在curr的左子树中找到curr的右子树在先序遍历中的前驱结点，也就是curr的左子树的最右下的结点。
            prev = curr->left;
            while (prev->right && prev->right!=curr)
                prev = prev->right;
            if (prev->right == nullptr) { // curr的左子树还未被访问，因为是先序遍历，所以先访问curr/根，再遍历左子树。
                prev->right = curr;
                ans.push_back(curr->val);
                curr = curr->left;
            } else { // `prev->right==curr`，curr的左子树已经访问过了，刚回到curr，现在应该遍历右子树。
                prev->right = nullptr; // 恢复树的形状。
                curr = curr->right;
            }
        }
        return ans;
    }
};
```

```cpp
// 更直观的迭代版实现。
// 如果是中序遍历，那还是用上面的迭代版比较好实现。
vector<int> preorderTraversal(TreeNode* root) {
    if (!root) return {};
    vector<int> ans;
    stack<TreeNode*> s;
    s.push(root);
    TreeNode* p;
    while (!s.empty()) {
        p = s.top();
        s.pop(); // 先序遍历，根先访问，把其左右子树入栈，然后根就没有可利用的信息了，直接从栈中删除。
        ans.push_back(p->val);
        if (p->right) s.push(p->right); // 先推入右子树，这样就会先访问左子树，后访问右子树。（XXX 左子树遍历完后，不断弹出左子树的结点，然后就轮到这个时候推入的右子树的根了，然后就遍历右子树）
        if (p->left) s.push(p->left);
    }
    return ans;
}
```

