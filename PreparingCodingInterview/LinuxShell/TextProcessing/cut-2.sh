#Display the  and  character from each line of text.
#
#Input Format
#
#A text file with  lines of ASCII text only.
#
#Constraints
#
#Output Format
#
#The output should contain  lines. Each line should contain just two characters at the  and the  position of the corresponding input line.
#
#Sample Input
#
#Hello
#
#World
#
#how are you
#
#Sample Output
#
#e
#
#o
#
#oe

while read l
do
  ch2=$(echo $l | cut -c2)
  ch7=$(echo $l | cut -c7)
  res="$ch2$ch7"
  echo "$res"
done