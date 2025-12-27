using CSharpWithAlgorithm.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Strings;

public sealed class WildcardMatching : ISolution<bool>
{
    private readonly string text;
    private readonly string pattern;

    //private readonly char[] alphabets = Enumerable.Range('a', 26).Select(c => (char)c).ToArray();

    public WildcardMatching(string text, string pattern)
    {
        this.text = text;
        this.pattern = pattern;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public bool PartialMatch(string subTxt, string subPattern)
    {
        if (subTxt.Length == 0 && subPattern.Length == 0)
            return true;
        else if (subTxt.Length == 0)
            return subPattern.All(c => c =='*');
        else if (subPattern.Length == 0)
            return false;


        if (subPattern.StartsWith('?'))
            return PartialMatch(subTxt.Substring(1), subPattern.Substring(1));

        if (subPattern == "*")
            return true;
        else if (subPattern.StartsWith('*'))
        {
            foreach (var startIdx in Enumerable.Range(0, subTxt.Length))
            {
                if(PartialMatch(subTxt.Substring(startIdx), subPattern[1..]))
                    return true;
            }
        }

        if (subTxt[0] == subPattern[0])
            return PartialMatch(subTxt.Substring(1), subPattern.Substring(1));

        return false;
    }

    public bool Solve()
    {
        var s = text;
        var p = pattern;


        var dp = new bool[(s.Length+1)*(p.Length+1)];


        Func<int, int, int> IndexOf = (i, j) => i * (p.Length + 1) + j;

        Func<bool[], int, bool[]> Row = (arr, rowIdx) => arr[IndexOf(rowIdx,0)..IndexOf(rowIdx+1,0)];
        Func<bool[], int, bool[]> Col = (arr, colIdx) => arr.Zip(Enumerable.Range(0, arr.Length))
                                                            .Where(pair => (pair.Second % arr.Length) == colIdx)
                                                            .Select(pair => pair.First)
                                                            .ToArray();

        //Array.Fill(dp, false);

        dp[IndexOf(0, 0)] = true;

        for(int i =1; i <= p.Length; ++i)
        {
            dp[IndexOf(0, i)] = dp[IndexOf(0, i-1)] && (p[i-1] == '*');
        }


        for(int i = 1; i <= s.Length; ++i)
        {
            bool leak = false;
            for(int j=1; j <= p.Length; ++j)
            {
                

                dp[IndexOf(i, j)] = p[j-1] switch
                {
                    '?' => dp[IndexOf(i - 1, j - 1)],
                    '*' => dp[IndexOf(i-1, j)] || dp[IndexOf(i, j-1)],
                    _ => dp[IndexOf(i-1, j-1)] && (s[i-1] == p[j-1])
                };

                leak |= dp[IndexOf(i, j)];
            }

            if (!leak)
                return false;

        }



        return dp[dp.Length-1];
    }
}
