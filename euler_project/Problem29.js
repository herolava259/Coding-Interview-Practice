function distinctPowers(n) {

    const MODK = 2000000007;
    
    const hashHit = new Set();
    
    for(let a = 2; a <= n; ++a)
    {
        let result = a;
        for(let b = 2; b <= n ; ++b)
        {
            result = (result * a) % MODK;

            hashHit.add(result);
        }
    }

    let result = hashHit.size;

    console.log(result);
    return result;
}


function getPrimesBySieve(n)
{
    const isPrimes = [];
    const results = [];

    for(let i = 0; i <= n +1; ++i)
    {
        isPrimes[i] = true;
        
    }

    isPrimes[0] = isPrimes[1] = false;

    for(let i = 2; i <= n + 1; ++i)
    {
        if(isPrimes[i] && i*i <= n+1)
        {
            for(let j = i * i; j <= n+1; j+=i)
            {
                isPrimes[j] = false;
            }
        }
    }

    for(let i = 2; i <= n+1; ++i)
    {
        if(isPrimes[i] == true)
        {
            results.push(i);
        }
    }

    return results;
}

distinctPowers(30);