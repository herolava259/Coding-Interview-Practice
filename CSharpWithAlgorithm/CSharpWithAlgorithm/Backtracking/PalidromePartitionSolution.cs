using CSharpWithAlgorithm.Interfaces;

namespace CSharpWithAlgorithm.Backtracking;

public class PalidromePartitionSolution : ISolution<IList<IList<string>>>
{
    private readonly string s;
    private readonly IList<IList<string>> partitions;

    public PalidromePartitionSolution(string s)
    {
        this.s = s;
        this.partitions = new List<IList<string>>();
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    private void Backtrack(int k, int n, IList<string> partition)
    {
        if(k == n)
        {
            partitions.Add(partition.ToList());
            return;
        }
        
        for(int i = k+1; i <= n; i++)
        {
            var substr = s.Substring(k, i - k);
            if (!IsPanlidrome(substr))
                continue;
            partition.Add(substr);
            Backtrack(i, n, partition);
            partition.RemoveAt(partition.Count-1);
        }


    }

    private bool IsPanlidrome(string s)
    {
        int firstP = 0, lastP = s.Length - 1;

        while (firstP < lastP) {
            if (s[firstP] != s[lastP]) {
                return false;
            }
            firstP++;
            lastP--;
        }

        return true;
    }

    public IList<IList<string>> Solve()
    {
        Backtrack(-1, s.Length, new List<string>());
        return this.partitions;
    }
}
