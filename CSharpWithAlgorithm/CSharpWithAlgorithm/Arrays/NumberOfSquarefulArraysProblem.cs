using System.Collections.Immutable;

namespace CSharpWithAlgorithm.Arrays;

public static class NumberOfSquarefulArraysProblem
{
    private static IEnumerable<TResult> TriangleCombine<TElement, TResult>(this IList<TElement> sequence, Func<TElement, TElement,int, int TResult> resultSelector)
    {
        for (int i = 0; i < sequence.Count; i++) {
            for (int j = i + 1; j < sequence.Count; j++) {
                yield return resultSelector(sequence[i], sequence[j], i, j);
            }
        }
    }

    private static TValue GetOrInit<TKey, TValue>(this IDictionary<TKey, TValue> source, TKey key, Func<TValue> initFactory)
    {
        if(source.ContainsKey(key))
            return source[key];
        return source[key] = initFactory();
    }

    static int encode(params int[] indexes)
    {
        int bitMask = 0;
        foreach (var pos in indexes)
        {
            bitMask |= 1 << (pos % 32);
        }
        return bitMask;
    }


    static IEnumerable<int> decode(int bitMask)
    {
        var counter = 0;
        while (bitMask > 0)
        {
            if ((bitMask & 1) == 1)
                yield return counter;
            counter++;
            bitMask >>= 1;
        }
    }

    static bool contains(int bitMask, int pos)
        => (bitMask & (1 << pos)) != 0;

    static IEnumerable<int> primeSieve(int limit)
    {

        var notPrime = new SortedSet<int>();

        for (int i = 2; i <= limit; ++i)
        {
            if (!notPrime.Contains(i) && i < Math.Sqrt(limit))
            {
                for (int j = i * i; j < limit; j += i)
                {
                    notPrime.Add(j);
                }
            }
            else if (!notPrime.Contains(i))
            {
                yield return i;
            }

            notPrime.RemoveWhere(c => c <= i);
        }
    }

    static IEnumerable<int> analyseToPrimeFactors(int num, ImmutableSortedSet<int> primes)
    {
        if (num == 0)
            yield return num;

        foreach (var prime in primes)
        {
            if (num < prime)
                break;
            while (num > 1 && num % prime == 0)
            {
                yield return prime;
                num /= prime;
            }
        }
    }

    static bool isPerfectSquareNumber(int num, ImmutableSortedSet<int> primes)
    {
        if (num <= 1)
            return false;
        int valueCache = -1;
        int counterCache = 0;
        foreach (var primeFactor in analyseToPrimeFactors(num, primes))
        {
            if (valueCache == primeFactor)
            {
                counterCache++;
                continue;
            }

            if (counterCache % 2 == 1)
                return false;
            counterCache = 1;
            valueCache = primeFactor;
        }

        return true;
    }

    static int add(int bitMask, int pos)
        => bitMask | (1 << pos);


    static int factorial(int num)
    {
        int result = num;

        while (--num > 0) result *= num;

        return result;
    }

    static bool enough(int bitMask, int numOfElements)
    {
        int counter = -1;

        while (++counter < numOfElements && (bitMask & 1) == 1)
        {
            bitMask >>= 1;
        }
        return counter == numOfElements;
    }

    static int exclusive(int bitMask, int numOfElement)
    {
        var result = 0;

        for (int i = 0; i < numOfElement; i++) {

            if ((bitMask & (1 << i)) != 0)
                continue;
            result |= 1 << i;
        }

        return result;
    }


    private static IEnumerable<TResult> TriangleQuery<TElement, TResult>(this IList<TElement> sequence,
                                                                        Func<TElement, TElement, int, int, bool> filterCondition, 
                                                                        Func<TElement, TElement, int, int, TResult> resultSelector)
    {
        for (int i = 0; i < sequence.Count; i++)
        {
            for (int j = i + 1; j < sequence.Count; j++)
            {
                if (filterCondition(sequence[i], sequence[j], i, j))
                    yield return resultSelector(sequence[i], sequence[j], i, j);
            }
        }
    }

