# push latest file
scp main.tex a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/computer-vision-assignments/reports/report1/

# compile first
ssh a1700831@uss.cs.adelaide.edu.au "cd /users/1/a1700831/Codes/computer-vision-assignments/reports/report1 && sh -x remote.sh"

# drag back
scp a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/computer-vision-assignments/reports/report1/main.pdf main.pdf
