import requests
import sys

# Get username and password from arguments
username = sys.argv[1]
password = sys.argv[2]
new_password = sys.argv[3]

# Send first request to get cookies
r = requests.get('https://www.instagram.com/')
csrf_token = r.cookies['csrftoken']

# Then login using above cookies
print("LOGIN .............")
r = requests.post('https://www.instagram.com/accounts/login/ajax/', data={'username': username, 'password': password},
                  headers={
                      'origin': 'https://www.instagram.com',
                      'referer': 'https://www.instagram.com/',
                      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
                      'x-csrftoken': csrf_token,
                      'x-instagram-ajax': 1,
                      'x-requested-with': 'XMLHttpRequest'
                  }, cookies=r.cookies)

# You can check HTTP status code or response (json) from here, authenticated=true mean success
if r.status_code == 200 and r.json()['authenticated']:
    print("OK, authenticated.")
else:
    raise Exception("Login failure with username/password: %s/%s\nResponse: %s" % (username, password, r.text))

# Get new CSRF token from login response to change password
print("CHANGE PASSWORD .............")
csrf_token = r.cookies['csrftoken']
r = requests.post('https://www.instagram.com/accounts/password/change/',
                  data={'old_password': password, 'new_password1': new_password, 'new_password2': new_password},
                  headers={
                      'origin': 'https://www.instagram.com',
                      'referer': 'https://www.instagram.com/accounts/password/change/?wo=1',
                      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
                      'x-csrftoken': csrf_token,
                      'x-instagram-ajax': 1,
                      'x-requested-with': 'XMLHttpRequest'
                  }, cookies=r.cookies)

if r.status_code == 200 and r.json()['status'] == "ok":
    print("OK, password changed.")
else:
    raise Exception("Change password fail: %s" % r.text)
