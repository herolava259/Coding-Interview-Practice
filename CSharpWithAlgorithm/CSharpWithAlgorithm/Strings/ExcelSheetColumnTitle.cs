using System.Text;

namespace CSharpWithAlgorithm.Strings;

public class ExcelSheetColumnTitle
{
    public static string ConvertToTitle(int columnNumber)
    {
        var sb = new StringBuilder();
        columnNumber--;
        while (columnNumber > 0) { 
            sb.Append((char)((columnNumber % 26) + 'A'));
            columnNumber /= 26;
            columnNumber--;
        }

        return new string(sb.ToString().Reverse().ToArray());
    }
}
