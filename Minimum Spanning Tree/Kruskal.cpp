#include "Kruskal.h"

int Kruskal(std::vector<std::pair<int, std::pair<int, int>>>& graph, std::vector<std::pair<int, int>>& mst, int n, int m) {

    int cost = 0;
    std::sort(graph.begin(), graph.end());
    std::vector<int> tree_id(n);
    std::iota(tree_id.begin(), tree_id.end(), 0);

    for (int i = 0; i < m; i++) {

        int a = graph[i].second.first;
        int b = graph[i].second.second;
        int c = graph[i].first;

        if (tree_id[a] != tree_id[b]) {
            cost += c;
            mst.push_back(std::make_pair(a, b));
            int old_id = tree_id[a];
            int new_id = tree_id[b];
            for (int j = 0; j < n; j++) {
                if (tree_id[j] == old_id) {
                    tree_id[j] = new_id;
                }
            }
        }
    }
    return cost;
}
