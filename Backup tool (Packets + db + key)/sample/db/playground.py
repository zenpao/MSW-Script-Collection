import os, os.path, shutil, time, traceback, datetime
from datetime import timedelta, date
from pathlib import Path


date_end = "2022-06-12"
new_date = datetime.datetime.strptime(date_end, "%Y-%m-%d")
plus_date = new_date + datetime.timedelta(days=1)

print(plus_date)