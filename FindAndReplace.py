# find and replace part/all of a filename


# 1. -p "searched for substring" "replace with this" <- replace for 1 file
#       both must be valid strings
# 2. -f "searched for substring" "replace substring with this" <- replace for all instances
#       input must be valid string, output may be empty string <- unless this results in a empty filename
#NOTE : In all instances, check replacement filename is valid before replacing
# 3. -c <- Capitalise the first char of filename, lower case for the rest


# PATH -r "root path to search from" (default is current)
# -l "ReplaceLog.txt" <- output to a log file (default is "ReplaceLog.txt")

