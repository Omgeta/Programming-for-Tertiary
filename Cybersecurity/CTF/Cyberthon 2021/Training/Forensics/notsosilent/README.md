# Not So Silent

## Description
Someone has been bruteforcing his/her way into our servers, can you please investigate? In particular, take a close look at any successful attempts.

## Analysis

We are given a pcapng file so let's boot up wireshark and see what we can do with it.

```txt
GET /storage/classified HTTP/1.1
Host: 192.168.0.150
Connection: close
Authorization: Basic YWRtaW46MTIzNDU2Nw==
User-Agent: Mozilla/4.0 (Hydra)

HTTP/1.1 401 Unauthorized
Server: nginx/1.14.0 (Ubuntu)
Date: Sun, 29 Mar 2020 17:40:47 GMT
Content-Type: text/html
Content-Length: 204
Connection: close
WWW-Authenticate: Basic realm="Restricted"

<html>
<head><title>401 Authorization Required</title></head>
<body bgcolor="white">
<center><h1>401 Authorization Required</h1></center>
<hr><center>nginx/1.14.0 (Ubuntu)</center>
</body>
</html>
```

Just looking through some random TCP streams, we can see what the author meant by bruteforcing. We basically have many, many, many TCP requests of the hacker trying to access the server with the authorization ``admin:password`` and the server denying him.

Let's try to find out which of his attempts succeeded in order to find the password.

## Solution

```txt
GET /storage/classified HTTP/1.1
Host: 192.168.0.150
Connection: close
Authorization: Basic YWRtaW46Y2F0aGVyaW5l
User-Agent: Mozilla/4.0 (Hydra)

HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Sun, 29 Mar 2020 17:40:52 GMT
Content-Type: application/octet-stream
Content-Length: 67
Last-Modified: Sun, 29 Mar 2020 17:02:18 GMT
Connection: close
ETag: "5e80d49a-43"
Accept-Ranges: bytes

This is not the flag. The flag format is CTFSG{<admins_password>}.
```

With a quick filter to look for HTTP 200 response, we can find the correct packet. Woohoo!

Now all we need to do is decode the authorization ``YWRtaW46Y2F0aGVyaW5l`` by base64 to obtain the flag below:
```txt
CTFSG{catherine}
```
