# cybersleuth

## Description
```txt
Okay this is weird, I can't seem to open this word document. Hang on... is it even a word document?
```

## Analysis

The challenge description is hinting to us that the file may actually be of a different file type than the one we are presented with so let's try to find out the truth. 

```shell
$ file flag.docx
flag.docx: ASCII text
```

Oh cool! It's just a normal text file.

## Solution

Just read the contents of the file to get the flag: 

```shell
$ cat flag.docx
CTFSG{F1l3_typ3_D3T3cT0R}
```