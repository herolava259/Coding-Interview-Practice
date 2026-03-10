using CSharpWithAlgorithm.Strings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Agorithm.Tests.String.Tests;

[TestFixture]
public class DifferentWaysToAddParenthesesTests
{
    [Test]
    [TestCase("2-1-1", new int[] { 0, 2})]
    [TestCase("2*3-4*5", new int[] { -34, -14, -10, -10, 10 })]
    public void NormalCase(string expression, int[] expectedResults)
    {
        var result = DifferentWaysToAddParentheses.DiffWaysToCompute(expression);

        Assert.AreEqual(result.Count, expectedResults.Length);

        foreach (var item in result.OrderBy(c => c).Zip(expectedResults.OrderBy(c => c)))
        {
            Assert.AreEqual(item.First, item.Second);
        }


    }
}
