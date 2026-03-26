namespace CSharpWithAlgorithm.Extensions;

internal static class IEnumerableExtension
{
    public static IEnumerable<int> UntilTo(this IEnumerable<int> source, int skipValue)
    {
        bool yieldable = false;
        foreach (var e in source)
        {
            if (e == skipValue && !yieldable)
                continue;
            else if (!yieldable)
                yieldable = true;

            yield return e;
        }
    }
}
