import os
import subprocess

# Helper functions for main script

def get_file_details(file_to_check):
  fileinfo = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_to_check], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  return round(float(fileinfo.stdout),0)


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

