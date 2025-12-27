using CSharpWithAlgorithm.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Arrays;

public class ConcatenateOfArray : ISolution<int[]>
{
    private readonly int[] nums;

    public ConcatenateOfArray(int[] nums)
    {
        this.nums = nums;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public int[] Solve()
    {
        Span<int> results = stackalloc int[2 * nums.Length];

        results.Fill(0);

        foreach(var num in nums)
        {
            results[num] = num;
            results[num + nums.Length] = num;
        }

        nums.AsSpan().CopyTo(results[0..nums.Length]);
        nums.AsSpan().CopyTo(results[nums.Length..(2 * nums.Length)]);

        return results.ToArray();
    }
}
