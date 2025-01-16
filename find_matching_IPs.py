import requests

def read_ips(filename):
    with open(filename, "r") as file:
        return set(line.strip() for line in file)

def fetch_impacted_ips(url):
    response = requests.get(url)
    response.raise_for_status()
    return set(line.split(":")[0] for line in response.text.splitlines())

def find_matching_ips(our_ips_file, impacted_ips_url, output_file):
    our_ips = read_ips(our_ips_file)
    impacted_ips = fetch_impacted_ips(impacted_ips_url)
    
    matched_ips = our_ips.intersection(impacted_ips)
    
    with open(output_file, "w") as file:
        file.writelines(f"{ip}\n" for ip in matched_ips)

our_ips_file = "ourIPs.txt"
impacted_ips_url = "https://raw.githubusercontent.com/arsolutioner/fortigate-belsen-leak/refs/heads/main/affected_ips.txt"
output_file = "matchedIPs.txt"

find_matching_ips(our_ips_file, impacted_ips_url, output_file)

print(f"Matching IPs written to {output_file}")