namespace CSharpWithAlgorithm.Interfaces;

public interface ISolution<out TResult>
{
    void Initialize();

    TResult Solve();
}
