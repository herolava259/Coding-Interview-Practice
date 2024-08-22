function coinSums(n) {
    const coinValues = [1, 2, 5, 10, 20, 50, 100, 200];
    const numTypes = coinValues.length;

    const templateDp = [0,0,0,0,0,0,0,0]

    let dp = [[1,1,1,1,1,1,1,1]];

    for(let i = 1; i <= n; ++i)
    {
        //debugger;
        let curr = [...templateDp];
        for(let j = 0; j < numTypes; ++j)
        {
            let upperCoinVal = coinValues[j];

            if(j > 0)
            {
                curr[j] = curr[j-1];
            }

            if(upperCoinVal <= i)
            {             
                curr[j] += dp[i-upperCoinVal][j];
            }
        }

        dp.push(curr);
        //console.log('dp = ');
        //console.log(dp);
        //console.log('curr = ' + curr);
    }

    //console.log('dp[10] = ' + dp[10]);
    return dp[n][numTypes-1];
}
  
  //coinSums(200);