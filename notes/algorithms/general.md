# [graph]

## depth first, dfs, [search]
## breadth first, bfs, [search]
## a star, a\*, [search]
## dijkstra, [search]

## floyd-warshall, [all pair shortest path], [path find], [dp]
```cpp
for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        }
    }
}
```

## edmonds-karp, ford-fulkerson, [flow], [max flow], [pending]
