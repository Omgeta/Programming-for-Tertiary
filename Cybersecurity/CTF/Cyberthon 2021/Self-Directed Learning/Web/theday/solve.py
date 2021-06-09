import requests

cookies = {
    '__cfduid': 'd8842845d46c2c9d151393c6362f8bd291618227131',
    'unix_time': '71727221532000',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-GPC': '1',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': '"605e435d-abe"',
    'If-Modified-Since': 'Fri, 26 Mar 2021 20:26:05 GMT',
}

response = requests.get('http://3qo9k5hk5cprtqvnlkvotlnj9d14b7mt.ctf.sg:50501/', headers=headers, cookies=cookies, verify=False)

print(response.content)