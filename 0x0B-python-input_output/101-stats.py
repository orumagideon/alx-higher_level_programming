!/usr/bin/python3
import sys
import signal

"""Initialize variables to store metrics"""
total_file_size = 0
status_code_counts = {}

""" Define a function to handle SIGINT (CTRL + C) and print metrics"""
def handle_interrupt(sig, frame):
    print_metrics()

"""Register the signal handler for SIGINT"""
signal.signal(signal.SIGINT, handle_interrupt)

"""Function to print metrics"""
def print_metrics():
    print(f"File size: {total_file_size}")
    sorted_status_codes = sorted(status_code_counts.keys())
    for code in sorted_status_codes:
        count = status_code_counts[code]
        print(f"{code}: {count}")

line_count = 0

"""Read input lines from stdin"""
for line in sys.stdin:
    line_count += 1
    parts = line.split()
    
    """ Check if the line has the expected format"""
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = int(parts[-1])
        
        """ Update total file size"""
        total_file_size += file_size
        
        """Update status code counts"""
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1
        
        """ Print metrics every 10 lines"""
        if line_count % 10 == 0:
            print_metrics()
