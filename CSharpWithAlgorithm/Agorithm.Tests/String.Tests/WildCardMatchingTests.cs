using CSharpWithAlgorithm.Strings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Agorithm.Tests.String.Tests;

[TestFixture]
public class WildCardMatchingTests
{

    private sealed record Params(string Text, string Pattern);


    private sealed record Test(Params Params, bool Result);

    [SetUp]
    public void SetUp() { }

    [Test]
    [TestCase("aa", "a")]
    public void NormalCases(string text, string pattern)
    {
        var sln = new WildcardMatching(text, pattern);

        Assert.False(sln.Solve());
    }


    [Test]
    [TestCase("aa", "*")]
    public void NormalCases2(string text, string pattern)
    {
        var sln = new WildcardMatching(text, pattern);

        Assert.True(sln.Solve());
    }


    [Test]
    [TestCase("cb", "?a")]
    public void NormalCases3(string text, string pattern)
    {
        var sln = new WildcardMatching(text, pattern);

        Assert.False(sln.Solve());
    }


    [Test]
    [TestCase("ad", "a*", ExpectedResult =true)]
    public bool SpecialCases1(string text, string pattern)
    {
        var sln = new WildcardMatching(text, pattern);

        return sln.Solve();
    }
    [Test]
    public void MultipleCases()
    {

        var tests = new List<Test>
        {
            new Test(new Params("adecb", "*a*b"), false),
            new Test(new Params("adceb", "*a?b"), true),
            new Test(new Params("adceb", "?a*b"), false),
            new Test (new Params("adceb", "?a?b"), true)
            
        };


        tests.ForEach(t =>
        {
            var sln = new WildcardMatching(t.Params.Text, t.Params.Pattern);

            Assert.That(sln.Solve(), Is.EqualTo(t.Result));
        });


    }
}
