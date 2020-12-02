# [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

> Given a non-empty list of words, return the *k* most frequent elements.
>
> Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
>
> **Example 1:**
>
> ```
> Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
> Output: ["i", "love"]
> Explanation: "i" and "love" are the two most frequent words.
>     Note that "i" comes before "love" due to a lower alphabetical order.
> ```
>
> 
>
> **Example 2:**
>
> ```
> Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
> Output: ["the", "is", "sunny", "day"]
> Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
>     with the number of occurrence being 4, 3, 2 and 1 respectively.
> ```
>
> 
>
> **Note:**
>
> 1. You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
> 2. Input words contain only lowercase letters.
>
> 
>
> **Follow up:**
>
> 1. Try to solve it in *O*(*n* log *k*) time and *O*(*n*) extra space.

```java
// O(NlogN), O(N).
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // 先用哈希表计数和去重。
        Map<String, Integer> count = new HashMap();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        List<String> candidates = new ArrayList(count.keySet());
        Collections.sort(candidates, (w1, w2) -> count.get(w1).equals(count.get(w2)) ?
                w1.compareTo(w2) : count.get(w2) - count.get(w1)); // XXX 升序，1减/compareTo2（返回负值，表示1比2小，1放前面，小的放前面，升序），降序，2减/compareTo1（返回负值，表示1比2小，1放前面，但实际上2比1小，故变成了大的放前面，降序）。

        return candidates.subList(0, k);
    }
}
```

```java
// O(Nlogk), O(N).
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // 先用哈希表计数和去重。
        Map<String, Integer> count = new HashMap();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<String> heap = new PriorityQueue<String>(
                (w1, w2) -> count.get(w1).equals(count.get(w2)) ?
                w2.compareTo(w1) : count.get(w1) - count.get(w2) ); // XXX java出堆的顺序是先出排前面的元素，所以这里对出现次数升序排，把出现次数少的先出堆，留下出现次数多的，然后若出现次数相等，按字典序降序排，字典序大的先出堆，留下字典序小的。

        for (String word: count.keySet()) {
            heap.offer(word);
            if (heap.size() > k) heap.poll(); // 始终保持堆的大小为k，这样插入删除才能O(logk)，而不是O(logN)。
        }

        List<String> ans = new ArrayList();
        while (!heap.isEmpty()) ans.add(heap.poll());
        Collections.reverse(ans); // 反转一下。
        return ans;
    }
}
```

# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

> Given a non-empty array of integers, return the ***k\*** most frequent elements.
>
> **Example 1:**
>
> ```
> Input: nums = [1,1,1,2,2,3], k = 2
> Output: [1,2]
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1], k = 1
> Output: [1]
> ```
>
> **Note:**
>
> - You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
> - Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.
> - It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
> - You can return the answer in any order.

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 先用哈希表计数并去重。
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x: nums) {
            cnt.put(x, cnt.getOrDefault(x, 0)+1);
        }
        Queue<Integer> pq = new PriorityQueue<>((Integer x, Integer y)->cnt.get(x)-cnt.get(y)); // 1减2，升序，排前面的小的先出堆。如果是降序，则排前面的大的先出堆。
        for (Integer x: cnt.keySet()) {
            pq.offer(x);
            if (pq.size() > k) {
                pq.poll(); // 始终保持堆的大小为k，这样插入删除才能O(logk)，而不是O(logN)。
            }
        }
        int[] res = new int[k];
        for (int i=0; i<k; i++) {
            res[i] = pq.poll();
        }
        return res;
    }
}
```

```java
// 桶排序，O(N)。
// 不过如果数据范围不集中，那么会消耗很大的内存，其中可能有一些桶没用到。
public List<Integer> topKFrequent(int[] nums, int k) {

	List<Integer>[] bucket = new List[nums.length + 1];
	Map<Integer, Integer> frequencyMap = new HashMap<Integer, Integer>();

	for (int n : nums) {
		frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
	}

	for (int key : frequencyMap.keySet()) {
		int frequency = frequencyMap.get(key);
		if (bucket[frequency] == null) {
			bucket[frequency] = new ArrayList<>();
		}
		bucket[frequency].add(key);
	}

	List<Integer> res = new ArrayList<>();

    // 从装出现次数最大的元素的桶开始，添加k个。
	for (int pos = bucket.length - 1; pos >= 0 && res.size() < k; pos--) {
		if (bucket[pos] != null) {
			res.addAll(bucket[pos]);
		}
	}
	return res;
}
```

```java
// 快排思想，快速选择。
// 平均时间复杂度为O(N)，最坏时间复杂度为O(N^2)。
class Solution {
    int[] unique;
    Map<Integer, Integer> count;

    public void swap(int a, int b) {
        int tmp = unique[a];
        unique[a] = unique[b];
        unique[b] = tmp;
    }

