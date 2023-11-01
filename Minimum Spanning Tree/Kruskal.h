#pragma once

#include <algorithm>
#include <numeric>
#include <vector>

int Kruskal(std::vector<std::pair<int, std::pair<int, int>>>& graph, std::vector<std::pair<int, int>>& mst, int n, int m);
