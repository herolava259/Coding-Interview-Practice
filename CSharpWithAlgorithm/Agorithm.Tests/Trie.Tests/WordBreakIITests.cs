

using CSharpWithAlgorithm.Tries;

namespace Agorithm.Tests.Trie.Tests;

[TestFixture]
public class WordBreakIITests
{
    [Test]
    [TestCase("catsanddog", new string[] {"cat", "cats", "and", "sand", "dog"})]
    public void NormalCase(string s, string[] wordDict)
    {
        WordBreakIIProblem.WordBreak(s, wordDict);
    }
}
