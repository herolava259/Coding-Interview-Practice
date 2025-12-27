namespace CSharpWithAlgorithm.Interfaces;

public interface ISolution<out TResult>
{
    void Initialize();

    TResult Solve();
}


public abstract class AbstractSolution<TResult> : ISolution<TResult>
{
    public abstract void Initialize();
    public abstract TResult Solve();



}