# Compare Files Script

# -len <- show files of the same length
# -d <- only compare files in the same directory
# -smax n <- show biggest n files in a directory (where n is an integer)
# -log "log.txt" <- output results to a text file (default is "FileCompare.txt")
# TODO add ability to change logfile text name
###
# take input arguments, decode and validate

# selected -> len function
# make a dictionary with lengths being the key, and list of filepaths the values
# return keys that have more than one value
# as 
# key: [file,.. file]

# selected -> smax function
# list the top n files by size
import sys
import FileLib
from dataclasses import dataclass

@dataclass
class Data:
  compare_by_length: bool = False
  same_directory: bool = False
  list_largest: int = 0
  log_results: bool = False
  validation_log: str = ""
  valid_arguments: bool = True
  log_filename = "FileCompare.txt"

def try_parse_valid_int(s):
  try:
    return int(s)
  except ValueError:
    return 0

def parse_arguments():
  print(sys.argv)
  if len(sys.argv) <= 1:
    print("No arguments passed. ")
    return
    #return compare_by_length, same_directory, list_largest, log_results, validation_log, valid_arguments
  cl_commands = sys.argv[1:]
  #TODO delete - just for logging
  for item in cl_commands:
    print(f">> {item}")
  
  while len(cl_commands) > 0:
    instruction = cl_commands.pop(0)

    #TODO change to 'switch'-style ?
    if instruction == "-len":
      Data.compare_by_length = True
      Data.validation_log += "\nComparing lengths of files"

    elif instruction == "-d":
      Data.same_directory = True
      Data.validation_log += "\nUsing same directory"

    elif instruction == "-smax":
      if len(cl_commands) == 0:
        Data.validation_log += "\nno max number value input. Using default 10"
      else:
        Data.list_largest = try_parse_valid_int(cl_commands[0])
        cl_commands.pop(0)
        if Data.list_largest <= 0:
          Data.validation_log += "\nInvalid number given"
    
    elif instruction == "-log":
      #TODO add ability to edit file name
      Data.validation_log += f"Logging results to {Data.log_filename}"
      Data.log_results = True

    else:
      Data.valid_arguments = False
      Data.validation_log += f"\nError: Command {instruction} not found"

##
      
def main():
  parse_arguments()
  results = ""
  
  if not Data.valid_arguments:
      results += f"\n\nValidation log follows : {Data.validation_log}" 
      print(results)
      return

  if Data.compare_by_length:
    results += "\nFiles found with identical length :"
    file_dict = FileLib.comparing_files(".mp4", Data.same_directory)
    for (k,v) in file_dict.items():
      if len(v) <= 1:
        continue
      results += f"\n{k} :"
      for value in v:
        results += f"\n{value}"
    
  if Data.list_largest > 0:
    results += f"\nThe largest {Data.list_largest} files are :"
    #TODO using results from above (compare by length) -> sort keys -> return top n results
    #results += get_largest_files(list_largest)
  
  if Data.validation_log != "":
    results += f"\n\nValidation log follows : {Data.validation_log}" 
  
  if Data.log_results:
    FileLib.write_text_to_file(Data.log_filename, results)
  print(results, "\n")

##

if __name__ == "__main__":
  main()