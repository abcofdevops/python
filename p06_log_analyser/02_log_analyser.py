import sys
import pandas as pd
from collections import Counter
import re

log_file = sys.argv[1]

log_entries = []

with open(log_file, "r") as file:
    for line in file:
        match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line.strip() )
        if match:
            timestamp, level, message = match.groups()
            log_entries.append([timestamp, level, message])

df = pd.DataFrame(log_entries, columns=["timestamp", "level", "message"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

error_count = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30s"))

threshold = 3

if len(sys.argv) > 2:    
    output = int(sys.argv[2])
else:
    output = int(input("1. Concise Output\n2. Full Log Output \nPlease select from above for output [1 or 2] : "))

if output == 1:
    for time, count in error_count.items():
        if count > threshold:
            print(f"Anomaly detected {count} ERROR logs in 30 seconds at {time}")
else:
    for time, count in error_count.items(): 
        if count > threshold:
            print(f"-> Anomaly detected {count} ERROR logs in 30 seconds at {time}")
            print(df[df["timestamp"].dt.floor("30s") == time])
            print("#"*80)
