# corrupted

## Description
```txt
Can you recover this corrupted image?
```

## Analysis

The description makes it quite clear that we are actually looking at a corrupted image so let's now try to take a look at the underlying binary to figure out whats wrong.

```shell
$ head corrupted.jpg | hexdump -C
00000000  4b 45 4b 45 00 10 4a 46  49 46 00 01 01 00 00 48  |KEKE..JFIF.....H|
00000010  00 48 00 00 ff e1 00 8c  45 78 69 66 00 00 4d 4d  |.H......Exif..MM|
```

And... there's our problem.

If you didn't already see it, the [file header](https://en.wikipedia.org/wiki/List_of_file_signatures) for this jpg is wrong. 

JPG files are expected to start with a file header such that the first 4 bytes are ```ff d8 ff d0``` or ```ÿØÿà```.

## Solution

Now that we know what the problem is, we can just change the first 4 bytes to the correct data.

solve.py
```py
with open("./corrupted.jpg", "rb") as f:
    data = f.read()

with open("./uncorrupted.jpg", "wb") as f:
    f.write(b"\xff\xd8\xff\xd0"+data[4:])
```

Bam! We have our fixed image.
![Fixed Image](./uncorrupted.jpg)
```txt
CTFSG{HUDSON_YARDZ}
```