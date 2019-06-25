import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Disregard insecure request warnings
from lxml import html

# Create a session
session_requests = requests.session()

# Required variables
login_url = 'https://www.codecademy.com/login'
authd_url = 'https://www.codecademy.com/learn'
name = 'xxxxxxxx'
password = 'xxxxxxxx'

# Get the auth token
result_auth_token = session_requests.get(login_url, verify=False)
tree = html.fromstring(result_auth_token.text)
authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

# Payload
payload = {
    'user[login]': name,
    'user[password]': password,
    'authenticity_token': authenticity_token
}

# Send login data to login_url
result = session_requests.post(
    login_url,
    data = payload,
    headers = dict(referer=login_url)
)
# Get data using authd_url after session has been authorized
result_authd = session_requests.get(
    authd_url,
    headers = dict(referer = authd_url)
)

# Search the authd_url contents for defined content (returns an array)
tree_authd = html.fromstring(result_authd.content)
badges = tree_authd.xpath("//div[@class='count__15egunoru_dNyrewQyvICt']/text()")[0]
print(badges)
