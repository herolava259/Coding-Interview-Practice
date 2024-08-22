const test_cases = [50, 100, 150, 200]
const test_results = [451, 4563, 21873, 73682]

for(let i = 0; i < test_cases.length; ++i)
{
    console.log("Test i = " + (i+1) + ', input_arg = ' + test_cases[i]);
    console.log("Expected Result : " + test_results[i]);

    let tmp = coinSums(test_cases[i])
    console.log("Actual Result: " + tmp);

    console.log(tmp === test_results[i] ? 'Passed!!!': 'Failed???');
    console.log('-----------------------------------------------------');
}