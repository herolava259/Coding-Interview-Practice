using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Arrays;

public class CombinationSumII
{
    public static IList<IList<int>> SolveCombinationSumII(int[] candidates, int target)
    {
        var result = new List<IList<int>>();

        var frequencies = candidates.GroupBy(c => c)
                                    .ToDictionary(c => c.Key, c => c.Count());

        var keys = frequencies.Keys.ToArray();

        Array.Sort(keys);

        void backtrack(int[] keys, int begin, IDictionary<int, int> tries, int total)
        {
            if (total > target)
                return;
            if (total == target)
            {
                result.Add(tries.SelectMany(c => Enumerable.Repeat(c.Key, c.Value)).ToList());
                return;
            }

            if (begin >= keys.Length)
                return;

            for (int i = begin; i < keys.Length; ++i)
            {
                var elem = keys[i];

                for (int freq = 1; freq <= frequencies[elem]; ++freq)
                {
                    tries.Add(elem, freq);

                    backtrack(keys, i + 1, tries, total + freq * elem);

                    tries.Remove(elem);
                }
            }
        }


        backtrack(keys, 0, new Dictionary<int, int>(), 0);

        return result;

    }
}