    private static void CountingMerge(this IDictionary<int, int> counter, IDictionary<int, int> other, int key)
    {
        foreach(var msk in other.Keys)
        {
            var newMsk = add(msk, key);

            if (!counter.ContainsKey(newMsk))
                counter[newMsk] = 0;

            counter[newMsk] += other[msk];
        }
    }

    private static bool FastCheckSquareNumber(int num)
    {
        var low = 0;
        var high = (int)Math.Ceiling(Math.Sqrt(num));

        while(low < high)
        {
            var mid = (low + high) >> 1;

            if (mid * mid == num) return true;
            else if (mid * mid < num) low = mid + 1;
            else high = mid - 1;
        }

        return false;
    }

    public static int SovleByDfsInGraph(int[] nums)
    {

        var graphAsLookup = nums.TriangleQuery((f, s, _, _) => FastCheckSquareNumber(f + s), 
                                                (_, _, fid, sid) => new (int, int)[] { (fid, sid), (sid, fid)})
                                .SelectMany(ps => ps)
                                .ToLookup(p => p.Item1, p => p.Item2);

        if (nums.Length << 1 != graphAsLookup.Count)
            return 0;

        var result = 0;

        void dfsCounting(int path, int u)
        {
            if(enough(path, nums.Length))
            {
                result++;
                return;
            }

            foreach(var v in graphAsLookup[u])
            {
                if (contains(path, v))
                    continue;
                dfsCounting(add(path, v), v);
            }
        }

        for (int i = 0; i < nums.Length; ++i) 
            dfsCounting(encode(i), i);

        return result / ;
    }

    static bool disjointed(int bitMskOne, int bitMskTwo)
        => (bitMskOne & bitMskTwo) == 0;

    static int union(int bitMskOne, int bitMskTwo)
        => bitMskOne | bitMskTwo;

    public static int SolveBySepratedDP(int[] nums)
    {
        var complementPairs = nums.TriangleQuery(
                                    (f, s, fid, sid) => FastCheckSquareNumber(f + s),
                                    (f, s, fid, sid) => (fid, sid));

        var bitMskPairs = complementPairs.Select(p => encode(p.fid, p.sid)).ToHashSet();

        var n = nums.Length;

        var numBits = (int)Math.Ceiling(Math.Log2(n));

        bool combinable(int pairOne, int pairTwo)
            => decode(pairOne).Any(a => decode(pairTwo).Any(b => bitMskPairs.Contains(encode(a, b))));


        int concat(int bitPairOne, int bitPairTwo)
        { 

            var exclusiveBitMsks = decode(bitPairOne).SelectMany(a => decode(bitPairTwo).Select(b => encode(a, b)))
                                                    .Where(p => bitMskPairs.Contains(p))
                                                    .SelectMany(p => decode(p))
                                                    .Distinct()
                                                    .ToArray()
                                                    ;
            return union(bitPairOne, bitPairTwo) ^ encode(exclusiveBitMsks);

        }


        var bases = Enumerable.Range(1, numBits)
                          .Aggregate(new List<Dictionary<int, Dictionary<int, int>>>() { Enumerable.Range(0, n).ToDictionary(c => encode(c), c => new Dictionary<int, int>() { { encode(c), 1 } }) },
                                     (acc, i) =>
                                     {
                                         var previous = acc[acc.Count - 1];

                                         var factor = i == 1 ? 4 : 1;

                                         acc.Add(previous.Keys.ToArray()
                                                              .TriangleQuery((i, j, ei, ej) => combinable(ei, ej),
                                                                             (i, j, ei, ej) => new KeyValuePair<int, Dictionary<int, int>>
                                                                                                      (key: concat(ei, ej), 
                                                                                                      value: previous[ei].SelectMany(kvi =>
                                                                                                                            previous[ej]
                                                                                                                                .Where(kvj => disjointed(kvi.Key, kvj.Key))
                                                                                                                                .Select(kvj =>
                                                                                                                                    new KeyValuePair<int, int>(union(kvi.Key, kvj.Key), factor * kvi.Value * kvj.Value / 2)))
                                                                                                                         .ToDictionary()
                                                                                                      )
                                                              )
                                                              .ToDictionary());

                                         return acc;
                                     })
                          .ToArray();


        var levels = decode(nums.Length).ToArray();

        var result = 0;

        var combinationDuplication = (int)Math.Pow(2, levels.Length - 1);

        if (n % 2 == 1)
            combinationDuplication >>= 1;

        void combine(int k, IList<int> combination, int headPair, int msk = 0)
        {
            if (k == levels.Length && enough(msk, n))
            {
                result += combination.Aggregate(1, (cr, tr) => cr * tr) / combinationDuplication;
                return;
            }
            else if (k >= levels.Length) 
                return;


            foreach(var kvi in bases[levels[k]].Where(kvr => combinable(kvr.Key, headPair)))
            {
                foreach(var kvj in kvi.Value.Where(kvc => disjointed(msk, kvc.Key)))
                {
                    combination.Add(kvj.Value);
                    combine(k + 1, combination, concat(kvi.Key, headPair), union(msk, kvj.Key));
                    combination.RemoveAt(combination.Count - 1);
                }
            }
        }

        return result / (nums.GroupBy(c => c).Select(c => c.Count()).Aggregate(1, (result, c) => result * factorial(c)) * factorial(levels.Length));
    }


