import socket
import re

def scan_url(url):
    # Parse the URL into its components
    try:
        protocol, host, path = re.findall(r"^(.*://)?(.*?)(/.*)?$", url)[0]
    except:
        print(f"Error parsing URL: {url}")
        return
    # Set the default protocol to HTTP if not specified
    if protocol is None:
        protocol = "http://"
    # Set the default path to the root if not specified
    if path is None:
        path = "/"
    # Create a socket object and connect to the target host
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 80))
    except socket.error as e:
        print(f"Error connecting to {host}: {e}")
        return
    # Send an HTTP GET request to the target host
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    s.send(request.encode())
    # Receive the response from the target host
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data
    # Decode the response into a string
    response_str = response.decode()
    # Check for vulnerabilities in the response
    # Check for possible SQL injection vulnerabilities
    if re.search(r"\b(select|insert|update|delete|drop|create)\b", response_str, re.IGNORECASE):
        print(f"Possible SQL injection vulnerability found in URL: {url}")
        # Add suggestions for fixing SQL injection vulnerabilities
        print("Suggested fix: Use parameterized queries instead of building SQL statements from user input")
    # Check for possible cross-site scripting (XSS) vulnerabilities
    if re.search(r"\b(script|onload)\b", response_str, re.IGNORECASE):
        print(f"Possible XSS vulnerability found in URL: {url}")
        # Add suggestions for fixing XSS vulnerabilities
        print("Suggested fix: Use input validation and output encoding to prevent script injection attacks")
    # Close the socket connection
    s.close()
    print(f"Scan completed for URL: {url}")
    print("No vulnerabilities found" if not re.search(r"\b(select|insert|update|delete|drop|create|script|onload)\b", response_str, re.IGNORECASE) else "")

if __name__ == "__main__":
    # Enter the URL to scan
    url = input("Enter the URL to scan: ")
    # Start scanning the URL for vulnerabilities
    scan_url(url)
