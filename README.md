# Fortinet Vulnerability IP Checker

## Background
In 2022, Fortinet disclosed a critical authentication bypass vulnerability (**CVE-2022-40684**) affecting FortiOS, FortiProxy, and FortiSwitchManager. In January 2025, configurations from approximately **15,000 affected devices** were publicly released by the Belsen Group.

## Purpose
This Python script allows users to compare a list of their **public IP addresses** against the known affected list. This helps determine if their devices may be compromised and require immediate action.

## Features
- Checks your list of public IPs against the affected list.
- Provides a report on matches.
- Simple and easy to use.

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/fortinet-vuln-checker.git
   cd fortinet-vuln-checker
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```
3. Run the script:
   ```sh
   python find_matching_IPs.py
   ```
4. Files:
   
   Input File: https://raw.githubusercontent.com/arsolutioner/fortigate-belsen-leak/refs/heads/main/affected_ips.txt
   
   Input File ourIPs.txt: This is the file with your public IP addresses. IP addresses only supported. CIDR notation not supported.
   
   Output File matchedIPs.txt: This is the output file after the comparison.
   
## Disclaimer
This tool is provided for informational and security awareness purposes only. The authors are not responsible for misuse or damages resulting from its use.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Pull requests are welcome! Please ensure your contributions align with the project's scope and guidelines.

## Contact
For any issues or inquiries, feel free to open an issue on GitHub or reach out via email at `your-email@example.com`.

