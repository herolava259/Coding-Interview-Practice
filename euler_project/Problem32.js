/*
Problem 32: Pandigital products
We shall say that an n-digit number is pandigital if it makes use of all the digits 1
to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through n pandigital.

Hint: Some products can be obtained in more than one way so be sure to only include it once in your sum.
*/ 

function pandigitalProducts(n) {

    const permutation = [];

    let result = 0;

    const productSet = new Set()

    for(let i = 1; i <= n; ++i)
    {
        permutation.push(i);
    }

    const numCheck = factorial(n);

    let currPerm = [...permutation];
    for(let i = 1; i <= numCheck; ++i)
    {
        //console.log('currPerm: ');
        //console.log(currPerm);
        let product = getPandigitalProducts(currPerm);
        if(product != 0) productSet.add(product);
        currPerm = nextPermutation(currPerm);
        
    }

    productSet.forEach(val => {
        result += val;
    });

    //console.log('result = ' + result);
    //console.log(getPandigitalProducts([3, 4, 2, 1]))



    return result;
}

function getPandigitalProducts(permArr)
{
    const n = permArr.length;

    const limit1 = Math.floor(n / 4) + 1;

    const limit2 = Math.floor(n / 2) + 1;

    for(let i = 0; i < limit1; ++i)
    {
        let multiplicand = getNumberFromDigits(permArr, 0, i);

        let remain = getNumberFromDigits(permArr, i+1, n-1);

        if(multiplicand >= remain) break;
        for(let j = i + 1; j < limit2; ++j)
        {
            let multiplier = getNumberFromDigits(permArr, i+1, j)
            let product = getNumberFromDigits(permArr, j+1, n-1);

            if(product <= multiplicand || product <= multiplier) break;

            if(product % multiplicand === 0 
                && Math.floor(product / multiplicand) === multiplier)
            {
                return product;
            }

        }
    }

    return 0;
}

function getNumberFromDigits(arr, begin, end)
{
    let pow10 = 1;
    let result = 0
    for(let i = end; i >= begin; --i, pow10 *=10)
    {
        result += arr[i] * pow10;
    }

    return result;
}

function factorial(n)
{
    let mult = 1;

    for(let i = 1; i <= n; ++i)
    {
        mult *= i;
    }

    return mult;
}
function nextPermutation(curr)
{
    const next = [...curr];
    if(next.length < 2) return next;
    if(next.length == 2 )
    {
        if(next[0] == 0)
        {
            swap(next, 0, 1);
        }

        return next;
    }
    let lowerId = next.length - 2;
    while(next[lowerId] >= next[lowerId+1] && lowerId >= 0)
    {
        lowerId--;
    }

    let swapId = next.length - 1;

    while(next[lowerId] >= next[swapId] && swapId > lowerId ) swapId--;

    swap(next, lowerId, swapId);

    let begin = lowerId + 1;
    let end = next.length - 1;

    while(begin < end)
    {
        swap(next, begin, end);
        begin++;
        end--;
    }


    return next;

}

function swap(arr, id1, id2)
{
    let tmp = arr[id1];
    arr[id1] ^= arr[id2];
    arr[id2] ^= arr[id1];
    arr[id1] ^= tmp;
}

  
pandigitalProducts(9);