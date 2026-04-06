namespace CSharpWithAlgorithm.Strings;

public static class LargestNumberSolution
{
    public class ComparasionRule : IComparer<string>
    {
        private int CompareRecursive(string a, string b)
        {
            if (a == b)
                return 0;
            else if (b == string.Empty)
                return 1;

            var lengthOfLoop = a.Length - (a.Length % b.Length);

            for (int i = 0; i < lengthOfLoop; ++i)
            {
                if (a[i] > b[i % b.Length])
                    return 1;
                else if (a[i] < b[i % b.Length])
                    return -1;
            }

            if (a.Length == b.Length)
                return 0;


            return -CompareRecursive(b, a.Substring(b.Length * (a.Length / b.Length)));
        }
        public int Compare(string? x, string? y)
        {
            if (x == null && y == null)
                return 0;
            else if (x == null)
                return -1;
            else if (y == null)
                return 1;

            return x.Length >= y.Length ? CompareRecursive(x!, y!) : -CompareRecursive(y!, x!);
        }
    }
    public static string Solve(int[] nums)
    {
        var countZero = nums.Count(c => c == 0);

        nums = nums.Where(c => c != 0).ToArray();

        if (nums.Length == 0)
            return "0";

        var numStrs = nums.Select(c => c.ToString()).ToArray();

        Array.Sort(numStrs, new ComparasionRule());


        return string.Join("", numStrs.Reverse()) + new string('0', countZero);
    }
}
