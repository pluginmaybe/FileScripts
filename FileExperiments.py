import os

# Room for testing and experimenting with code blocks

dirs = os.scandir()

for item in dirs:
  print(item.path)

curr_dir = os.getcwd()

mp4s = {}
directories = [curr_dir]
while directories != []:
  curr_dir = directories.pop()
  print(curr_dir)
  dirs = os.scandir(curr_dir)

  for item in dirs:
    if (item.is_dir()):
      directories.append(item.path)
    if (item.name.endswith(".mp4")):
      # get file length
      if mp4s.__contains__(item.path):
        mp4s[item.path] += 1
      else:
        mp4s[item.path] = 1
      

print("Found MP4s")
for (k,v) in mp4s.items():
  print(k, v)

"""
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
           print(entry.name)
           """