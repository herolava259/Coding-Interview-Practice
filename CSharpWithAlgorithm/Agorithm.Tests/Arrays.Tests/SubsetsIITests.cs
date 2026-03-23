using CSharpWithAlgorithm.Arrays;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Agorithm.Tests.Arrays.Tests;

[TestFixture]
public class SubsetsIITests
{
    [Test]
    [TestCase(new int[] { 1, 2, 2 })]
    public void NormalCase(int[] nums)
    {
        var result = SubsetsIIProblem.SubsetWithDuplicated(nums);
    }
}
