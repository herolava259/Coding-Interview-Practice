using CSharpWithAlgorithm.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Strings;

public sealed class CountAndSay : ISolution<string>
{
    private readonly int n = 1;
    public CountAndSay(int n =1)
    {
        this.n = n;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public string Solve()
    {
        string currrROE = "1";

        for(int i =1; i < n; i++)
        {
            StringBuilder sb = new StringBuilder();
            char prevC = currrROE[0];
            int counter = 1;

            for(int j =1; j < currrROE.Length; ++j)
            {
                if(prevC !=  currrROE[j])
                {
                    sb.Append(counter)
                      .Append(prevC);
                    counter = 1;
                    prevC = currrROE[j];
                }
                else
                {
                    counter++;
                }
            }
            currrROE = sb.Append(counter)
                         .Append(prevC).ToString();


        }

        return currrROE;
    }
}
