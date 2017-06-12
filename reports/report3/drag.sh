# push latest file
scp report2.tex a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/computer-vision-assignments/reports/report3/

# compile first
ssh a1700831@uss.cs.adelaide.edu.au "cd /users/1/a1700831/Codes/computer-vision-assignments/reports/report3 && sh -x remote.sh"

# drag back
scp a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/computer-vision-assignments/reports/report3/report3.pdf report3.pdf
