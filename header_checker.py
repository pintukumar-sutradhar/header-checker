import requests

# Define the URL of the web application to check
url = input("Enter URL:")

# Send a GET request to the URL to retrieve the headers
response = requests.head(url)

# Get the headers from the response object
headers = response.headers

# Check the headers for security-related settings
security_headers = {
    'X-XSS-Protection': '1; mode=block',
    'X-Content-Type-Options': 'nosniff',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
    'Content-Security-Policy': "default-src 'self'",
    'X-Frame-Options': 'DENY',
}

missing_headers = []
for header, value in security_headers.items():
    if header not in headers:
        missing_headers.append(header)

if missing_headers:
    print(f"The following security headers are missing from {url}:")
    for header in missing_headers:
        print(f"- {header}")
else:
    print(f"All security headers are present on {url}.")

