# push latest file
scp main.tex a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/cv-reports/

# compile first
ssh a1700831@uss.cs.adelaide.edu.au 'sh -s' < remote.sh

# drag back
scp a1700831@uss.cs.adelaide.edu.au:/users/1/a1700831/Codes/cv-reports/main.pdf main.pdf
