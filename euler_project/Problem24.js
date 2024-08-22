function lexicographicPermutations(n)
{
    const permNumbers = getPermutationNumber(limit = 10);
    const choosenNumbers = [false, false, false, false, false, false, false, false, false, false];
    console.log(permNumbers);
    let level = 8;
    const results = [];
    let currNum = n;
    for(let i = 0; i <= 9; ++i)
    {
        console.log(currNum);
        console.log('level = ' + level);
        let counter = 0;
        if(currNum > permNumbers[level])
        {
            
            counter = Math.floor(currNum / permNumbers[level]);
            currNum -= counter * permNumbers[level];

        }

        //console.log(counter)
        for(let j = 0; j <= 9; ++j)
        {
            if(choosenNumbers[j] == false && counter == 0)
            {
                choosenNumbers[j] = true;
                //console.log(results);
                results.push(j);
                break;
            }
            else if(choosenNumbers[j] == false)
            {
                --counter;
            }
        }

        level = level >= 1 ? --level : 0;
    }

    let result = '';
    //console.log(results);
    results.forEach((val, key)=>{
        result += val;
    });

    return result;
}

function getPermutationNumber(limit = 10)
{
    let curr = 1;
    const results = [];
    for(let i =1; i <= limit; ++i)
    {
        curr *= i;

        results.push(curr);
    }

    return results;
}

function nextPermutation(curr)
{
    const next = [...curr];
    if(next.length < 2) return next;
    if(next.length == 2 )
    {
        if(next[0] == 0)
        {
            swap(next, 0, 1);
        }

        return next;
    }
    let lowerId = next.length - 2;
    while(next[lowerId] >= next[lowerId+1] && lowerId >= 0)
    {
        lowerId--;
    }

    let swapId = next.length - 1;

    while(next[lowerId] >= next[swapId] && swapId > lowerId ) swapId--;

    swap(next, lowerId, swapId);

    let begin = lowerId + 1;
    let end = next.length - 1;

    while(begin < end)
    {
        swap(next, begin, end);
        begin++;
        end--;
    }


    return next;

}

function swap(arr, id1, id2)
{
    let tmp = arr[id1];
    arr[id1] ^= arr[id2];
    arr[id2] ^= arr[id1];
    arr[id1] ^= tmp;
}

function swapElement(arr, id1, id2)
{
    [arr[id1], arr[id2]] = [arr[id2], arr[id1]];
}