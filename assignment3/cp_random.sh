# csh
# this script will randomly copy specified number of files into a destination folder

# inputs:
# $1: source folder (without ending slash)
# $2: number of files
# $3: destination folder (without ending slash)

shuf -zen"$2" "$1"/* | xargs -0 mv -t "$3"/
