#!/usr/bin/env python3

# Import necessary libraries
import nmap  # For performing network scans
import ipaddress  # For validating IP addresses
import re  # For regular expressions
import pyfiglet  # For creating ASCII art banners
import concurrent.futures  # For parallel execution of tasks
import sys  # For system-specific parameters and functions
from datetime import datetime  # For handling dates and times

# Compile a regular expression pattern to match the port range input
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

# Define minimum and maximum port numbers
port_min = 0
port_max = 65535

# Create and print an ASCII banner using pyfiglet
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Prompt the user to enter a valid IP address for scanning
while True:
    ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
    try:
        # Validate the entered IP address
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid IP address.")
        break
    except ValueError:
        # Inform the user if the IP address is invalid
        print("You entered an invalid IP address")

# Prompt the user to enter a valid port range for scanning
while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (e.g., 60-120) or type 'all' to scan all ports")
    port_range = input("Enter port range: ").strip().lower()
    if port_range == "all":
        # Set port range to all possible ports
        port_min = 0
        port_max = 65535
        break
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        # Extract and set the minimum and maximum ports from the user input
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

# Initialize the nmap PortScanner object
nm = nmap.PortScanner()

# Function to scan a single port
def scan_port(port):
    try:
        # Perform the scan on the specified port
        result = nm.scan(ip_add_entered, str(port))
        # Get the status of the port (open, closed, etc.)
        port_status = result['scan'][ip_add_entered]['tcp'][port]['state']
        return f"Port {port} is {port_status}"
    except KeyError:
        # Handle cases where the port is not responding
        return f"Port {port} is not responding"
    except Exception as e:
        # Handle any other exceptions that may occur
        return f"Cannot scan port {port}. Reason: {e}"

# Add a banner and scan details
print("-" * 50)
print("Scanning Target: " + ip_add_entered)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
    # Use a ThreadPoolExecutor to scan multiple ports in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Submit scan tasks for each port in the specified range
        futures = [executor.submit(scan_port, port) for port in range(port_min, port_max + 1)]
        # Print the result of each completed scan task
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
except KeyboardInterrupt:
    # Handle user interruption gracefully
    print("\nExiting Program !!!!")
    sys.exit()
except Exception as e:
    # Handle any other exceptions that may occur during scanning
    print(f"\nAn error occurred: {e}")
    sys.exit()
