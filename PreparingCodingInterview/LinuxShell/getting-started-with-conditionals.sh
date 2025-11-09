read c
if [ $c = "Y" -o $c = 'y']
then
    echo "YES"
else
    echo "NO"
fi

# Way 2
read X
if [ "$X" = "y"] || [ "$X" = "Y"];
then
  echo "YES"
elif [ "$X" = "n"] || ["$X" = "N"];
then
  echo "NO"
fi
