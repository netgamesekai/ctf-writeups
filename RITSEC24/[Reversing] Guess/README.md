# RITSEC24

## [Reversing] Guess

## Approach

An APK file `guess.apk` is provided. Running the app does not result in any visible GUI interactions. After decompiling the app (e.g. using jadx), it can be observed that the `flag` function in the `MainActivity` class performs several Base64-related operations.

The standard approach would be to run the APK, attach a debugger, and extract the return value of the flag directly from memory. However, rather than investing time in setting up the debugging environment on my laptop, I'd like to quickly translate the decompiled code into Python and obtain the return value of the flag function.

## Exploit Code

```python
import base64
evilstring = "cmpkdjNjYzE6MzUuU1R8aHY0dHR6YGd2b2R1MnBvfi46MTI0M3M6amcz"
fornameN = base64.b64decode(evilstring.encode('UTF-8')).decode('UTF-8')
undecryptedencryptedString = "SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw=="
recursiveCharArray = ""
finalrray = list(undecryptedencryptedString)

kentucky = 0
xortrad = len(finalrray)-1
while (kentucky < xortrad):
    glaf = finalrray[kentucky]
    finalrray[kentucky] = finalrray[xortrad]
    finalrray[xortrad] = glaf

    kentucky += 1
    xortrad -= 1
print(finalrray)

recursiveCharArray = ""
everyOther = 0
while (everyOther < len(fornameN)):
    decryptedChar = ord(fornameN[everyOther])-1
    recursiveCharArray += chr(decryptedChar)
    everyOther += 1

for c in finalrray:
    undecryptedencryptedString = "SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==".encode() + \
        c.encode()

print("SGF2ZSB5b3UgZXZlciB1c2VkIEZyaWRhPw==" +
      recursiveCharArray + undecryptedencryptedString.decode())

```
