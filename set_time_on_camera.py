import requests
from requests.auth import HTTPDigestAuth
from datetime import datetime

# Credentials for HTTP Digest Authentication
username = 'admin'
password = 'your_password_here'
auth = HTTPDigestAuth(username, password)

# Get the system's current time and format it as 'YYYY-MM-DD HH:MM:SS'
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Encode the time for the URL (replace spaces with %20)
formatted_time = current_time.replace(' ', '%20')

# Build the request URL with the formatted time : CHANGE IP ADDRESS HERE!
url = f'http://192.168.254.85/cgi-bin/global.cgi?action=setCurrentTime&time={formatted_time}'

# Send the GET request
r = requests.get(url, auth=auth)

# Print the response for verification
print(f"Request URL: {url}")
print(f"Response Code: {r.status_code}")
print(f"Response Body: {r.text}")
