import requests

url = "http://3qo9k5hk5cprtqvnlkvotlnj9d14b7mt.ctf.sg:50301/flag"

payload="{\"secret\": \"I know how to make a POST request\"}"
headers = {
'Give-Flag': 'yes',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)