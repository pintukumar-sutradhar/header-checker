import requests

def check_http_headers(url):
    """
    Check the HTTP headers of a given URL and verify the presence of required headers.

    Args:
        url (str): The URL of the web application to check.

    Returns:
        None
    """
    try:
        # Normalize the URL
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        # Send a GET request to the URL to retrieve the page content
        response = requests.get(url)

        # Print the status code of the response
        print(f"Response Status Code: {response.status_code}\n")

        # Print the headers for the request and response
        print(f"Request Headers:")
        for header, value in response.request.headers.items():
            print(f"{header}: {value}")
        print(f"\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Define the set of required headers and check if they are present in the response
        required_headers = {
            "Content-Type", "Strict-Transport-Security", "X-Frame-Options",
            "X-XSS-Protection", "X-Content-Type-Options", "Referrer-Policy", "Content-Security-Policy",
            "Permissions-Policy"
        }
        missing_headers = [header for header in required_headers if header.lower() not in [h.lower() for h in response.headers]]

        # Print the list of missing headers or a message indicating that all headers are present
        if missing_headers:
            print(f"\nMissing Headers:")
            for header in missing_headers:
                print(f"- {header}")
        else:
            print(f"\nAll required headers are present.")

    except requests.RequestException as e:
        print(f"An error occurred while checking the headers: {e}")

# Prompt the user to enter the URL and call the function
url = input("Enter the URL of the web application to check: ")
print("\n--- Checking HTTP Headers ---\n")
check_http_headers(url)
