/*
Problem 28: Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in an n by n spiral formed in the same way?
 */

function spiralDiagonals(n) {

    

    let cursor = 1;
    let step = 2;
    let sums = 0;

    while(cursor <= n*n)
    {
        sums += cursor;

        if(cursor >= (step+1) * (step+1))
        {
            step += 2;
        }

        cursor += step;
        // console.log("cursor = " + cursor);
        // console.log("sums = " + sums);
        // console.log("step = " + step);
        // console.log("---------------------------------");
    }

    console.log("result = " + sums);


    return sums;
}