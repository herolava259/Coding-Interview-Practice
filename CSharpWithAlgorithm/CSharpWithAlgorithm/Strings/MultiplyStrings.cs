using CSharpWithAlgorithm.Extensions;
using CSharpWithAlgorithm.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Strings;

public sealed class MultiplyStrings : ISolution<string>
{
    private readonly string num1;
    private readonly string num2;

    public MultiplyStrings(string num1, string num2)
    {
        this.num1 = num1;
        this.num2 = num2;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public string Solve()
    {
        Dictionary<int, int[]> multiplyCache = new Dictionary<int, int[]>();

        Func<string, int[]> ToIntArray = s => s.Select(c => c-'0').Reverse().ToArray();

        Func<int[], int, int, bool, int[]> PaddingSide = (int[] arr, int expectedLength, int value, bool leftSide) 
                => leftSide ? [..Enumerable.Repeat(value, expectedLength - arr.Length), ..arr] 
                            : [..arr, ..Enumerable.Repeat(value, expectedLength - arr.Length)];

        Func<int[], int, int[]> PaddingZeroToRight = (int[] arr, int expectedLength)=> PaddingSide(arr, expectedLength,0,false);


        IEnumerable<int> AddExtent(int[] me, int[] you)
        {
            int length = Math.Max(me.Length, you.Length);

            if (length > me.Length)
                me = PaddingZeroToRight(me, length);
            if (length > you.Length)
                you = PaddingZeroToRight(you, length);

            var residual = 0;
            for(int i = 0; i < length; ++i)
            {
                var total = me[i] + you[i] + residual;
                yield return total % 10;

                residual = total / 10;
            }

            if(residual > 0)
            {
                yield return residual;
            }
        }

        IEnumerable<int> AtomicMultiply(int[] arr, int num)
        {
            int residual = 0;
            for(int i =0; i < arr.Length; ++i)
            {
                var prod = arr[i] * num + residual;

                yield return prod % 10;

                residual = prod / 10;
            }

            if(residual > 0)
                yield return residual;
        }

        Func<int[], int, int[]> LeftShiftDecimal = (int[] arr, int leftShift) => [.. Enumerable.Repeat(0, leftShift), .. arr];

        var result = new int[0];

        var one = ToIntArray(num1);
        var two = ToIntArray(num2);

        // explain: num1 = 123, num2 = 321
        // calc: 123 * 321

        for(int i = 0; i < two.Length; i++)
        {
            // step i: take num1 multiply with element of num2
            // ex:Step 0: 123 * 1

            // get digit at position i of num2:
            var factor = two[i];


            // computation cache
            if(!multiplyCache.ContainsKey(factor))
            {
                multiplyCache[factor] = AtomicMultiply(one, factor).ToArray();
            }

            result = AddExtent(result, LeftShiftDecimal(multiplyCache[factor], i)).ToArray();

        }
        IEnumerable<int> AlignResult(int[] arr)
        {
            bool yieldable = false; 
            foreach(var e in arr.Reverse())
            {
                if (e == 0 && !yieldable)
                    continue;
                else if(!yieldable)
                    yieldable = true;
                yield return e;
            }


        }


        result = AlignResult(result).ToArray();

        if (result.Length == 0)
            result = [0];
        return String.Join("",result);
    }
}
