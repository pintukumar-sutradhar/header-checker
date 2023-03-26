import requests

# Define the URL of the web application to check
url = input("Enter URL: ")
if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url

# Send a GET request to the URL to retrieve the page content
response = requests.get(url)

# Print the status code of the response
print(f"Status Code: {response.status_code}\n")

# Print the headers for the request and response
print(f"Request Headers:")
for header, value in response.request.headers.items():
    print(f"{header}: {value}")
print(f"\nResponse Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")

# Define the list of required headers and check if they are present in the response
required_headers = ["Content-Type", "User-Agent", "Strict-Transport-Security", "X-Frame-Options",
                    "X-XSS-Protection", "X-Content-Type-Options", "Referrer-Policy", "Content-Security-Policy",
                    "Permissions-Policy"]
missing_headers = []
for header in required_headers:
    if header not in response.headers:
        missing_headers.append(header)

# Print the list of missing headers or a message indicating that all headers are present
if missing_headers:
    print(f"\nMissing Headers:")
    for header in missing_headers:
        print(header)
else:
    print(f"\nAll required headers are present.")
    
