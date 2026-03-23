using CSharpWithAlgorithm.Arrays;


namespace Agorithm.Tests.Arrays.Tests;

[TestFixture]
public class SpiralMatrixIITests
{
    [Test]
    [TestCase(3)]
    public void NormalCase(int n)
    {
        SpiralMatrixII.GenerateMatrix(n);
    }
}
