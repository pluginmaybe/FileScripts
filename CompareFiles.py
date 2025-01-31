# -len <- show files of the same length
# -d <- only compare files in the same directory
# -smax n <- show biggest n files in a directory (where n is an integer)

# -log "log.txt" <- output results to a text file (default is "FileCompare.txt")

###
# take input arguments, decode and validate

# selected -> len function
# make a dictionary with lengths being the key, and filedata the values
# return keys that have more than one value
# as 
# key:
#   file
#   file

# selected -> smax function
# list the top n files by size
import sys
import os
import subprocess
import FileLib

log_filename = "logging.txt"

def try_parse_valid_int(s):
  try:
    return int(s)
  except ValueError:
    return 0

def parse_arguments():
  # Defaults
  compare_by_length = False
  same_directory = False
  list_largest = 0
  log_results = False
  validation_log = ""

  if len(sys.argv) <= 1:
    print("No arguments passed. ")
    return
  cl_commands = sys.argv[1:][0].split()
  #TODO delete - just for logging
  for item in cl_commands:
    print(f">> {item}")
  
  while len(cl_commands) > 0:
    instruction = cl_commands.pop(0)

    #TODO change to 'switch'-style ?
    if instruction == "-len":
      compare_by_length = True
      validation_log += "\nComparing lengths of files"

    elif instruction == "-d":
      same_directory = True
      validation_log += "\nUsing same directory"

    elif instruction == "-smax":
      if len(cl_commands) == 0:
        validation_log += "\nno max number value input. Using default 10"
      else:
        list_largest = try_parse_valid_int(cl_commands[0])
        cl_commands.pop(0)
        if list_largest <= 0:
          validation_log += "\nInvalid number given"
    
    elif instruction == "-log":
      #TODO add ability to edit file name
      validation_log += f"Logging results to {log_filename}"
      log_results = True

    else:
      validation_log += f"\nError: Command {instruction} not found"

  return compare_by_length, same_directory, list_largest, log_results, validation_log

def get_file_details(file_to_check):
  fileinfo = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_to_check], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  return float(fileinfo.stdout)


def comparing_files(extension):
  curr_dir = os.getcwd()

  file_dict = {}
  directories = [curr_dir]
  while directories != []:
    curr_dir = directories.pop()
    dirs = os.scandir(curr_dir)

    for item in dirs:
      if (item.is_dir()):
        directories.append(item.path)
      if (item.name.endswith(extension)):
        x = get_file_details(item.path)
        # get file length
        if file_dict.__contains__(item.path):
          file_dict[item.path] += x
        else:
          file_dict[item.path] = x

    return file_dict

      
def main():
  compare_by_length, same_directory, list_largest, log_results, validation_log = parse_arguments()
  results = ""
  
  if compare_by_length:
    results += "\nFiles found with identical length :"
    file_dict = FileLib.comparing_files(".mp4")
    for (k,v) in file_dict.items():
      results += f"\n{v} : {k}"
    #results += compare_file_lengths(same_directory)
  if list_largest > 0:
    results += f"\nThe largest {list_largest} files are :"
    #results += get_largest_files(list_largest)
  if validation_log != "":
    results += f"\n\nValidation log follows : {validation_log}" 
  if log_results:
    # logging_results_to_file()
    pass
  print(results, "\n")

  #get_file_details()



if __name__ == "__main__":
  main()