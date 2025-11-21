read sizex
read sizey
read sizez

if [[ $sizex -eq $sizey && $sizex -eq $sizez ]]
then
  echo "EQUILATERAL";
elif [[ $sizex -eq $sizey || $sizex -eq $sizez || $sizey -eq $sizez ]]
  then
    echo "ISOSCELES";
else
  echo "SCALENE"
fi