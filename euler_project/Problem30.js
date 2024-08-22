function digitnPowers(n) {

    let result = 0;

    

    let mine = 2;
    let maxe = 2 * Math.pow(10, 5);

    let curr = mine
    while(curr < maxe)
    {
        let tmp = curr;
        let sums = 0;
        //console.log('curr = ' + curr);
        while(tmp > 0)
        {
            sums += Math.pow(tmp % 10, n);
            tmp = Math.floor(tmp / 10);
            //console.log('tmp = ' + tmp);
            //console.log('sums = ' + sums);
        }

        if(sums == curr)
        {
            result += curr;
        }
        
        curr++;
    }

    console.log('result = ' + result);
    return result;
}
  
  digitnPowers(4);