import requests

auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'
email = 'tim@plymouth.ac.uk'
password = 'COMP2001!'

credentials = {
    'email' : email,
    'password' : password
}

response = requests.post(auth_url, json=credentials)

if response.status_code == 200:
        try:
            json_response = response.json()
            print("Authenticated successfully:", json_response)
            print(json_response[1])
            if json_response[1] == 'True':
                print("Log in success")
            else:
                print (" Log in failed")
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
else:
    print(f"Authentication failed with status code {response.status_code} ")
    print("Response content:", response.text)