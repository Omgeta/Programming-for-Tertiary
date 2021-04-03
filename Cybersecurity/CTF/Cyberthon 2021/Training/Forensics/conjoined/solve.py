with open("conjoined.gif", "rb") as f:
    data = f.read()

with open("seperated.jpg", "wb") as f:
    f.write(data[2173699:])