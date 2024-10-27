using CSharpWithAlgorithm.Backtracking;
using CSharpWithAlgorithm.DynamicProgramming;
using CSharpWithAlgorithm.Heap;
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

//var n = 5;

//var sln = new PascalTriangle(n);

//var result = sln.Solve();

//for(int i = 0; i < n; i++)
//{
//    var r = result[i];

//    foreach (var item in r)
//    {
//        Console.Write($", {item}");
//    }

//    Console.WriteLine();
//}

int[] nums = [1, 1, 1, 2, 2, 3];
int k = 2;

var sln = new TopKFrequentElementsSolution(nums, k);

var result = sln.Solve();

Console.WriteLine(result);