# find and replace part/all of a filename
# FindAndReplace.py -p oldname newname 
# 1. -p "searched for substring" "replace filename with this" <- replace for 1 file
#       both must be valid strings
# 2. -f "searched for substring" "replace substring with this" <- replace for all instances
#       input must be valid string, output may be empty string <- unless this results in a empty filename
#NOTE : In all instances, check replacement filename is valid before replacing
# 3. -c <- Capitalise the first char of filename, lower case for the rest

# PATH -r "root path to search from" (default is current)
# -log "ReplaceLog.txt" <- output to a log file (default is "ReplaceLog.txt")
from dataclasses import dataclass
import sys
import FileLib

@dataclass
class Data:
  TitleCase: bool = False
  SingleFile: bool = True
  Logfilename: str = "ReplaceLog.txt"
  valid_arguments: bool = False
  validation_log: str = ""

def parse_arguments():
  print(sys.argv)
  if len(sys.argv) <= 1:
    print("No arguments passed. ")
    return
  cl_commands = sys.argv[1:]
  #TODO delete - just for logging
  for item in cl_commands:
    print(f">> {item}")
  
  while len(cl_commands) > 0:
    instruction = cl_commands.pop(0)

    #TODO change to 'switch'-style ?
    if instruction == "-p":
      try:
        oldname = cl_commands.pop(0)
        newname = cl_commands.pop(0)
      except:
        Data.validation_log += "\nInvalid entry"
        Data.valid_arguments = True
        return
      # search for file containing oldname
      oldfile, newfile = FileLib.search_files_replace_substring(oldname, newname)
      if oldfile == "":
        Data.validation_log += f"\nCouldn't find {oldname}"
        return
      # replace with new
      if oldfile == newfile:
        Data.validation_log += "\nUnable to rename file. Possible conflict with potential new name"
        return
      Data.validation_log += f"\nRenamed {oldfile} with {newfile}"

    elif instruction == "-f":
      try:
        oldname = cl_commands.pop(0)
        newname = cl_commands.pop(0)
      except:
        Data.validation_log += "\nInvalid entry"
        Data.valid_arguments = True
        return
      # search for file containing oldname
      oldfile, newfile = FileLib.search_files_replace_full(oldname, newname)
      if oldfile == "":
        Data.validation_log += f"\nCouldn't find {oldname}"
        return
      # replace with new
      if oldfile == newfile:
        Data.validation_log += "\nUnable to rename file. Possible conflict with potential new name"
        return
      Data.validation_log += f"\nRenamed {oldfile} with {newfile}"

    elif instruction == "-c":
      pass
    
    elif instruction == "-log":
      #TODO add ability to edit file name
      Data.validation_log += f"Logging results to {Data.log_filename}"
      Data.log_results = True

    else:
      Data.valid_arguments = False
      Data.validation_log += f"\nError: Command {instruction} not found"





def main():
  FileLib.write_text_to_file("atestfile.txt", "abcdef") # create a test file
  parse_arguments()

  print(Data.validation_log)

if __name__ == "__main__":
  main()