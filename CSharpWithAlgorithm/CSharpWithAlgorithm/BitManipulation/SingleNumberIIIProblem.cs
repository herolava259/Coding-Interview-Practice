
namespace CSharpWithAlgorithm.BitManipulation;

public static class SingleNumberIIIProblem
{

    public static int XorAll(this IEnumerable<int> nums)
        => nums.Aggregate(0, (result, num) => result ^ num);

    public static int XorRange(this IList<int> nums, int begin, int end)
    {
        var xorResult = 0;
        for (int i = begin; i < end; i++) {
            xorResult ^= nums[i];
        }

        return xorResult;
    }

    public static int[] SolveByDiffBit(int[] nums)
    {
        var xorBetween = nums.XorAll();

        var bitDiff = xorBetween & (-xorBetween);

        var num1 = 0;
        var num2 = 0;

        foreach(var num in nums)
        {
            if ((num & bitDiff) != 0)
                num1 ^= num;
            else
                num2 ^= num;
        }

        return [num1, num2];
    }

    private sealed class BitCounter
    {
        public int[] BitOnes { get; private init; } = new int[32];

        public int[] BitZeros { get; private init; } = new int[32];

        public void Update(int value)
        {
            int counter = 0;

            while (counter < 32)
            {
                if ((value & 1) == 1)
                    BitOnes[counter]++;
                else
                    BitZeros[counter]++;
                counter++;
                value >>= 1;
            }
        }

        public IEnumerable<bool> XorResult
            => BitOnes.Zip(BitZeros).Select(p => {
                var (one, _) = p;
                if (one == 0)
                    return false;
                return one % 2 == 1;
            });
    }

    private sealed class TenaryArray
    {
        private static int XorRule(int tenaryOne, int tenaryTwo)
        {
            return (tenaryOne, tenaryTwo) switch
            {
                (-1, -1) => 0,
                (-1, 0) => -1,
                (-1, 1) => 0,
                (0, -1) => -1,
                (0, 0) => 0,
                (0, 1) => -1,
                (1, -1) => 0,
                (1, 0) => 1,
                (1, 1) => 0,
                _ => throw new ArgumentException("Invalid argument $tenaryOne or $tenaryTwo")
            };
        }
        public int[] Triages { get; private init; } = new int[32];

        public void XorWith(int value)
        {
            int counter = 0; 
            while(counter < 32)
            {
                var bit = (value & 1);

                Triages[counter] = XorRule(Triages[counter], bit);

                value >>= 1;
                counter++;
            }
        }
    }

    private static int[] SolveByTenaryOperation(int[] nums)
    {
        var tenaryArr = new TenaryArray();
        var bitCounter = new BitCounter();

        var xorBetween = 0;

        foreach(var num in nums)
        {
            tenaryArr.XorWith(num);
            bitCounter.Update(num);
            xorBetween ^= num;
        }

        int numOne = 0;

        foreach(var (bit, idx) in bitCounter.XorResult.Zip(Enumerable.Range(0, 32)))
        {
            if(!bit)
            {
                numOne |= bitCounter.BitOnes[idx] > bitCounter.BitZeros[idx] ? 1 << idx : 0;
            }
            else
                numOne |= tenaryArr.Triages[idx] == 1 ? 1 << idx : 0;
        }

        return [numOne, xorBetween ^ numOne];
        
    }

    public static int[] SingleNumber(int[] nums)
    {
        return SolveByTenaryOperation(nums);
    }
}
