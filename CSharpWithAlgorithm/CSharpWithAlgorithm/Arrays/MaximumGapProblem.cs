
namespace CSharpWithAlgorithm.Arrays;

public static class MaximumGapProblem
{

    public static int MaximumGap(int[] nums)
    {
        var minElement = nums.Min(x => x);

        var maxElement = nums.Max(x => x);

        int size = maxElement - minElement;

        if (size == 0)
            return 0;

        var gap = Math.Max(1, (maxElement - minElement) / (nums.Length - 1));

        var buckets = new (int, int)[(maxElement - minElement) / gap + 1];

        Array.Fill(buckets, (int.MaxValue, int.MinValue));

        foreach(var num in nums)
        {
            var idx = (num - minElement) / gap;
            var (minOfBucket, maxOfBucket) = buckets[idx];

            buckets[idx] = (Math.Min(num, minOfBucket), Math.Max(num, maxOfBucket));
            
        }

        var prevCorner = buckets[0].Item2;
        var maxGap = 0;

        for(int i = 1; i < buckets.Length; i++)
        {
            if (prevCorner != int.MinValue && buckets[i].Item1 != int.MaxValue)
                maxGap = Math.Max(maxGap, buckets[i].Item1 - prevCorner);

            if (buckets[i].Item2 != int.MinValue)
                prevCorner = buckets[i].Item2;
        }

        return maxGap;


    }
}
