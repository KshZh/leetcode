# 449. Serialize and Deserialize BST

> Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
>
> Design an algorithm to serialize and deserialize a **binary search tree**. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
>
> **The encoded string should be as compact as possible.**
>
> **Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

1. Medium。

```cpp
// Encodes a tree to a single string.
// "根,左子树,右子数"，因为是BST，所以左子树序列小于根，右子树序列大于根。
string serialize(TreeNode* root) {
    if (!root) return "";
    ostringstream out(std::ios_base::app);
    stack<TreeNode*> s;
    s.push(root);
    while (!s.empty()) {
        root = s.top();
        s.pop();
        out << root->val << '#';
        if (root->right) s.push(root->right);
        if (root->left) s.push(root->left);
    }
    return out.str();
}

// Decodes your encoded data to tree.
TreeNode* deserialize(string data) {
    if (data.empty()) return nullptr;
    istringstream in(data);
    vector<int> v;
    int x;
    char c;
    while (in >> x) {
        v.push_back(x);
        in >> c;
    }
    return decode(v, 0, v.size());
}

TreeNode* decode(vector<int>& v, int begin, int end) {
    if (begin == end)
        return nullptr;
    TreeNode* root = new TreeNode(v[begin++]);
    int i;
    for (i=begin; i<end && v[i]<root->val; i++)
        ;
    root->left = decode(v, begin, i);
    root->right = decode(v, i, end);
    return root;
}
```

```cpp
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string order;
        inorderDFS(root, order);
        return order;
    }
    
    inline void inorderDFS(TreeNode* root, string& order) {
        if (!root) return;
        char buf[4];
        memcpy(buf, &(root->val), sizeof(int)); //burn the int into 4 chars
        for (int i=0; i<4; i++) order.push_back(buf[i]);
        inorderDFS(root->left, order);
        inorderDFS(root->right, order);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return reconstruct(data, pos, INT_MIN, INT_MAX);
    }
    
    // 因为是BST，所以传入一个范围[minValue, maxValue]，那么构建的树的应该在这个范围内，如果超出范围，说明读到了另一棵树的结点，返回nullptr，当前树构造完成。
    inline TreeNode* reconstruct(const string& buffer, int& pos, int minValue, int maxValue) {
        if (pos >= buffer.size()) return NULL; // using pos to check whether buffer ends is better than using char* directly.
        
        int value;
        memcpy(&value, &buffer[pos], sizeof(int));
        if (value < minValue || value > maxValue) return NULL;
        
        TreeNode* node = new TreeNode(value);
        pos += sizeof(int);
        node->left = reconstruct(buffer, pos, minValue, value);
        node->right = reconstruct(buffer, pos, value, maxValue);
        return node;
    }
};
```

```java
// 如果是普通的二叉树，那么需要在到达叶子时多编码一个结束符，这样解码按相同的序（先序/中序/后续）构建树的时候，才知道到哪里该子树构建完成，返回，构造另一棵子树。
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serialize(root, sb);
        return sb.toString();
    }
    
    public void serialize(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("#").append(",");
        } else {
            sb.append(root.val).append(",");
            serialize(root.left, sb);
            serialize(root.right, sb);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> q = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserialize(q);
    }
    
    public TreeNode deserialize(Queue<String> q) {
        String s = q.poll();
        if (s.equals("#")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(s));
        root.left = deserialize(q);
        root.right = deserialize(q);
        return root;
    }
}
```

