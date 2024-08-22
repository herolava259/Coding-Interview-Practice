/*
Problem 34: Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
 */


function digitFactorial() {

    var sum = 0;
    var numbers = [];

    let factorials = [];

    for(let i = 0; i <=9; ++i)
    {
      factorials.push(factorial(i));
    }

    console.log(factorials);

    let res = 6;
    

    for(let i =3; i <= 50_000; ++i)
    {
      //debugger;
      res = 0;
      let tmp = i;
      while(tmp > 0)
      {
        let r = tmp % 10;
        res += factorials[r];
        tmp = Math.floor(tmp / 10);
      }

      if(i == res)
      {
        sum += i;
        numbers.push(i)
      }
    }

    return { sum, numbers };
}

function factorial(n){

  let res = 1;

  for(let i = 1; i <= n; ++i)
  {
    res *= i
  }

  return res;
}
  