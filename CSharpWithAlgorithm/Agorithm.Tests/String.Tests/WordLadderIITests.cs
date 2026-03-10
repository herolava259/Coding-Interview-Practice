using CSharpWithAlgorithm.Strings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Agorithm.Tests.String.Tests;

[TestFixture]
public class WordLadderIITests
{
    [Test]
    [TestCase("a", "c", new string[] { "a", "b", "c" })]
    public void NormalCase(string beginWord, string endWord, string[] wordList)
    {
        var actualResult = WordLadderIIProblem.FindLadders(beginWord, endWord, wordList);
        Assert.AreEqual(0, 0);
    }
}
