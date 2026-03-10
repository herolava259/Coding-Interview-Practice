using System.Text;


namespace CSharpWithAlgorithm.Strings;

public static class DifferentWaysToAddParentheses
{
    public interface IElement
    {
        public bool IsNumber { get; }

        public bool IsOperator { get; }
    }
    public struct OperandElement : IElement
    {
        public bool IsNumber => true;
        public int Value { get; init; }

        public bool IsOperator => false;

        public static bool IsValid(string chain)
            => !string.IsNullOrEmpty(chain) && chain.All(c => Char.IsDigit(c));

        public static OperandElement FromString(string chain)
        {
            if (!IsValid(chain))
                throw new ArgumentException("Invalid chain, chain is not a representation for non-sign interger");

            return new OperandElement() { Value = int.Parse(chain) };
        }
    }

    public enum OperatorType : ushort
    {
        Add,
        Sub,
        Mult
    }

    public struct OperatorElement : IElement
    {

        public bool IsNumber => false;

        public bool IsOperator => true;

        public OperatorType Type { get; init; }

        public static readonly OperatorElement Add = new() { Type = OperatorType.Add};
        public static readonly OperatorElement Sub = new() { Type = OperatorType.Sub };
        public static readonly OperatorElement Mult = new() { Type = OperatorType.Mult };

  
        public int Compute(int x, int y)
            => Type switch
            {
                OperatorType.Sub => x - y,
                OperatorType.Add => x + y,
                OperatorType.Mult => x * y,
                _ => 0
            };
        public static bool IsValid(char c)
            => c == '+' || c == '*' || c == '-';

        public static OperatorElement FromChar(char c)
        {
            if (!IsValid(c))
                throw new ArgumentException("Invalid character");
            return c switch
            {
                '+' => Add,
                '-' => Sub,
                '*' => Mult,
                _ => throw new NotSupportedException()
            };
        }
    }

    public static OperatorElement AsOperator(this IElement element)
    {
        return (OperatorElement)element;
    }

    public static OperandElement AsOperand(this IElement element)
    {
        return (OperandElement)element;
    }

    public static IList<int> DiffWaysToCompute(string expression)
    {
        
        IElement[] split(string expr)
        {
            var buffer = new StringBuilder();

            var result = new List<IElement>();

            foreach(var e in expr)
            {
                if (OperatorElement.IsValid(e) && buffer.Length > 0)
                {
                    result.Add(OperandElement.FromString(buffer.ToString()));
                    buffer.Clear();
                }

                if(OperatorElement.IsValid(e))
                {
                    result.Add(OperatorElement.FromChar(e));
                }
                else if(Char.IsDigit(e))
                {
                    buffer.Append(e);
                }
            }

            if (buffer.Length > 0)
                result.Add(OperandElement.FromString(buffer.ToString()));

            return result.ToArray();

        }

        var elements = split(expression);

        var n = elements.Length;

        var numOperand = (n / 2) + 1;

        var dp = Enumerable.Range(0, numOperand)
                           .Select(i =>
                           {
                               return Enumerable.Range(0, numOperand)
                                         .Select(j =>
                                         {
                                             return i == j ? new List<int> { elements[i << 1].AsOperand().Value } : [];
                                         })
                                         .ToArray();
                           })
                           .ToArray();

        var operators = elements.Zip(Enumerable.Range(0, elements.Length))
                                .Where(c => c.Second % 2 == 1)
                                .Select(c => c.First.AsOperator())
                                .ToArray();

        IEnumerable<int> computeBetween(int high, int low, int sep)
        {
            var calculator = operators[sep - 1];

            foreach(var r1 in dp[high][sep])
                foreach(var r2 in dp[sep - 1][low])
                {
                    yield return calculator.Compute(r2, r1);
                }
        }

        for(int i = 1; i < numOperand; i++)
        {
            for(int j = i-1; j >= 0; --j)
            {
                for(int k = i; k > j; --k)
                {
                    dp[i][j].AddRange(computeBetween(i, j, k));
                }
            }
        }


        return dp[numOperand-1][0];
    }
}
