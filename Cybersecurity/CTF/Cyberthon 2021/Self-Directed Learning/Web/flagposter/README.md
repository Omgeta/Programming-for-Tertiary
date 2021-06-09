# Terrible Sequel

# Description
Free flag for you over here! Just make sure you request for it via post yeah?

Concept(s) Required:
- HTTP POST
- HTTP Headers

## Analysis

All we need to do is to clear the first two conditions in order to return a successful response

```py
if not give_flag_header or give_flag_header != 'yes':
    return FAIL

if not flag_request or flag_request.secret != SECRET:
    return FAIL

return SUCCESS
```

## Solution

All we need to do is send a POST request to the server with the required header and body

solve.py
```py
import requests

url = "http://3qo9k5hk5cprtqvnlkvotlnj9d14b7mt.ctf.sg:50301/flag"

payload="{\"secret\": \"I know how to make a POST request\"}"
headers = {
'Give-Flag': 'yes',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```


The flag found is:
```txt
CTFSG{53r14l_fl4g_p05t3r_g1v35_fr33_fl4g5}
```