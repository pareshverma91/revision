## binary search tree, bst

## segment tree

## fenwick, bit, binary index tree
> Stores partial (logarithmically) prefix sum as the value of an i.
> ```cpp
> // update operation
> for (; i < n; i += i & (-i)) value[i] += val
> // query operation
> sum = value[0];
> for (; i > 0; i -= i & (-i)) sum += value[i]
> ```

## quad tree

## b-tree

## prefix sum

## set-disjoint, union-find
> Each node initialized as its own parent. When merging, set parent of one as the parent of the parent of the other. Short-circuit parents only when traversing. Membership querying.
