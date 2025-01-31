import os
import subprocess

# Helper functions for main scripts


def get_file_details(file_to_check):
  fileinfo = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_to_check], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  return round(float(fileinfo.stdout),0)

def search_files_replace_full(search_string, replace_string):
  found_filename = ""
  curr_dir = os.getcwd()

  directories = [curr_dir]
  while directories != [] and found_filename == "":
    curr_dir = directories.pop()
    dirs = os.scandir(curr_dir)

    for item in dirs:
      if (item.is_dir()):
        continue
        #directories.append(item.path)
      if item.name.__contains__(search_string):
        found_filename = item.name
        if os.path.isfile(replace_string):
          return found_filename, found_filename
        # confirm change
        os.rename(item.name, replace_string)
        return found_filename, replace_string
  
  return found_filename, replace_string

def search_files_replace_substring(search_string, replace_string):
  found_filename = ""
  new_name = ""
  curr_dir = os.getcwd()

  directories = [curr_dir]
  while directories != [] and found_filename == "":
    curr_dir = directories.pop()
    dirs = os.scandir(curr_dir)

    for item in dirs:
      if (item.is_dir()):
        continue
        #directories.append(item.path)
      if item.name.__contains__(search_string):
        found_filename = item.name
        new_name = found_filename.replace(search_string, replace_string)
        # confirm change
        if os.path.isfile(new_name):
          return found_filename, found_filename
        os.rename(item.name, new_name)
        return found_filename, new_name
  
  return found_filename, new_name


def comparing_files(extension, same_dir):
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
        if file_dict.__contains__(x):
          file_dict[x].append(item.path)
        else:
          file_dict[x] = [item.path]
    if same_dir:
      break

  return file_dict
  
def write_text_to_file(filename, text):
  with open(filename, 'w') as writer:
    writer.write(text)
