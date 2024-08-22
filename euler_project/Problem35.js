
function circularPrimes(n) {

    return n;
  }



function primeSieve(limit)
{
    const isPrimes = [];
    const results = [];

    for(let i = 0; i <= limit; ++i)
    {
        isPrimes.push(true);
    }

    isPrimes[0] = isPrimes[1] = false;

    for(let i = 2; i <= limit; ++i)
    {
        if(isPrimes[i] == true && i * i <=limit)
        {
            for(let j = i*i; j <= limit; j += i)
            {
                isPrimes[j] = false;
            }
        }
    }

    for(let i = 2; i <= limit; ++i)
    {
        if(isPrimes[i])
        {
            results.push(i);
        }
    }

    return results;
}