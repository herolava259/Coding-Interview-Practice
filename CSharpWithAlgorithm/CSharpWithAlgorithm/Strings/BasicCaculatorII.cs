

using System.Text;

namespace CSharpWithAlgorithm.Strings;

public static class BasicCaculatorII
{
    public static int Calculate(string s)
    {
        if (string.IsNullOrEmpty(s))
            return 0;

        var priority = new Dictionary<char, int>
        {
            ['+'] = 1,
            ['-'] = 1,
            ['*'] = 0,
            ['/'] = 0,
        };

        bool isOperator(char c)
            => "+-*/".Contains(c);
        bool isSign(char c)
            => "+-".Contains(c);
        bool isDigit(char c)
            => "0123456789".Contains(c);

        int compute(int a, int b, char oper)
            => oper switch
            {
                '+' => a + b,
                '-' => a - b,
                '*' => a * b,
                '/' => a / b,
                _ => 0
            };

        var operandBuilder = new StringBuilder();

        var operandStack = new Stack<int>();
        var operatorStack = new Stack<char>();
        var prevIsOperator = true;


        foreach (var c in s)
        {
            if (isOperator(c) && !prevIsOperator)
            {
                if (operandBuilder.Length > 0) operandStack.Push(int.Parse(operandBuilder.ToString()));
                operandBuilder.Clear();
                while (operatorStack.TryPeek(out var prevOper) && (priority[prevOper] <= priority[c]))
                {
                    var y = operandStack.Pop();
                    var x = operandStack.Pop();
                    operandStack.Push(compute(x, y, prevOper));
                    operatorStack.Pop();
                }
                operatorStack.Push(c);
                prevIsOperator = true;
            }
            else if (isDigit(c) || isSign(c))
            {
                operandBuilder.Append(c);
                prevIsOperator = false;
            }

        }

        if (operandBuilder.Length > 0) operandStack.Push(int.Parse(operandBuilder.ToString()));

        while (operatorStack.TryPeek(out var oper))
        {
            var y = operandStack.Pop();
            var x = operandStack.Pop();
            operandStack.Push(compute(x, y, oper));
            operatorStack.Pop();
        }

        return operandStack.Pop();
    }
}
