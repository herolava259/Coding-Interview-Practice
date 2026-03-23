

namespace CSharpWithAlgorithm.Arrays;

public static class PascalTriangleIIProblem
{
    public static IList<int> GetRow(int rowIndex)
    {
        if (rowIndex == 0)
            return [1];
        else if (rowIndex == 1)
            return [1, 1];

        Span<int> dp = stackalloc int[35];
        Span<int> nxtDp = stackalloc int[35];


        dp[0] = 1; dp[1] = 1;

        for (int i = 2; i <= rowIndex; i++)
        {
            nxtDp[0] = nxtDp[i] = 1;
            for (int j = 1; j < i; j++)
            {
                nxtDp[j] = dp[j - 1] + dp[j];
            }

            var tmp = dp;
            dp = nxtDp;
            nxtDp = tmp;
        }

        return dp.ToArray().Take(rowIndex+1).ToArray();

    }
}
