
namespace CSharpWithAlgorithm.Arrays;

public static class SubsetsIIProblem
{

    public static IList<IList<int>> SubsetWithDuplicated(int[] nums)
    {
        var counter = nums.GroupBy(c => c)
                          .ToDictionary(gr => gr.Key, gr => gr.Count());

        var uniques = counter.Select(g => g.Key).ToArray();

        IEnumerable<int> decode(int bitMask)
        {
            int idx = 0;

            while(bitMask > 0)
            {
                if (bitMask % 2 == 1)
                    yield return idx;
                bitMask >>= 1;
                idx++;
            }
        }

        var result = new List<IList<int>>();

        void backtrack(int[] frequency, int[] element, int k =0)
        {
            if(element.Length == k)
            {

                result.Add(element.Zip(frequency).SelectMany(p => Enumerable.Repeat(p.First, p.Second)).ToList());
                return;
            }

            for(int i =1; i <= counter[element[k]]; ++i)
            {
                frequency[k] = i;

                backtrack(frequency,element, k+1);
            }

        }

        for(int i = 0; i < Math.Pow(2, uniques.Length); ++i)
        {
            var indexes = decode(i).ToArray();

            backtrack(new int[indexes.Length], indexes.Select(idx => uniques[idx]).ToArray());
        }

        return result;
    }
}
