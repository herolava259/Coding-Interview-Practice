
const inputs = [15, 20, 25, 30]
const expectedResults = [177, 324, 519, 755]

for(let i = 0; i < inputs.length; ++i)
{
    console.log("Test: Input n = " + inputs[i]);
    let result = distinctPowers(inputs[i]);
    console.log("Result: " + result);
    console.log("Expected Result: " + expectedResults[i]);
    console.log(result === expectedResults[i] ? "Passed" : "Failed");
    console.log('--------------------')
}

