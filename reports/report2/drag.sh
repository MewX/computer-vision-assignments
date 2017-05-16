# push latest file
scp report2.tex a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/computer-vision-assignments/reports/report2/

# compile first
ssh a1700831@uss.cs.adelaide.edu.au "cd /users/1/a1700831/Codes/computer-vision-assignments/reports/report2 && sh -x remote.sh"

# drag back
scp a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/computer-vision-assignments/reports/report2/report2.pdf report2.pdf
