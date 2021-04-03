with open("./corrupted.jpg", "rb") as f:
    data = f.read()

with open("./uncorrupted.jpg", "wb") as f:
    f.write(b"\xff\xd8\xff\xd0"+data[4:])