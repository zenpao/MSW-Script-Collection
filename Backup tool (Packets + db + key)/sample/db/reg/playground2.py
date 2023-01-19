import os, shutil, time, traceback, datetime
from datetime import datetime
from future.backports.datetime import timedelta

date_end = input("""
[SAMPLE] yyyy-mm-dd -> 2022-06-12
    Enter END date range: """)
date_end = datetime.strptime(date_end, '%Y-%m-%d') + timedelta(days=1)
print(date_end)

date_end_format = str(date_end).replace(" 00:00:00", "")
print(date_end_format)