# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List

> Given the array `favoriteCompanies` where `favoriteCompanies[i]` is the list of favorites companies for the `ith` person (**indexed from 0**).
>
> *Return the indices of people whose list of favorite companies is not a **subset** of any other list of favorites companies*. You must return the indices in increasing order.
>
> 
>
> **Example 1:**
>
> ```
> Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
> Output: [0,1,4] 
> Explanation: 
> Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
> Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
> Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
> ```
>
> **Example 2:**
>
> ```
> Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
> Output: [0,1] 
> Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
> ```
>
> **Example 3:**
>
> ```
> Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
> Output: [0,1,2,3]
> ```
>
> 
>
> **Constraints:**
>
> - `1 <= favoriteCompanies.length <= 100`
> - `1 <= favoriteCompanies[i].length <= 500`
> - `1 <= favoriteCompanies[i][j].length <= 20`
> - All strings in `favoriteCompanies[i]` are **distinct**.
> - All lists of favorite companies are **distinct**, that is, If we sort alphabetically each list then `favoriteCompanies[i] != favoriteCompanies[j].`
> - All strings consist of lowercase English letters only.

```java
// 数据范围不大， 直接暴露枚举。
// 考点：子集判断。
class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        for (List<String> l: favoriteCompanies) {
            Collections.sort(l); // 先按统一顺序排序。
        }
        
        List<Integer> res = new ArrayList<>();
        int n = favoriteCompanies.size();
        // 遍历每个集合，看是否是其它集合的子集。
        for (int i=0; i<n; i++) {
            boolean flag = false;
            for (int j=0; j<n; j++) {
                if (i == j) continue;
                // 判断集合i是否是集合j的子集。
                int curr=0, m=favoriteCompanies.get(i).size();
                for (int k=0, limit=favoriteCompanies.get(j).size(); k<limit && curr<m; k++) {
                    if (favoriteCompanies.get(i).get(curr).equals(favoriteCompanies.get(j).get(k))) {
                        curr++;
                    }
                }
                if (curr >= m) {
                    // 集合i中的元素在集合j中都有出现，则集合i是集合j的子集。
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                res.add(i);
            }
        }
        return res;
    }
}
```

```java
// 实际上这道题是要判断大集合的个数，大集合包含集合的子集，可以用并查集解决。
// 时间复杂度其实和上面一样大概也是O(N^3)，因为判断是否子集也是O(N)，然后并查集的O(logN)被覆盖。
class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        int n = favoriteCompanies.size();
        List<Set<String>> sets = new ArrayList<>(n);
        for (int i=0; i<n; i++) {
            sets.add(new HashSet(favoriteCompanies.get(i)));
        }
        int[] parent = new int[n];
        for (int i=0; i<n; i++) {
            parent[i] = i; // 初始时每个元素是root。
        }
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                int rootA = find(parent, i);
                int rootB = find(parent, j);
                if (rootA == rootB) {
                    // 已经在同一个集合（集合的集合）中，不必做什么。
                } else if (contains(sets.get(rootA), sets.get(rootB))) {
                    // 让更大的集合做根。
                    parent[j] = i;
                } else if (contains(sets.get(rootB), sets.get(rootA))) {
                    parent[i] = j;
                } else {
                    // 两个集合不是子集关系。
                }
            }
        }
        Set<Integer> x = new HashSet<>();
        for (int i=0; i<n; i++) {
            x.add(find(parent, i));
        }
        List<Integer> res = new ArrayList(x);
        Collections.sort(res);
        return res;
    }
    
    private int find(int[] parent, int i) {
        if (parent[i] != i) {
            parent[i] = find(parent, parent[i]);
        }
        return parent[i];
    }
    
    private boolean contains(Set<String> s1, Set<String> s2) {
        if (s1.size() <= s2.size()) return false;
        return s1.containsAll(s2);
    }
}
```

