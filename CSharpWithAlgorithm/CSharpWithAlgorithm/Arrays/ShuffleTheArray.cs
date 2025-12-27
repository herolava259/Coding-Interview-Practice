using CSharpWithAlgorithm.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Arrays;

public class ShuffleTheArray : ISolution<int[]>
{
    private readonly int[] nums;
    private readonly int n;

    public ShuffleTheArray(int[] nums, int n)
    {
        this.nums = nums;
        this.n = n;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public int[] Solve()
    {

        int halfLength = nums.Length / 2;

        Span<int> results = stackalloc int[nums.Length];

        int fastIndex = 0;

        for(int i = 0; i < halfLength; ++i)
        {
            results[fastIndex++] = nums[i];
            results[fastIndex++] = nums[i + halfLength];
        }

        return results.ToArray();
    }
}
