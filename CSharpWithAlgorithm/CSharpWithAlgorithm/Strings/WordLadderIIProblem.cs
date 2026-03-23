
namespace CSharpWithAlgorithm.Strings;

public static class WordLadderIIProblem
{
    public static IEnumerable<TResult> SlipItSelfNoDuplicate<TElement, TResult>(this IList<TElement> sequence, Func<TElement, TElement, TResult> resultSelector)
    {
        for (int i = 0; i < sequence.Count; ++i)
        {
            for (int j = i + 1; j < sequence.Count; ++j)
                yield return resultSelector(sequence[i], sequence[j]);
        }
    }

    private static IList<string> GetOrInitEmpty(this IDictionary<string, IList<string>> g, string word)
    {
        if (g.ContainsKey(word))
            return g[word];

        return g[word] = new List<string>();
    }

    private static HashSet<string> GetOrInitEmpty(this IDictionary<string, HashSet<string>> g, string word)
    {
        if (g.ContainsKey(word))
            return g[word];

        return g[word] = new HashSet<string>();
    }

    private static int GetOrInit(this IDictionary<string, int> counter, string word, int defaultValue = 0)
    {
        if (counter.ContainsKey(word))
            return counter[word];

        return counter[word] = defaultValue;
    }


    public static IList<IList<string>> FindLadders(string beginWord, string endWord, IList<string> wordList)
    {
        bool AreAdjancentWords(string wordOne, string wordTwo)
            => wordOne.Zip(wordTwo).Select(pair => pair.First == pair.Second ? 0 : 1).Sum() <= 1;

        IDictionary<string, IList<string>> buildNeighborWordGraph(IList<string> vocab)
        {
            var resultGraph = new Dictionary<string, IList<string>>();

            foreach (var (wordOne, wordTwo, isAdj) in vocab.SlipItSelfNoDuplicate((one, two) => (one, two, AreAdjancentWords(one, two))))
            {
                if (isAdj)
                {
                    resultGraph.GetOrInitEmpty(wordOne).Add(wordTwo);
                    resultGraph.GetOrInitEmpty(wordTwo).Add(wordOne);
                }
            }

            return resultGraph;
        }

        var resultList = new List<IList<string>>();
        void traceBack(IDictionary<string, HashSet<string>> traces, string curWord, int quota, IList<string>? currentPath = null)
        {
            if (currentPath is null)
                currentPath = new List<string>();

            // decrease to 1 for current word 
            if (--quota < 0)
                return;
            currentPath.Insert(0, curWord);
            if (curWord == beginWord)
            {
                resultList.Add(currentPath.ToList());
                currentPath.RemoveAt(0);
                return;
            }

            foreach (var prevWord in traces.GetOrInitEmpty(curWord))
            {
                traceBack(traces, prevWord, quota, currentPath);
            }
            currentPath.RemoveAt(0);
        }


        var queue = new Queue<string>(wordList.Where(c => c != beginWord).Where(c => AreAdjancentWords(c, beginWord)));
        var backwardTrace = new Dictionary<string, HashSet<string>>(queue.Select(c => new KeyValuePair<string, HashSet<string>>(key: c, value: new HashSet<string>() { beginWord })));
        var forwardTrace = new Dictionary<string, HashSet<string>>() { { beginWord, queue.ToHashSet() } };
        var scoreBoard = new Dictionary<string, int>(queue.Select(c => new KeyValuePair<string, int>(key: c, value: 2)));

        var adjWordGraph = buildNeighborWordGraph(wordList);

        while (queue.Count > 0)
        {
            var currentWord = queue.Dequeue();

            if (currentWord == endWord
                || scoreBoard.GetOrInit(currentWord, 2) >= scoreBoard.GetValueOrDefault(endWord, int.MaxValue))
                continue;

            var currentScore = scoreBoard.GetOrInit(currentWord, 2);

            // only choose adj-word of current-word only if:
            // + adj-word is new next-word to curr-word (is the first time when from the curr-word, one choose it)
            // + and the current-word is not the next of adj-word (the cur-word is not in forward-trace of adj-word)
            foreach (var nextWord in adjWordGraph.GetOrInitEmpty(currentWord)
                                                .Where(c => !forwardTrace.GetOrInitEmpty(c).Contains(currentWord)
                                                             && backwardTrace.GetOrInitEmpty(c).Add(currentWord)))
            {

                scoreBoard[nextWord] = Math.Min(currentScore + 1, scoreBoard.GetValueOrDefault(nextWord, int.MaxValue));

                forwardTrace.GetOrInitEmpty(currentWord).Add(nextWord);
                queue.Enqueue(nextWord);
            }
        }

        // potential to overflow-stack when back-track
        traceBack(backwardTrace, endWord, scoreBoard.GetOrInit(endWord, 2));

        return resultList;

    }
}
