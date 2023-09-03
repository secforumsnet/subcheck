import requests
import socket
from colorama import Fore, Style
from tqdm import tqdm
import time

# Function to check subdomains
def check_subdomains(domain, subdomains):
    results = []

    # Initialize tqdm progress bar
    progress_bar = tqdm(total=len(subdomains), position=0, leave=True)

    for subdomain in subdomains:
        http_url = f"http://{subdomain}.{domain}"
        https_url = f"https://{subdomain}.{domain}"

        try:
            # Try making an HTTP request to the subdomain
            http_response = requests.get(http_url, timeout=5)
            http_status = http_response.status_code
        except requests.exceptions.RequestException:
            http_status = "Error"

        try:
            # Try making an HTTPS request to the subdomain
            https_response = requests.get(https_url, timeout=5)
            https_status = https_response.status_code
        except requests.exceptions.RequestException:
            https_status = "Error"

        # Resolve the IP address
        try:
            ip_address = socket.gethostbyname(subdomain + "." + domain)
        except socket.gaierror:
            ip_address = "N/A"

        # Display the results in real-time with green color for found subdomains with HTTP status code 200
        if http_status == 200 or https_status == 200:
            result = (
                f"{Fore.GREEN}Subdomain: {subdomain}{Style.RESET_ALL}\n"
                f"{Fore.GREEN}HTTP: {http_url} - Status Code: {http_status}{Style.RESET_ALL}\n"
                f"{Fore.GREEN}HTTPS: {https_url} - Status Code: {https_status}{Style.RESET_ALL}\n"
                f"{Fore.GREEN}IP Address: {ip_address}{Style.RESET_ALL}\n"
            )
            results.append(result)
            print(result)

        # Update the tqdm progress bar
        progress_bar.update(1)

    # Close the tqdm progress bar
    progress_bar.close()

    # Save the results to a file
    with open("subdomain_check_results.txt", "w") as file:
        file.write("\n".join(results))

# Main function
def main():
    # Input domain
    input_domain = input("Enter the domain to be checked (e.g., example.com): ").strip()

    # Read subdomains from a .txt file
    subdomains_file = input("Enter the path to the subdomains .txt file: ").strip()

    try:
        with open(subdomains_file, "r") as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File '{subdomains_file}' not found.")
        return

    if not subdomains:
        print("No subdomains found in the file.")
        return

    # Display the number of domains to be checked
    print(f"Number of domains to be checked: {len(subdomains)}")

    # Calculate an estimated time to finish
    start_time = time.time()

    # Check subdomains and display results with progress
    check_subdomains(input_domain, subdomains)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
