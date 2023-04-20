import socket
import re
import threading

# Define a function to scan a URL for vulnerabilities
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
    # Build the GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    # Send the GET request to the target host
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
    # Return the response for further processing
    return response_str


# Define a function to scan a response for SQL injection vulnerabilities
def scan_sql(response_str, url):
    # List of SQL injection keywords to look for
    sql_keywords = ["select", "insert", "update", "delete", "alter", "drop", "create", "truncate", "union", "join", "order by", "group by", "having", "exists", "not exists", "like", "in", "between"]
    # Search the response string for each SQL keyword
    vulnerable_queries = []
    for keyword in sql_keywords:
        match = re.search(rf"{keyword}\s.*[;\n]", response_str, re.IGNORECASE)
        if match:
            vulnerable_queries.append(match.group())
    # If vulnerable queries were found, print a report and suggest solutions
    if vulnerable_queries:
        print(f"SQL injection vulnerabilities found on {url}")
        for query in vulnerable_queries:
            print(f"Vulnerable query: {query}")
        print("Suggested solutions: Use prepared statements with parameterized queries, escape user input before using it in a SQL query, limit the privileges of the database user, and sanitize user input to prevent malicious SQL code from being executed.")
    else:
        print(f"No SQL injection vulnerabilities found on {url}")

# Define a function to scan a response for XSS vulnerabilities
def scan_xss(response_str, url):
    # Search the response string for potential XSS vulnerabilities
    vulnerable_elements = []
    for match in re.finditer(r"<\s*(script|iframe|img).*?>", response_str, re.IGNORECASE):
        element = match.group()
        if "src" in element:
            attribute = "src"
        elif "data" in element:
            attribute = "data"
        else:
            attribute = "content"
        # Check if the element's attribute contains user-controlled data
        user_input_match = re.search(rf"{attribute}\s*=\s*[\"']?(.*?)[\"']?\s*", element, re.IGNORECASE)
        if user_input_match:
            user_input = user_input_match.group(1)
            vulnerable_elements.append((element, attribute, user_input))
    # If vulnerable elements were found, print a report and suggest solutions
    if vulnerable_elements:
        print(f"XSS vulnerabilities found on {url}")
        for element, attribute, user_input in vulnerable_elements:
            print(f"Vulnerable element: {element}")
            print(f"User input in {attribute}: {user_input}")
        print("Suggested solutions: Sanitize user input to remove any potentially malicious code, escape user input before using it in an HTML element, and use a Content Security Policy to restrict the sources from which scripts and other resources can be loaded.")
    else:
        print(f"No XSS vulnerabilities found on {url}")

def thread_link(response, url):
    t1 = threading.Thread(target=scan_sql, args=(response, url))
    t2 = threading.Thread(target=scan_xss, args=(response, url))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    url = input("Enter the URL to scan\n")
    resp = scan_url(url)
    thread_link(resp , url)