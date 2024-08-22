function quadraticPrimes(range) {

    const lower = -range;
    const upper = range;

    const primes = primeSieve(range);
    const primeSet = new Set(primes);
    //console.log(primes);

    let result = 0;
    let maxN = 0

    for(let b of primes){
        let mina = Math.max(0-(b + 1), lower+1);

        for(let a = mina ; a < range; ++a)
        {
            let tmp = maxFormula(a, b, maxN);

            if(tmp > maxN)
            {
                result = a * b;
                maxN = tmp ;
                //console.log('maxN = ' + maxN);

                //console.log('a = ' + a);
                //console.log('b= '+ b);
            }
        }
    }

    //console.log(result)
    return result;
}


function maxFormula(a, b, prevN = 0)
{
    if(!isPrime(fPrime(a,b,prevN)))
    {
        return -1;
    }

    let cDown = prevN - 1;

    while(cDown >= 0)
    {
        if(!isPrime(fPrime(a,b,cDown)))
        {
            return -1;
        }

        cDown--;
    }

    let cUp = prevN + 1;

    while(isPrime(fPrime(a,b,cUp)))
    {
        cUp++;
    }

    return cUp-1;

}

function fPrime(a,b,n)
{
    return Math.pow(n, 2) + n * a + b;
}
function isPrime(num)
{
    if(num < 0) return false;
    const sqrtNum = Math.floor(Math.sqrt(num)) +1;

    for(let i = 2; i <= sqrtNum; ++i)
    {
        if(num % i == 0)
        {
            return false;
        }
    }

    return true;

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