    // 双指针分割数组，出现频率小于pivot的在pivot左边，大于pivot的在pivot右边。
    public int partition(int left, int right, int pivot_index) {
        int pivot_frequency = count.get(unique[pivot_index]);
        // 1. move pivot to end
        swap(pivot_index, right);

        // 2. move all less frequent elements to the left
        for (int i = left; i <= right; i++) { // 注意合法的区间是[left, right]而不是[0, right]。
            if (count.get(unique[i]) < pivot_frequency) {
                swap(left++, i);
            }
        }

        // 3. move pivot to its final place
        swap(left, right);

        return left; // 返回主元的下标。
    }
    
    // [left, right].
    public void quickselect(int left, int right, int k_smallest) {
        /*
        Sort a list within left..right till kth less frequent element
        takes its place. 
        */

        // base case: the list contains only one element
        if (left == right) return;
        
        // select a random pivot_index
        Random random_num = new Random();
        int pivot_index = left + random_num.nextInt(right - left);  // 生成[left, right]范围内的随机数，先生成[0, right-left]范围内的随机数，再加上偏移量left即可。

        // find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index);

        // if the pivot is in its final sorted position
        if (k_smallest == pivot_index) {
            return;    
        } else if (k_smallest < pivot_index) {
            // go left
            // 小元较多，需要将这批小元再分少一点。
            quickselect(left, pivot_index - 1, k_smallest);     
        } else {
            // go right 
            // quickselect(pivot_index + 1, right, k_smallest-(pivot_index-left+1)); // 并不需要缩减k_smallest，因为递归终止条件是拿pivot_index和k_smallest进行比较，pivot_index是一个值的范围在[left, right]之间全局的下标，而不是base为left的下标，它的base仍然是0。
            quickselect(pivot_index + 1, right, k_smallest); 
        }
    }
    
    public int[] topKFrequent(int[] nums, int k) {
        // build hash map : character and how often it appears
        // 先用哈希表计数并去重。
        count = new HashMap();
        for (int num: nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        // array of unique elements
        int n = count.size();
        unique = new int[n]; 
        int i = 0;
        for (int num: count.keySet()) {
            unique[i] = num;
            i++;
        }
        
        // kth top frequent element is (n - k)th less frequent.
        // Do a partial sort: from less frequent to the most frequent, till
        // (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        // All element on the left are less frequent.
        // All the elements on the right are more frequent. 
        quickselect(0, n - 1, n - k); // 把n-k个最小的元放在左边，剩下的右边的k个元素就是top k了。
        // Return top k frequent elements
        return Arrays.copyOfRange(unique, n - k, n);
    }
}
```

# [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

> We have a list of `points` on the plane. Find the `K` closest points to the origin `(0, 0)`.
>
> (Here, the distance between two points on a plane is the Euclidean distance.)
>
> You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)
>
>  
>
> **Example 1:**
>
> ```
> Input: points = [[1,3],[-2,2]], K = 1
> Output: [[-2,2]]
> Explanation: 
> The distance between (1, 3) and the origin is sqrt(10).
> The distance between (-2, 2) and the origin is sqrt(8).
> Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
> We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
> ```
>
> **Example 2:**
>
> ```
> Input: points = [[3,3],[5,-1],[-2,4]], K = 2
> Output: [[3,3],[-2,4]]
> (The answer [[-2,4],[3,3]] would also be accepted.)
> ```
>
>  
>
> **Note:**
>
> 1. `1 <= K <= points.length <= 10000`
> 2. `-10000 < points[i][0] < 10000`
> 3. `-10000 < points[i][1] < 10000`

```java
// 快排思想，快速选择。
// 平均时间复杂度为O(N)，最坏时间复杂度为O(N^2)。
// 也可以用排序或堆。
class Solution {
    int[][] points;
    public int[][] kClosest(int[][] points, int K) {
        this.points = points;
        quickSelect(0, points.length-1, K);
        return Arrays.copyOf(points, K);
    }
    
    // [l, r].
    private void quickSelect(int l, int r, int kClosest) {
        if (l >= r) {
            return;
        }
        
        int pivot = new Random().nextInt(r-l)+l;
        int pivotIdx = partition(l, r, pivot);
        
        if (pivotIdx == kClosest) {
            return;
        } else if (pivotIdx < kClosest) {
            quickSelect(pivotIdx+1, r, kClosest);
        } else {
            quickSelect(l, pivotIdx-1, kClosest);
        }
    }
    
    private int partition(int l, int r, int pivot) {
        int pivot_distance = dis(pivot);
        
        // 把主元放到最后。
        swap(pivot, r);
        
        int i, j;
        for (i=l, j=l; j<r; j++) {
            if (dis(j) < pivot_distance) {
                swap(i++, j);
            }
        }
        
        // 把主元放到中间。
        swap(i, r);
        return i;
    }
    
    private void swap(int i, int j) {
        int[] temp = points[i];
        points[i] = points[j];
        points[j] = temp;
    }
    
    private int dis(int i) {
        // 注意到，虽然严格定义上要取平方根，但因为底数大，其平方根就大，所以只是为了判断大小，没必要花费算力求平方根。
        return points[i][0]*points[i][0]+points[i][1]*points[i][1];
    }
}
```

