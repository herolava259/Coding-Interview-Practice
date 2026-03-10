
namespace CSharpWithAlgorithm.Strings;


public class TreeNode
{
      public int val;
      public TreeNode left;
      public TreeNode right;
      public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
      {
        this.val = val;
        this.left = left;
        this.right = right;
      }

 }
public static class BinaryTreePathsProblem
{
    public static IList<string> Solve(TreeNode root)
    {
        if (root is null)
            return [];

        var paths = new List<string>();

        void dfsBuildPath(TreeNode? curNode, string prevPath)
        {
            if (curNode is null)
            {
                return;
            }

            var curPath = string.IsNullOrEmpty(prevPath) ? curNode.val.ToString() : $"{prevPath}->{curNode.val}";

            if (curNode.left is null && curNode.right is null)
            {
                paths.Add(curPath);
                return;
            }

            dfsBuildPath(curNode.right, curPath);
            dfsBuildPath(curNode.left, curPath);

        }

        dfsBuildPath(root, string.Empty);

        return paths;
    }
}
