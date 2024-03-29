# Java Very Mocha

# Description
```txt
Can you reverse engineer this Java program?

Hint: You can decompile it, not all decompilers are equal.
```

# Analysis

If the description wasn't clear enough, we just need to decompile this class file to get the Java source code for analysis. I'm too lazy to download a program to decompile so I will just be using [this website](https://www.decompiler.com) instead.

Cleaned up Java code
```java
import java.util.Scanner;

public class JavaVeryMocha {
   public static void main(String[] args) {
      int[] data = new int[]{116, 104, 105, 115, 32, 105, 115, 32, 110, 111, 116, 32, 116, 104, 101, 32, 102, 108, 97, 103};
      System.out.print("[+] Enter Passphrase => ");
      Scanner scanner = new Scanner(System.in);
      String input = scanner.nextLine();
      if (input.length() == data.length) {
         int i = 0;

         for(int j = data.length - 1; j >= 0; --j) {
            if (input.charAt(i++) != (char)data[j] + 1) {
               System.exit(0);
            }
         }

         System.out.print("The flag is CTFSG{" + input + "}");
      }

   }
}
```

Pythonized version for my fellow Java haters
```py
import sys

data = [116, 104, 105, 115, 32, 105, 115, 32, 110, 111, 116, 32, 116, 104, 101, 32, 102, 108, 97, 103]

inp = input("[+] Enter Passphrase => ")
if len(inp) == len(data):
   for inpchar, dataord in zip(inp, reversed(data)):
      if inpchar != chr(dataord + 1):
         sys.exit(0)
   
   print("The flag is CTFSG{" + inp + "}")
   
```

From this, we can infer that the password (as well as the flag) are just the reversed ``data`` array with 1 added to each digit, converted to ASCII.

# Solution

All we need to do is to obtain the password by reversing the int array and convert it to a string.

```py
data = [116, 104, 105, 115, 32, 105, 115, 32, 110, 111, 116, 32, 116, 104, 101, 32, 102, 108, 97, 103]

flag = ""
for x in reversed(data):
    flag += char(x+1)
print("CTFSG{"+ res + "}")
```

And out we get the flag that looks nothing like a flag. Hooray.

```txt
CTFSG{hbmg!fiu!upo!tj!tjiu}
```