using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Strings;

public static class ExcelSheetColumnNumber
{
    public static int TitleToNumber(string columnTitle)
    {
        var columnNumber = 0;

        var factor = 1;

        foreach(var c in columnTitle.Reverse())
        {
            columnNumber += (c - 'A' + 1) * factor;
            factor *= 26;
        }

        return columnNumber;
    }
}
