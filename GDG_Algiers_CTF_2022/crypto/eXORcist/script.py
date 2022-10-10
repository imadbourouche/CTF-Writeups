from pwn import *


def solution(cipher):
	v1=bytes.fromhex(cipher).decode('utf-8')[:16]
	v2="aaaaaaaaaaaaaaaa" #16
	key_bytes= [(ord(a) ^ ord(b)) for a,b in zip(v1, v2)]
	key=""
	for i in key_bytes:
		key+=chr(i)
	
	print(xor(bytes.fromhex(cipher).decode('utf-8'),key))

p=b"a"*800
con=process(['./challenge/server.py'])
con.recv()
con.sendline(p)
s=str(con.recv())
print(solution(s[4:len(s)-6]))