    public static int NumOfSquarefulPermutation(int[] nums)
    {
        
        var primeSet = primeSieve(nums.Max() * nums.Length).ToImmutableSortedSet();

        var complementLookup = nums.TriangleCombine((first, second, firstIdx, secondIdx) => (isPerfectSquareNumber(first + second, primeSet), firstIdx, secondIdx))
                              .Where(tup => tup.Item1)
                              .ToLookup(tup => tup.Item2, tup => tup.Item3);
        

        if (complementLookup.Count != nums.Length)
            return 0;

        var dp = complementLookup.SelectMany(gr => gr.Select(c => new KeyValuePair<int, Dictionary<int, int>>(key: encode(gr.Key, c), value: new() { { encode(gr.Key, c), 2} })))
                                 .ToDictionary();
        var nextDp = new Dictionary<int, Dictionary<int, int>>();

        void computeNext(Dictionary<int, int> memory, Dictionary<int, Dictionary<int, int>> result, int head, int tail)
        {
            var candidates = complementLookup[head];
            foreach(var bitMsk in memory.Keys)
            {
                foreach(var cdPos in candidates.Where(p => !contains(bitMsk, p)))
                {

                    var newMask = add(bitMsk, cdPos);
                    var newHeadTail = encode(cdPos, tail);
                    var tb = result.GetOrInit(newHeadTail, () => new());

                    tb[newMask] = tb.GetValueOrDefault(newMask, 0) + memory[bitMsk];
                }
            }
        }

        int findResult(Dictionary<int, Dictionary<int, int>> computation)
            => computation.SelectMany(kvp => kvp.Value)
                          .Where(kvp => enough(kvp.Key, nums.Length))
                          .Select(kvp => kvp.Value)
                          .Sum();

        for (int i = 3; i <= nums.Length; ++i)
        {
            foreach(var kvp in dp)
            {
                var headTail = decode(kvp.Key).ToArray();
                var head = headTail[0];
                var tail = headTail[1];
                computeNext(kvp.Value, nextDp, head, tail);
                computeNext(kvp.Value, nextDp, tail, head);
            }

            dp = nextDp;
            nextDp = new();
        }

        var nOfDuplication = nums.GroupBy(c => c).Aggregate(1, (result, element) => result * factorial(element.Count()));

        return findResult(dp) / nOfDuplication;
    }
}
