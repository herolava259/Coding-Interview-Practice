using CSharpWithAlgorithm.Arrays;
using CSharpWithAlgorithm.Strings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Agorithm.Tests.Arrays.Tests;

[TestFixture]
public class CombinationSumIITests
{
    [SetUp]
    public void SetUp() { }

    [Test]
    [TestCase(new int[] { 10, 1, 2, 7, 6, 1, 5 }, 8)]
    public void NormalCases(int[] candidates, int target)
    {
        var reuslt = CombinationSumII.SolveCombinationSumII(candidates, target);
        IList<IList<int>> expectedResult = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]];
    }

}
