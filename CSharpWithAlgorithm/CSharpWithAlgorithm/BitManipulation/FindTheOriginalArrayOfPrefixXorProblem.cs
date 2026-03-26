namespace CSharpWithAlgorithm.BitManipulation;

public static class FindTheOriginalArrayOfPrefixXorProblem
{
    public static int[] FindArray(int[] pref)
    {
        var originArr = new int[pref.Length];
        originArr[0] = pref[0];

        for (int i = 1; i < pref.Length; i++)
            originArr[i] = pref[i] ^ pref[i - 1];

        return originArr;
    }
}
