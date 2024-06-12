# Nmap-based Port Scanner

This Python script is a simple port scanner that utilizes the Nmap library to scan for open ports on a specified IP address. It allows users to input an IP address and a range of ports to scan, and it reports back the status of each port (open or closed).

## Features

- Utilizes the Nmap library for efficient port scanning.
- Supports scanning of a range of ports or all ports.
- Provides a multithreaded scanning process for faster results.
- Gracefully handles user input errors and exceptions.

## Usage

1. Clone the repository:

git clone https://github.com/clommm/Nmap-Port-Scanner.git

2. Navigate to the project directory:

cd (directory)

markdown
Copy code

3. Run the script:

python3 nmap_port_scanner.py

4. Follow the on-screen instructions to input the IP address and port range to scan.

## Requirements

- Python 3.x
- Python-nmap library
- Python pyfiglet

Install the required Python packages using pip:

pip install python-nmap
pip install pyfiglet

Otherwise, you can install Nmap from the official nmap website [here](https://nmap.org)
