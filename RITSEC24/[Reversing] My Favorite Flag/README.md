# RITSEC24

## [Reversing] [Warm Up] My Favorite Flag

## Approach

Two files are given, an executable file `a.out` and the original code: `checker.c`.
The executable file takes user input, performs XOR between the input and a given string, and then compares the result to another string to check whether the input is right or wrong while hiding the original flag.
<br/>

The XOR operation is carried out as follows:

```c
  for (i = 0; i < l; i++) {
    output[(2*i) % l] = input[i] ^ b[i];
  }
```

Thanks to the properties of XOR, the value of `output[(2*i) % l] ^ b[i]` is equal to `input[i]`, so the original flag can be recovered.

## Exploit Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char b[] = {0x0, 0x28, 0x13, 0x36, 0x11, 0x7a, 0x6e, 0x4, 0x6c, 0x55, 0x5f, 0x39, 0x4, 0x1d, 0x4e, 0x66, 0x6f, 0x6b, 0x42, 0x49, 0x0, 0x52, 0x0, 0x53, 0x1f, 0x0, 0x56, 0x4e, 0x5c};
    char *s = "RS{0h_b0y,I_10v3_f4k3_fl4gs!}";
    int l = strlen(s);
    int flag[30];

    for (int i = 0; i < l; i++) {
        int tmp = l - 1 - i;
        flag[tmp] = s[(2 * tmp) % l] ^ b[tmp];
    }

    for (int i = 0; i < l; i++) {
        printf("%c", flag[i]);
    }
    printf("\n");

    return 0;
}
```
