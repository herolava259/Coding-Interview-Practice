using System.Text;

namespace CSharpWithAlgorithm.Strings;

public static class FractionToRecurringDecimalProblem
{
    public class Residual
    {
        public int ActualLength { get; set; }

        public UInt128 Decimal { get; set; }

        public string AsRepeatesFraction
        {
            get
            {
                var decimalLength = Decimal.ToString().Length;
                return new string('0', Math.Max(0, ActualLength - decimalLength)) + Decimal.ToString();
            }
        }
    }

    public static bool OnlyDivisibleTwoOrFive(int num)
    {
        long numLong = Math.Abs((long)num);

        while (numLong > 0 && numLong % 2 == 0)
        {
            numLong /= 2;
        }

        while (numLong > 0 && numLong % 5 == 0)
        {
            numLong /= 5;
        }

        return numLong == 1;
    }

    public static Residual ComputeRecurringFractionalPart(int nume, int denom)
    {
        int numOfCharacter = 1;
        UInt128 expo = 10;

        UInt128 bigDenom = (UInt128)denom;
        UInt128 bigNume = (UInt128)nume;

        while (((expo - 1) * bigNume) % bigDenom != 0)
        {
            expo *= 10;
            numOfCharacter++;
        }

        return new Residual { Decimal = (expo-1) * bigNume / bigDenom, ActualLength = numOfCharacter};
    }

    public static (int, int, int) ExtractTwoAndFiveFactor(int num)
    {
        var twoCounter = 0;
        var fiveCounter = 0;

        while (num > 0 && num % 2 == 0)
        {
            num /= 2;
            twoCounter++;

        }

        while(num > 0 && num % 5 == 0)
        {
            num /= 5;
            fiveCounter++;
        }

        return (twoCounter, fiveCounter, num);
    }

    public static string RecurringFractionalDivide(int nume, int denom)
    {
        var sb = new StringBuilder();
        
        var signNum = Math.Sign(nume);
        var signDen = Math.Sign(denom);

        if(signNum != 0 && signNum != signDen)
        {
            sb.Append('-');
        }

        nume = Math.Abs(nume);
        denom = Math.Abs(denom);

        var intergerPart = nume / denom;

        if (intergerPart > 0)
            nume = nume % denom;

        sb.Append(intergerPart).Append('.');


        var (numTwoFactor, numFiveFactor, newDenom) = ExtractTwoAndFiveFactor(denom);

        var leadingZero =  Math.Max(numTwoFactor, numFiveFactor);

        var newNume = nume * (int)Math.Pow(2, Math.Max(0, numFiveFactor - numTwoFactor)) * (int)Math.Pow(5, Math.Max(0, numTwoFactor - numFiveFactor));

        var topFractional = newNume / newDenom;

        if (topFractional > 0)
        {
            newNume = newNume % newDenom;
            sb.Append(new string('0', Math.Max(0, leadingZero - topFractional.ToString().Length))).Append(topFractional);
        }
        else sb.Append(new string('0', leadingZero));

        var residual = ComputeRecurringFractionalPart(newNume, newDenom);

        sb.Append('(')
          .Append(new string('0', Math.Max(0, residual.ActualLength - residual.Decimal.ToString().Length)))
          .Append(residual.Decimal)
          .Append(')');

        return sb.ToString();
        
    }

    public sealed record CustomDecimal(bool Sign, UInt128 IntergerPart, UInt128 DecimalPart, int LeadingZero, bool HasRecurringFractional = false)
    {
        public string AsString{
            get
            {
                return (Sign ? "" : "-") + $"{IntergerPart}.{new string('0', LeadingZero)}" + (HasRecurringFractional ? $"({DecimalPart})" : DecimalPart.ToString());
            }
        }


    }



    public static CustomDecimal BigDecimalDivide(int nume, int denom)
    {
        UInt128 BigPow(UInt128 factor, int expo)
        {
            UInt128 result = 1;

            int counter = 0;

            while (counter++ < expo)
                result *= factor;
            return result;
        }
        bool determineSignOfResult(int nume, int denom) {
            if (nume == 0) return true;

            return Math.Sign(nume) == Math.Sign(denom);
        }
        int countFactorOf(UInt128 num, UInt128 factor)
        {
            if (num == 0)
                return 0;
            var result = 0;

            while(num % factor == 0)
            {
                result++;
                num /= factor;
            }

            return result;
        }

        var signOfResult = determineSignOfResult(nume, denom);

        var bigUNume = (UInt128)Math.Abs((long)nume);
        var bigUDenom = (UInt128)Math.Abs((long)denom);

        var intergerPart = bigUNume / bigUDenom;

        if(intergerPart > 0)
            bigUNume = bigUNume % bigUDenom;

        var numeFactorTwo = countFactorOf(bigUNume, 2);
        var numeFactorFive = countFactorOf(bigUNume, 5);

        var denomFactorTwo = countFactorOf(bigUDenom, 2);
        var denomFactorFive = countFactorOf(bigUDenom, 5);

        var remainPart = bigUNume / (BigPow(2, numeFactorTwo) * BigPow(5, numeFactorFive));

        var reducedFactorTwo = denomFactorTwo - numeFactorTwo;
        var reducedFactorFive = denomFactorFive - numeFactorFive;

        var complementFactorTwo = 0;
        var complementFactorFive = 0;

        if(reducedFactorTwo < 0)
        {
            remainPart *= BigPow(2, -reducedFactorTwo);
            reducedFactorTwo = 0;
        }

        if (reducedFactorFive < 0)
        {
            remainPart *= BigPow(5, -reducedFactorFive);
            reducedFactorFive = 0;
        }

        if(reducedFactorTwo > reducedFactorFive)
        {
            complementFactorFive = reducedFactorTwo - reducedFactorFive;
        }
        else
        {
            complementFactorTwo = reducedFactorFive - reducedFactorTwo;
        }

        remainPart *= BigPow(2, complementFactorTwo) * BigPow(5, complementFactorFive);

        var actualFractionalLength = Math.Max(reducedFactorTwo + complementFactorTwo, reducedFactorFive + complementFactorFive) ;

        return new CustomDecimal(signOfResult, intergerPart, remainPart, Math.Max(0, actualFractionalLength - remainPart.ToString().Length));
    }


    public static string FractionToDecimal(int numerator, int denominator)
    {
        if(numerator == 0)
            return "0";

        if (Math.Abs((long)numerator) >= Math.Abs((long)denominator) 
            && (Math.Abs((long)numerator) % Math.Abs((long)denominator) == 0))
            return (numerator / denominator).ToString();
        if (OnlyDivisibleTwoOrFive(denominator))
            return BigDecimalDivide(numerator, denominator).AsString;

        return RecurringFractionalDivide(numerator, denominator);
    }
}
