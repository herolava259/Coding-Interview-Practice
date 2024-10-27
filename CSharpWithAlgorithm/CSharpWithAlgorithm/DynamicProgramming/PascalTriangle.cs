using CSharpWithAlgorithm.Interfaces;


namespace CSharpWithAlgorithm.DynamicProgramming;

public class PascalTriangle : ISolution<IList<IList<int>>>

{
    private readonly int n;

    public PascalTriangle(int n)
    {
        this.n = n;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public IList<IList<int>> Solve()
    {
        IList<IList<int>> rows = new List<IList<int>>();

        rows.Add(new List<int>() { 1 });
        rows.Add(new List<int>() { 1, 1 });

        for(int i = 3; i <= n; ++i)
        {
            var row = new List<int>();
            for(int j = 0; j < i; ++j)
            {
                var lastRow = rows[rows.Count - 1]; 
                if (j == 0)
                    row.Add(1);
                else if (j == i - 1)
                    row.Add(1);
                else
                    row.Add(lastRow[j-1] + lastRow[j]);

            }
            rows.Add(row);
        }

        return rows;
    }
}
