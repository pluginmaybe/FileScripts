import os
import subprocess

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
  
def write_text_to_file(filename, text):
  with open(filename, 'w') as writer:
    writer.write(text)

