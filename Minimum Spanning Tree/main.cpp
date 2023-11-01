#include "Kruskal.h"

#include <iostream>

int main() {
	int n, m;
	std::cin >> n >> m;

	std::vector<std::pair<int, std::pair<int, int>>> graph;
	std::vector<std::pair<int, int>> res;

	for (int i = 0; i < m; i++) {
		int f, s, c;
		std::cin >> f >> s >> c;
		f--; s--;
		graph.push_back({ c,{f,s} });
	}

	std::cout << Kruskal(graph, res, n, m);
}