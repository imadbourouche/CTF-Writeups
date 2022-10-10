# eXORcist - CRYPTO (500 points)
1- Understand how the key is generated
```py
def generate_key(length):
    random_seed = os.urandom(16)
    key = random_seed * (length //16) + random_seed[:(length % 16)]
    return key
```
- key is The random seed multiplied ``length//16`` time and some of the rendom seed ``random_seed[:length%16]`` (length = the length of the message)
```
                      message(>20)
<----------------------------------------------------------->

                        key 
<|--------|--------|--------|--------|--------|--------|---->
  random                                                rest
   seed
```

2- Understand how the cipher is generated

```py
key = generate_key(len(message))
offset = random.randint(0, len(message))
cipher = xor(message[:offset]+FLAG+message[offset:], key)
```
- simple but the problem is in the offset, if the message length is little than we have high chance to get little offset, and we cannot get our key after
- the solution is to put a long message to have the chance of an offset >16 

3- solution
- we put a long message
- key = (message ⊕ cipher)[0:16]
- message+flag+message = (cipher ⊕ key)
- Script

```py
from pwn import *


def solution(cipher):
	c=bytes.fromhex(cipher).decode('utf-8')
	v="aaaaaaaaaaaaaaaa" #16
	key_bytes= [(ord(a) ^ ord(b)) for a,b in zip(c[:16], v)]
	key=""
	for i in key_bytes:
		key+=chr(i)
	
	print(xor(bytes.fromhex(cipher).decode('utf-8'),key))

p=b"a"*144
con=process(['./challenge/server.py'])
con.recv()
con.sendline(p)
ciher=str(con.recv())[4:len(s)-6] #the cipher
print(solution(ciher))
```
## Flag
``CyberErudites{Y0u_kn0w_h0w_T0_XOR}``