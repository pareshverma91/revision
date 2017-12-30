# [tree]
## binary search tree, bst
## segment tree
## fenwick, binary tree, bit
Stores partial (logarithmically) prefix sum as the value of an i.
```cpp
// update operation
for (; i < n; i += i & (-i)) value[i] += val
// query operation
sum = value[0];
for (; i > 0; i -= i & (-i)) sum += value[i]
```
## quad tree
## b-tree

# prefix sum
