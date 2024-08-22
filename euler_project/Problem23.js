function sumOfNonAbundantNumbers(n) {

    const limit = 10000;
    const primes = getPrimesBySieve(n+1);

    const abundantNumbers = [];

    const sumPropMap = [];

    const isAbundants = [];

    sumPropMap.push(0);
    sumPropMap.push(1);
    isAbundants.push(false);
    isAbundants.push(false);


    for(let i = 2; i <= n; ++i)
    {

      let sumDiv = getSumPropDiv(i, sumPropMap, primes);
      sumPropMap.push(sumDiv);

      const isAbundant = sumDiv > 2 * i;
      if(isAbundant)
      {
        abundantNumbers.push(i);
        
      }

      isAbundants.push(isAbundant);
    }
    let result = sumNConsecutive(1, n);

    

    for(let i = 24; i <= n; ++i)
    {
        for(let j = 0; j < abundantNumbers.length; ++j)
        {
            let remainNum = i - abundantNumbers[j];
            if(remainNum <= 0) break;
            

            if(isAbundants[remainNum] == true)
            {
                result -= i;
                break;
            }
        }
    }
    return result;
}


function sumNConsecutive(first, end, step = 1)
{
    end -= first-1;
    first = 1;

    const numPair = Math.floor((end-first+1) / (2*step));


    return Math.floor((end+first)*(end-first+1) / (2*step));
}
function getSumPropDiv(num, prevSumDivs, primes)
{
  let curr = num;

  for(let i = 0; i < primes.length; ++i)
  {
    let prime = primes[i];
    let result = 0;
    if(curr % prime == 0)
    {
        curr = Math.floor(curr / prime );
        return calcSumProps(curr, prevSumDivs, prime);
    }
  }
}

function calcSumProps(divisor, prevSumDivMap, prime)
{
    let counter = 1;
    let curr = divisor;
    
    while(curr % prime == 0)
    {
        counter++;
        curr = Math.floor(curr / prime);

    }

    let oldFactor = getTotalOfExpo(prime, counter - 1);
    let newFactor = getTotalOfExpo(prime, counter);

    const result = Math.floor(prevSumDivMap[divisor] / oldFactor) * newFactor;

    return result;
}

function getPrimesBySieve(limit)
{
    const isPrimes = [];
    const results = [];

    for(let i = 0; i <= limit + 1; ++i)
    {
        isPrimes.push(true);
    }

    isPrimes[0] = isPrimes[1] = false;

    for(let i = 2; i <= limit + 1; ++i)
    {
        if(isPrimes[i] == true && i*i < limit+1)
        {
            for(let j = i*i; j <= limit + 1; j += i)
            {
                isPrimes[j] = false;
            }

        }

    }

    for(let i = 0; i <= limit + 1; ++i)
    {
        if(isPrimes[i]) results.push(i);
    }

    return results;
}

function sumProperDivisors(n, primes)
{

    let divMap = getProperDivisors(n, primes);

    let result = 1;

    divMap.forEach((val, key) => {
        result *= getTotalOfExpo(key, val);
    })

    return result - n;

}


function getProperDivisors(n, primes)
{
    let divMap = new Map();
    let curr = n;
    for(let i = 0; i < primes.length; ++i)
    {
        if(curr < prime)
        {
            break;
        }
        let prime = primes[i];
        if(curr % prime == 0)
        {
            divMap.set(prime, 1);
            curr = Math.floor(curr / prime);
        }

        while(curr % prime == 0)
        {
            divMap.set(prime, divMap.get(prime) + 1);
            curr = Math.floor(curr / prime);
        }
    }

    return divMap;
}

function getTotalOfExpo(factor, expo)
{
    if(factor == 1)
    {
        return 0;
    }
    return Math.floor((Math.pow(factor, expo + 1) - 1) / (factor - 1));
}

sumOfNonAbundantNumbers(28123);