using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpWithAlgorithm.Interfaces
{
    public interface ISolution<TResult>
    {
        void Initialize();

        TResult Solve();
    }
}
