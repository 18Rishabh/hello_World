st=input("Enter string = ")
a=[]
b=[]
i=0
while i <len(st):
	if(st[i] not in a):
		a.append(st[i])
	i=i+1
print("Distinct characters :",a)
j=0
while j<len(a):
	c=a[j]
	i=0
	sum=0
	while(i<len(st)):
		if(c==st[i]):
			sum=sum+1
		i=i+1
	b.append(sum)
	j=j+1
print("Respective occurences :",b)



