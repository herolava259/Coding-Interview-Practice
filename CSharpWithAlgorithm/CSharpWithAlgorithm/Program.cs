using CSharpWithAlgorithm.Backtracking;
using CSharpWithAlgorithm.DynamicProgramming;
//int[] nums = [1, 2, 3];

//var sln = new Subsets(nums);


//foreach (var item in sln.Solve())
//{
//    foreach (var c in item)
//    {
//        Console.Write($", {c}");
//    }

//    Console.WriteLine();

//}

var n = 5;

var sln = new PascalTriangle(n);

var result = sln.Solve();

for(int i = 0; i < n; i++)
{
    var r = result[i];

    foreach (var item in r)
    {
        Console.Write($", {item}");
    }

    Console.WriteLine();
}