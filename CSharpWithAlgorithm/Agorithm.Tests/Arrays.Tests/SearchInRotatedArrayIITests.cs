
using CSharpWithAlgorithm.Arrays;

namespace Agorithm.Tests.Arrays.Tests;

[TestFixture]
public class SearchInRotatedArrayIITests
{
    [Test]
    //[TestCase(new int[] { 2, 5, 6, 0, 0, 1, 2 }, 0, true)]
    //[TestCase(new int[] { 2, 5, 6, 0, 0, 1, 2 }, 3, false)]
    //[TestCase(new int[] { 2, 5, 6, 0, 0, 1, 2 }, 0, true)]
    //[TestCase(new int[] { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1 }, 2, true)]
    //[TestCase(new int[] { 1 }, 0, false)]
    //[TestCase(new int[] { 1, 0, 1, 1, 1 }, 0, true)]
    //[TestCase(new int[] { 2, 2, 2, 2, 2}, 2, true)]
    //[TestCase(new int[] { 1, 3 }, 3, true)]
    [TestCase(new int[] { 1, 1, 1, 1, 3 }, 3, true)]
    public void NormalCase(int[] nums, int target, bool expected)
    {
        Assert.That(SearchInRotatedArrayIIProblem.Search(nums, target), Is.EqualTo(expected));
    }
}
