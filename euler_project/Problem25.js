function digitFibonacci(n) {

    let nextDigits = initArr(n+2, 0);
    let prevDigits = initArr(n+2, 0);
    nextDigits[0] = prevDigits[0] = 1;
    //console.log(nextDigits);
    //console.log(sumDigits(nextDigits, prevDigits));

    let fibIdx = 2;

    let numDigit = 1;

    while(numDigit+1 < n)
    {
        let currDigits = sumDigits(prevDigits, nextDigits);
        fibIdx++;
        numDigit = getNumDigit(currDigits);

        prevDigits = nextDigits;
        nextDigits = currDigits;
        //console.log(currDigits);
    }

    console.log(fibIdx);
    return fibIdx;
}

function getNumDigit(digits)
{
    let result = digits.length-1;

    while(digits[result] == 0 && result >=0)
    {
        result--;
    }

    return result;
}
function sumDigits(digits1, digits2)
{
    const n = digits1.length;

    const result = initArr(n, 0);
    let residual = 0;
    for(let i = 0; i < n-1; ++i)
    {
        let sums = digits1[i] + digits2[i] + residual;

        result[i] = sums % 10;
        residual = Math.floor(sums / 10);
    }

    return result;
}

function initArr(numElem, initVal = 0)
{
    const result = [];

    for(let i = 0; i < numElem; ++i)
    {
        result.push(initVal);
    }

    return result;
}



