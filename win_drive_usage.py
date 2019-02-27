#!/usr/bin/python3.5

import shutil,os,sys,glob

usage = shutil.disk_usage("C:\\")
used = (usage[1]//(1024*1024*1024))
print("Total usage is: ", str(usage[0]//(1024*1024*1024)) + "GB")
print("Used space is: ", str(usage[1]//(1024*1024*1024)) + "GB")
print("Free space is: ", str(usage[2]//(1024*1024*1024)) + "GB")
if used >= 180:
  folder_path = input("Please provide the folder you want to empty: ")
  for file_object in os.listdir(folder_path):
    file_object_path = os.path.join(folder_path, file_object)
    if os.path.isfile(file_object_path)
      os.unlink(file_object_path)
    else:
      shutil.rmtree(file_object_path)
