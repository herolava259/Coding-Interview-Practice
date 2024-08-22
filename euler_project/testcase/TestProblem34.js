const input = undefined;

var expectedResult = { sum: 40730, numbers: [145, 40585] };
var actualResult = digitFactorial();

console.log('Expected Result: ' +'sum ='+  expectedResult.sum + ', numbers: ' + expectedResult.numbers);
console.log('Actual Result: ' +'sum ='+  actualResult.sum + ', numbers: ' + actualResult.numbers);


function validateResult(){
    if(expectedResult.sum !== actualResult.sum)
    {
        return false;
    }

    if(expectedResult.numbers.length !== actualResult.numbers.length)
    {
        return false;
    }

    expectedResult.numbers.sort();
    actualResult.numbers.sort();

    for(let i = 0; i < expectedResult.numbers.length; ++i)
    {
        if(expectedResult.numbers[i] !== actualResult.numbers[i])
        {
            return false;
        }
    }

    return true;
}


console.log( validateResult() ? 'Pass!!!!' : 'Fail????');