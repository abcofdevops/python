"""
02_log_analyser.py
A simple log analyser that detects anomalies in log files based on error counts.
Usage: python 02_log_analyser.py <log_file_path> [output_option]
output_option: 1 for concise output, 2 for full log output
"""
import sys
import pandas as pd
from collections import Counter
import re

# Check if the log file path is provided
if len(sys.argv) < 2:
    print("Usage: python 02_log_analyser.py <log_file_path>")
    log_file = input("Please provide the log file path or press Enter to exit!! : ")
else:
    log_file = sys.argv[1]

# Check if the log file exists
if not log_file:
    print("Bye!! Log file path not provided.")
    sys.exit(1) 

log_entries = []


try:
    with open(log_file, "r") as file:
        for line in file:
            match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line.strip() )
            if match:
                timestamp, level, message = match.groups()
                log_entries.append([timestamp, level, message])
except FileNotFoundError:
    print(f"Log file '{log_file}' not found. Please check the path and try again.")
    sys.exit(1) 

df = pd.DataFrame(log_entries, columns=["timestamp", "level", "message"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

error_count = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30s"))

threshold = 3

def output_option():
    print("Output Options: \n1. Concise Output \n2. Full Log Output")
    while True:
        try:
            output = int(input("Please select from above for output [1 or 2] : "))
            if output in [1, 2]:
                return output
            else:
                print("Invalid option. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


# Check if output option is provided
if len(sys.argv) > 2:
    try:
        output = int(sys.argv[2])
        if output not in [1, 2]:
            output = output_option()
    except ValueError:
        output = output_option()
else:
    output = output_option()

# Print anomalies based on the threshold
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
