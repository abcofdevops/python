
"""
01_log_analyser.py
A simple log analyser that detects anomalies in log files based on error counts.
Usage: python 01_log_analyser.py
"""

import sys
import pandas as pd
from collections import Counter
import re

# log file path
log_file = "app.log"

log_entries = []

# Read the log file and parse entries
with open(log_file, "r") as file:
    for line in file:
        match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line.strip() )
        if match:
            timestamp, level, message = match.groups()
            log_entries.append([timestamp, level, message])

# Convert log entries to a DataFrame
df = pd.DataFrame(log_entries, columns=["timestamp", "level", "message"])

# Convert timestamp to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Count ERROR logs in 30-second intervals
error_count = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30s"))

# Print anomalies based on a threshold
threshold = 3

# Output anomalies if they exceed the threshold
for time, count in error_count.items():
    if count > threshold:
        print(f"Anomaly detected {count} ERROR logs in 30 seconds at {time}")