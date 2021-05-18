import requests

response = requests.get('https://gmcruz.me')
response.content # gives the HTML for the page
response.status_code  # gives the HTTP status code (200, 404, etc.)
print(response.status_code)
print(response.content)
print(type(response.content))
