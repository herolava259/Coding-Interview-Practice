
using System.Text;

namespace CSharpWithAlgorithm.Tries;

public static class WordBreakIIProblem
{
    private sealed class PrefixTrie
    {
        private readonly TrieNode _root = new TrieNode();
        private sealed record TrieNode
        {
            public Dictionary<char, TrieNode> Children { get; set; } = new();

            public int NumLeaf { get; set; } = 0;

            public int NumChain { get; set; } = 0;

            public TrieNode? GetChildOrNull(char key)
                => Children.TryGetValue(key, out var child) ? child : null;

            public TrieNode InitChild(char key)
                => Children[key] = new TrieNode();

            public bool TryGet(char key, out TrieNode? value)
            {
                if (Children.ContainsKey(key))
                {
                    value = Children[key];
                    return true;
                }
                value = null;
                return false;
            }

            public void RemoveWith(char key)
                => Children.Remove(key);
        }

        public void AddChain(string chain)
        {
            var curNode = this._root;

            foreach (var c in chain)
            {
                var nxtNode = curNode.GetChildOrNull(c);

                if (nxtNode == null)
                    nxtNode = curNode.InitChild(c);
                nxtNode.NumLeaf += 1;

                curNode = nxtNode;
            }

            curNode.NumChain += 1;
        }

        public bool FindChain(string chain)
        {
            var curNode = this._root;

            foreach (var c in chain)
            {
                if (!curNode.TryGet(c, out var nxtNode))
                    return false;
                curNode = nxtNode!;
            }

            return curNode.NumChain > 0;
        }

        public bool RemoveChain(string chain)
        {
            if (!FindChain(chain))
                return false;
            var curNode = this._root;

            foreach (var c in chain)
            {
                if (curNode.TryGet(c, out var nxtNode))
                    return true;
                nxtNode!.NumLeaf--;

                if (nxtNode.NumLeaf == 0)
                    curNode.RemoveWith(c);
                curNode = nxtNode!;
            }

            curNode.NumChain--;
            return true;
        }

        public IEnumerable<string> QueryAllPrefixes(List<char> path)
        {
            var curNode = this._root;

            var sb = new StringBuilder();

            for (int i = 0; i < path.Count; i++)
            {
                var c = path[i];
                sb.Append(c);

                if (!curNode.TryGet(c, out var nxtNode) || nxtNode!.NumLeaf == 0)
                    break;

                
                if (nxtNode.NumChain > 0)
                    yield return sb.ToString();
                curNode = nxtNode;
            }
            
        }
    }

    public static IList<string> WordBreak(string s, IList<string> wordDict)
    {
        var prefixTrie = new PrefixTrie();

        foreach (var chain in wordDict)
            prefixTrie.AddChain(chain);

        var path = new List<char>();

        IList<string>[] possibleWords = new List<string>[s.Length];

        for (int i = s.Length - 1; i >= 0; i--)
        {
            path.Insert(0, s[i]);
            possibleWords[i] = prefixTrie.QueryAllPrefixes(path).ToArray();
        }

        bool[] calculated = new bool[s.Length+1];
        var memory = new List<string>[s.Length + 1];

        memory[s.Length] = [string.Empty];
        calculated[s.Length] = true;

        List<string> calculate(int k)
        {
            if (k >= s.Length)
                return memory[s.Length];
            if (calculated[k])
                return memory[k];
            memory[k] = possibleWords[k].SelectMany(word => calculate(k + word.Length)
                                                            .Select(suff => suff == string.Empty ? word 
                                                                                                 : word + ' ' + suff))
                                        .ToList();

            calculated[k] = true;
            return memory[k];
        }

        //var dp = Enumerable.Range(0, s.Length+1)
        //                   .Select(_ => new List<string>())
        //                   .ToArray();
        //dp[dp.Length - 1] = [string.Empty];
        //for(int i = s.Length-1; i >= 0; --i)
        //{
        //    foreach(var word in possibleWords[i])
        //    {
        //        int j = i + word.Length;
        //        foreach(var p in dp[j])
        //        {
        //            dp[i].Add(word + " " + p);
        //        }
        //    }
        //}

        return calculate(0);
    }
}
