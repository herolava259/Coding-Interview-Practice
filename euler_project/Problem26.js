/*
                  Problem 26: Reciprocal cycles
                  
A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
 It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < n for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
 */

function reciprocalCycles(n) {

    let maxLength = 0;
    let maxArg = 1;
    for(let i = 1; i <=n; i+=2)
    {
        if(i % 5 == 0)
        {
            continue;
        }
        let tmp = findReciprocalCycle(i)
        maxLength = Math.max(maxLength, tmp);
        maxArg = tmp >= maxLength ? i : maxArg;
    }

    //findReciprocalCycle(5);
    //console.log('maxArg = ' + maxArg);
    //console.log('maxLength = ' + maxLength);
    return maxArg;
  }

function findReciprocalCycle(n)
{
    if(n == 1) return 0;

    let divSet = new Set();
    let digits = [];

    let curr = 1;

    //let pow10 = 1;
   
    //console.log('curr = ' + curr);

    while(curr < n)
    {
        curr *= 10;
    }
    //console.log(divSet.has(curr))
    while(!divSet.has(curr))
    {
        
        let tmp = Math.floor(curr / n);
        divSet.add(curr);
        digits.push(tmp);
        //console.log(digits)
        curr %= n;

        let printStr = 'digits= '
        digits.forEach(n => {
            printStr += n;
            printStr += '; '
        })
        //console.log(printStr);
        //console.log(divSet);
        while(curr < n)
        {
            curr *= 10;
        }
        //break;

        
    }

    let firstVal = Math.floor(curr / n);

    while(digits.length > 0 && digits[0] != firstVal)
    {
        digits.shift();
    }

    //console.log(digits);

    return digits.length;
}

function findReciprocalCycle2(n)
{
    let pow10 = 10;

    if(n % 10 == 0) return 0;

    let factor5 = 0;

    let factor2 = 0; 

    while(n % 5 == 0)
    {
        factor5 += 1;
        n = Math.floor(n / 5);
    }

    while(n % 2 == 0)
    {
        factor2 += 1;
        n = Math.floor(n / 2);
    }

    
    //debugger;
    while( (pow10-1) % n != 0)
    {
        pow10 *= 10;
        //console.log('pow10 - 1 = ' + (pow10-1));
    }

    console.log('factor5 = ' + factor5);
    console.log('factor2 = ' + factor2);

    let pureCycle = Math.floor((pow10-1) / n);
    console.log(pureCycle);
    let remainder = Math.max(factor5, factor2) - Math.min(factor5, factor2);
    console.log('remainder = ' + remainder);

    pureCycle *= Math.pow(factor2 < factor5 ? 2 : 5, remainder);

    let upper = pureCycle * Math.floor(pow10, remainder);
    console.log('upper = ' + upper)

    pow10 *= Math.pow(10, Math.max(factor5, factor2));

    console.log('pow10 = ' + pow10);
    console.log('multi = ' + Math.pow(factor2 < factor5 ? 2 : 5, remainder));

    console.log(pureCycle)
    //let numDigit = pureCycle.toString().length;
    let additional = parseInt(pureCycle.toString().slice(0, Math.max(factor5, factor2))) || 0;

    pureCycle += additional;
    console.log(pureCycle)
    const result = parseInt(pureCycle.toString().slice(Math.max(factor5, factor2)));

    console.log(result);
    
    return result;
}



