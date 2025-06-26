using System;
using System.Text;
using System.Collections.Generic;

namespace Leetcode753
{
    public class Solution
    {
        public string CrackSafe(int n, int k)
        {
            var seen = new HashSet<string>();
            var result = new StringBuilder();

            string start = new string('0', n - 1);

            DFS(start, k, seen, result);

            result.Append(start);
            return result.ToString();
        }

        private void DFS(string current, int k, HashSet<string> seen, StringBuilder result)
        {
            for(int x = 0; x < k; x++)
            {
                string neighbor = current + x;
                if( !seen.Contains(neighbor))
                {
                    seen.Add(neighbor);
                    DFS(neighbor.Substring(1), k, seen, result);
                    result.Append(x);
                }
            }
        }
    }

    public class MainProgram
    {
        
       public static void Main()
        {
            int n = 2, k = 2;
            Solution solution = new Solution();
            string ans = solution.CrackSafe(n, k);
            Console.WriteLine(ans);
        }
    }
}