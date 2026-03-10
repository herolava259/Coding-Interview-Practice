using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Strings;

public class RestoreIpAddrs
{
    public static bool ChainAsValidNumber(string chain)
    {
        if (chain.Length == 0)
            return false;
        if (chain == "0")
            return true;
        else if (chain.StartsWith('0'))
            return false;
        if(!(int.TryParse(chain, out var num) && num >= 0 && num < 256))
            return false;
        return true;

    }
    public static IList<string> RestoreIpAddresses(string s)
    {
        var results = new List<string>();

        void backtrack(Stack<string> parts, int begin = 0)
        {
            if (parts.Count > 4)
                return;
            else if (parts.Count == 4 && begin == s.Length)
            {
                results.Add(string.Join('.', parts.Reverse()));
                return;
            }
            else if (parts.Count == 4)
                return;

            for(int i = 1; i <= 3; ++i)
            {
                if (begin + i > s.Length)
                    break;
                var newPart = s.Substring(begin, i);

                if (ChainAsValidNumber(newPart))
                {
                    parts.Push(newPart);
                    backtrack(parts, begin + i);
                    parts.Pop();
                }
                else
                    break;
            }
        }

        backtrack(new Stack<string>());
        return results;
    }
}
