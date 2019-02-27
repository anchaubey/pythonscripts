#!/usr/bin/python3.5

import csv

txt_file = r"/root/mytxt.txt"
csv_file = r"/root/mycsv.csv"

in_txt = cv.reader(open(txt_file, "rb"), delimeter = '\t')
out_csv = csv.writer(open(csv_file, "wb"))

out_csv.writerows(in_txt)
