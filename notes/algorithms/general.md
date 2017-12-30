{% tag ["graph"] %}

{% tag ["search"] %}
{% topicl "depth first", ["dfs"] %}

{% topicl "breadth first", ["bfs"] %}

{% topicl "a star", ["a\*"] %}

{% topicl "dijkstra" %}
{% endtag %}

{% topic "floyd-warshall", ["path find", "dp"] %}
All pair shortest path.
```cpp
for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        }
    }
}
```
{% endtopic %}

{% topicl "edmonds-karp", ["ford-fulkerson", "max flow", "pending"] %}

{% endtag %}
