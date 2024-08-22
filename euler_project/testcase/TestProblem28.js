const testCases = [101, 303, 505, 1001]


for(let test of testCases)
{
    console.log("Test case, Input = " + test);
    console.log(spiralDiagonals(test));
}

spiralDiagonals(1001);