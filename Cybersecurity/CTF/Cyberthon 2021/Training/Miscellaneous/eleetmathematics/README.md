# eleetmathematics

## Description

```txt
This is an easy challenge, i'm going to just give you the flag... except that i'll encode it with different number systems! Hahaha!

Hint: the flag is in ascii, and there are 3 parts to the flag with 3 different encodings.

The submission format is: CTFSG{part1_part2_ part3}
```

## Analysis

Looking at the data below, it is clear that the three parts of the flag are being represented in different data formats; more specifically, different base-N number systems.

```txt
CTFSG{
0100110100110100010101000011001101001000010011010011010001010100001100010100001100110101
_
127061132064122104
_
47334e315535
}
```

We can guess that the first part is a binary number as each digit has range 0-1.

Similarly, we can observe from the second part that each digit has range 0-7, making it a possible octal number.

Lastly, the last part might be a hexadecimal number due to the presence of uncapitalized alphabet.

## Solution

Decode each digit into text to find the flag:

```txt
CTFSG{M4T3HM4T1C5_W1Z4RD_G3N1U5}
```