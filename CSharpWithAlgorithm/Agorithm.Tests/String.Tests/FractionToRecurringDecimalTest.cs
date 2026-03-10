using CSharpWithAlgorithm.Strings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Agorithm.Tests.String.Tests;

[TestFixture]
public class FractionToRecurringDecimalTest
{
    [Test]
    public void DivisibleTwoOrFiveTests()
    {
        Assert.AreEqual(true, FractionToRecurringDecimalProblem.OnlyDivisibleTwoOrFive(2));

    }

    [Test]
    //[TestCase(4, 333, "0.(012)")]
    [TestCase(1, 214748364, "0.00(000000465661289042462740251655654056577585848337359161441621040707904997124914069194026549138227660723878669455195477065427143370461252966751355553982241280310754777158628319049732085502639731402098131932683780538602845887105337854867197032523144157689601770377165713821223802198558308923834223016478952081795603341592860749337303449725)")]
    //[TestCase(1, 17, "0.(0588235294117647)")]
    //[TestCase(1, 2, "0.5")]
    //[TestCase(-1, -2147483648, "0.0000000004656612873077392578125")]
    //[TestCase(12, 9765625, "-0.000000026624")]
    //[TestCase(1, 6, "0.1(6)")]
    public void NormalCase(int numerator, int denominator, string expectedResult)
    {
        Assert.AreEqual(expectedResult, FractionToRecurringDecimalProblem.FractionToDecimal(numerator, denominator));
    }
}
