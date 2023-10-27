from pwn import *

r = remote("chals.tuctf.com", 30202)
i = 0
while(1):
    try:
        i+=1
        print("prob "+str(i)+": ")
        raw = str(r.recvline())[2:-3]
        print(raw)
        func = eval(raw)
        print(func)
        r.recvuntil(" ")
        r.sendline(str(func))
        r.recvline()

    except SyntaxError:
        continue

r.interactive()