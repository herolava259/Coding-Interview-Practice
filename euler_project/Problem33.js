function digitCancellingFractions()
{
    return findCancellingFraction(2);
}

function findCancellingFraction(limitDigit = 2)
{
    const maxNum = 99;

    const minNum = 10;

    let res = {nume: 1, denom: 1};

    for(let nume = minNum; nume <= maxNum; ++nume)
    {
        for(let denom = nume+1; denom <= maxNum; ++denom)
        {
            //debugger;
            

            if(isCancellingFraction(nume, denom))
            {
                //console.log('nume: '+ nume + ', denom: '+ denom)
                res = simplyFraction(res.denom * denom, res.nume * nume);

                
            }
        }
    }

    //console.log(isCancellingFraction(49, 98));
    //let re = simplyFraction(4, 10)
    //console.log(re)
    return res.denom

}

function isCancellingFraction(nume, denom)
{
    let originSimpFrac = simplyFraction(denom, nume);

    

    let firstNumeDigit = Math.floor(nume / 10);
    let lastNumeDigit = nume % 10;


    let firstDenomDigit = Math.floor(denom / 10);
    let lastDenomDigit = denom % 10;

    //console.log('firsDenomDigit = '+ firstDenomDigit);
    //console.log('lastDenomDigit = ' + lastDenomDigit);

    if((firstNumeDigit === 0 && lastNumeDigit === 0)
        || (firstDenomDigit === 0 && lastDenomDigit === 0))
        return false;
    var result = false;
    if(firstDenomDigit === firstNumeDigit
        && firstDenomDigit !== 0
        && (lastNumeDigit !== 0 && lastDenomDigit !== 0))
    {
        result = result || compareFraction(originSimpFrac, {nume: lastNumeDigit, denom: lastDenomDigit});
    }

    if(firstNumeDigit === lastDenomDigit
        && firstNumeDigit !== 0
        && (lastNumeDigit !== 0 && firstDenomDigit !== 0))
    {
        result = result || compareFraction(originSimpFrac, {nume: lastNumeDigit, denom: firstDenomDigit});
    }
    

    if(lastNumeDigit === firstDenomDigit
        && lastNumeDigit !== 0
        && (firstNumeDigit !== 0 && lastDenomDigit !== 0))
    {
        result = result || compareFraction(originSimpFrac, {nume: firstNumeDigit, denom: lastDenomDigit})
    }

    if(lastNumeDigit === lastDenomDigit
        && lastDenomDigit !== 0
        && (firstNumeDigit !== 0 && firstDenomDigit !== 0))
    {
        result = result || compareFraction(originSimpFrac, {nume: firstNumeDigit, denom: firstDenomDigit});
    }

    return result;
}


function compareFraction(frac1, frac2)
{
    //console.log(frac1)
    let simpFrac1 = simplyFraction(frac1.denom, frac1.nume);
    let simpFrac2 = simplyFraction(frac2.denom, frac2.nume);
    return simpFrac1.denom === simpFrac2.denom 
            && simpFrac1.nume === simpFrac2.nume;
}

function simplyFraction(denom, nume)
{
    //debugger;
    let l = Math.max(denom, nume);
    let q = Math.min(denom, nume);
    let r = q;

    let checkTimeOut = false;
    let counter = 0;
    while((l % q) !== 0)
    {
        r = l % q;
        l = q;
        q = r;
        counter++;

        if(counter > 99)
        {
            checkTimeOut = true;
            break;
        }
    }

    if(checkTimeOut === true)
    {
        console.log('Time out nume: ' + nume+ ', denom: ' + denom);
    }
    return {denom: Math.floor(denom / r), nume: Math.floor(nume / r)};
}