using CSharpWithAlgorithm.Interfaces;

namespace CSharpWithAlgorithm.Backtracking;

public class Subsets : ISolution<IList<IList<int>>>
{
    private readonly int[] nums;

    private readonly IList<IList<int>> results;

    public Subsets(int[] nums)
    {
        this.nums = nums;
        results = new List<IList<int>>();

        results.Add(new List<int>());
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public IList<IList<int>> Solve()
    {
        for(int i = 0; i < nums.Length; ++i)
        {
            Backtrack(new List<int>(), i);
        }

        return results;
    }

    private void Backtrack(IList<int> sln, int k = 0)
    {
        if(k == nums.Length)
        {
            results.Add(sln!.ToList());
            return;
        }
        sln.Add(nums[k]);
        for(int i = k +1 ; i <= nums.Length; ++i)
        {
            Backtrack(sln!, i);
            
        }
        sln.RemoveAt(sln.Count - 1);
    }
}
