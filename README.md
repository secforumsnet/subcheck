secforums.net

This Python script is designed to check a list of subdomains for a specified domain and display subdomains with an HTTP status code of 200 in real-time in the terminal. It also provides information about the number of domains to be checked, progress during the check, and an estimated time to finish. The results are saved to a text file for later reference.

Requirements:

Before running the script, you need to install the following Python libraries using pip:

requests: This library is used to make HTTP requests to the subdomains and retrieve HTTP status codes.

Installation:


pip install requests colorama tqdm



How to Run the Script:

Install the required libraries using the commands provided above.

Save the Python script to a file, e.g., subdomain_checker.py.

Prepare a text file (e.g., subdomains.txt) with a list of subdomains, one subdomain per line, to be checked.

Open your terminal or command prompt.

Navigate to the directory where the subdomain_checker.py script and subdomains.txt file are located.

Run the script by executing the following command:


python subdomain_checker.py

Follow the on-screen prompts to enter the domain to be checked (e.g., example.com) and the path to the subdomains text file (e.g., subdomains.txt).

The script will start checking the subdomains and display subdomains with an HTTP status code of 200 in real-time in the terminal. It will also show the total number of domains to be checked, progress, and an estimated time to finish.

The results will be saved in a text file named subdomain_check_results.txt in the same directory for future reference.

This script is a helpful tool for identifying subdomains that return a successful HTTP status code (200) and can be used for various purposes like security assessments and domain management.
