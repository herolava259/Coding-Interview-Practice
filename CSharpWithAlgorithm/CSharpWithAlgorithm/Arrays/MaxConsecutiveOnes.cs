using CSharpWithAlgorithm.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Arrays;

public class MaxConsecutiveOnes : ISolution<int>
{
    private readonly int[] nums;

    public MaxConsecutiveOnes(int[] nums)
    {
        this.nums = nums;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public int Solve()
    {
        var maxConsecutive = 0;

        var numConsecutive = 0;

        for(int i = 0; i < nums.Length; ++i)
        {
            if (nums[i] == 0)
            {
                maxConsecutive = Math.Max(maxConsecutive, numConsecutive);
                numConsecutive = 0;
            }
            else
                numConsecutive++;
        }

        maxConsecutive = Math.Max(maxConsecutive, numConsecutive);

        return maxConsecutive;
    }
}
