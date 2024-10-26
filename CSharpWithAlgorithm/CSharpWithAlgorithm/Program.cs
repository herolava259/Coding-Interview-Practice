using CSharpWithAlgorithm.Backtracking;

int[] nums = [1, 2, 3];

var sln = new Subsets(nums);


foreach (var item in sln.Solve())
{
    foreach (var c in item)
    {
        Console.Write($", {c}");
    }

    Console.WriteLine();

}
