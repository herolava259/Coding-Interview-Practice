using CSharpWithAlgorithm.Interfaces;


namespace CSharpWithAlgorithm.Heap;

public class TopKFrequentElementsSolution : ISolution<int[]>
{
    private readonly int[] nums;
    private readonly int k;

    public TopKFrequentElementsSolution(int[] nums, int k)
    {
        this.nums = nums;
        this.k = k;
    }
    public void Initialize()
    {
        throw new NotImplementedException();
    }

    public int[] Solve()
    {
        var frequencies = new Dictionary<int, int>();

        foreach(var item in nums)
        {
            if(frequencies.ContainsKey(item))
                frequencies[item]++;
            else frequencies[item] = 0;
        }

        var pq = new PriorityQueue<int, int>();

        foreach(var key in frequencies.Keys)
        {
            pq.Enqueue(key, -frequencies[key]);
        }

        var result = new int[k];

        for(var i = 0; i < k; ++i)
        {
            if (pq.Count == 0)
                break;
            result[i] = pq.Dequeue();
        }

        return result;
    }
}
