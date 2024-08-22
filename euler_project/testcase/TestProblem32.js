const test_cases = [4, 6, 7, 8, 9];
const expected_results = [12, 162, 0, 13458, 45228];

for(let i = 0; i < test_cases.length; ++i)
{
    console.log('Test i = ' + (i+1) + ', input arg = ' + test_cases[i]);
    console.log('Expected Result = ' + expected_results[i]);
    let actual_result = pandigitalProducts(test_cases[i]);

    console.log('Actual Result = ' +  actual_result);

    console.log(expected_results[i] === actual_result ? "Passed!!!" : "Failed???");

    console.log("-------------------------------------------------------------------")
}