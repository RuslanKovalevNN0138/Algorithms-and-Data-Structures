using System;

namespace Leetcode839
{
    class UnionFind
    {
        private int[] rank;
        private int[] parents;

        public UnionFind(int size)
        {
            rank = new int[size];
            parents = new int[size];
            for (int i = 0; i < size; i++)
                parents[i] = i;
        }

        public int Find(int x)
        {
            if (parents[x] != x)
                parents[x] = Find(parents[x]);
            return parents[x];
        }

        public void Union(int x, int y)
        {
            int root_x = Find(x);
            int root_y = Find(y);

            if (root_x != root_y)
            {
                if (rank[root_x] < rank[root_y])
                    parents[root_x] = root_y;
                else if (rank[root_y] < rank[root_x])
                    parents[root_y] = root_x;
                else
                {
                    parents[root_x] = root_y;
                    rank[root_y]++;
                }
            }
        }
    }

    class Solution
    {
        public bool Similar(string a, string b)
        {
            int n = a.Length;
            int difference = 0;

            for (int i = 0; i < n; i++)
            {
                if (a[i] != b[i])
                {
                    difference++;
                }
            }
            return difference == 2 || difference == 0;
        }

        public int NumSimilarGroups(string[] strs)
        {
            int n = strs.Length;
            UnionFind uf = new UnionFind(n);

            int count = n;
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (Similar(strs[i], strs[j]) && uf.Find(i) != uf.Find(j))
                    {
                        uf.Union(i, j);
                        count--;
                    }
                }
            }
            return count;
        }
    }

    class MainClass
    {
        public static void Main()
        {
            string[] strs = new string[] { "tars", "rats", "arts", "star" };
            Solution solution = new Solution();
            int ans = solution.NumSimilarGroups(strs);
            System.Console.WriteLine("ans: " + ans);
        }
    }
}
