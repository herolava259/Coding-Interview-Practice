for((i=1;i<=99;i++))
do
  if((i % 2 == 1))
  then
    echo "$i"
    fi
done

# Way 2

i=1
while [ $i -lt 100 ]
do
  if [ expr $i % 2 -ne 0 ];
  then
    echo $i
  fi;
i = expr $i + 1
done


for i in {1..100..2}
do
  echo $i
done