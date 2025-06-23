# Log Analyser using Pandas

This project demonstrates how to analyze log files using Python's Pandas library. 

It contains three Python scripts that perform log analysis on a sample log file (`app.log`). Each script builds upon the previous one, adding more features and complexity to the analysis process. 

## Libraries and Dependencies
This project requires the following libraries and dependencies:
- Python 3.6 or higher
- Pandas library (for data manipulation and analysis)
- Regex library (for regular expressions)
- OS library (for operating system interactions)
- Sys library (for system-specific parameters and functions)


## Project Setup

To set up the project, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abcofdevops/python
   
   cd python/p06_log_analyser
    ```
2. **Install Python 3 and Pip**
    [Python Installation Guide](../README.md#python-installation-guide)

3. **Create a Virtual Environment (Optional but recommended)**

   It is recommended to create a virtual environment to manage dependencies for this project. You can do this using the following commands:
   ```bash
   python3 -m venv venv  # Create a virtual environment named 'venv'
   source venv/bin/activate  # Activate the virtual environment (Linux/MacOS)
   # or
   .\venv\Scripts\activate  # Activate the virtual environment (Windows)
   ```      
4. **Install Required Libraries**
   ```bash  
    pip3 install -r requirements.txt
   ```

5. **Run the Scripts**
   ```python
   python3 01_log_analyser.py app.log
   ```
   ```python
   python3 02_log_analyser.py app.log
   ```
   ```python
   python3 03_log_analyser.py app.log
   ```

##  How It Works
- Each script reads the `app.log` file.
- The log file `app.log` contains sample log entries that the scripts will analyze. It includes timestamps, log levels, messages, and other relevant information.   
- The scripts demonstrate different techniques for handling log data, such as using regular expressions for parsing, applying custom functions for data transformation, and leveraging Pandas' powerful data manipulation capabilities.
- The scripts utilize Pandas for data manipulation, allowing for efficient filtering, aggregation, and visualization of log data.   
