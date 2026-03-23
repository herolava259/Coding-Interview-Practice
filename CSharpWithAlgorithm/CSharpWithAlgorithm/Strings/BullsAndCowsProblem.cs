namespace CSharpWithAlgorithm.Strings;

public static class BullsAndCowsProblem
{
    private static int GetOrInit(this Dictionary<char, int> counter, char key, int defaultValue = 0)
    {
        if (counter.ContainsKey(key))
        {
            return counter[key];
        }

        return counter[key] = defaultValue;
    }

    private static int GetOrDefault(this Dictionary<char, int> counter, char key, int defaultValue = 0)
    {
        if (counter.ContainsKey(key))
        {
            return counter[key];
        }

        return defaultValue;
    }
    public static string GetHint(string secret, string guess)
    {
        int numBulls = 0;

        var wrongSecretCounter = new Dictionary<char, int>();

        var wrongGuessCounter = new Dictionary<char, int>();

        foreach (var (cg, cs) in guess.Zip(secret))
        {
            if (cg == cs)
            {
                numBulls++;
                continue;
            }
            wrongSecretCounter[cs] = wrongSecretCounter.GetOrInit(cs) + 1;
            wrongGuessCounter[cg] = wrongGuessCounter.GetOrInit(cg) + 1;
        }
        var numCows = wrongSecretCounter.Keys.Concat(wrongGuessCounter.Keys)
                                             .ToHashSet()
                                             .Select(k =>
        {
            return Math.Min(wrongGuessCounter.GetOrDefault(k), wrongSecretCounter.GetOrDefault(k));
        }).Sum();
        return $"{numBulls}A{numCows}B";
    }
}
