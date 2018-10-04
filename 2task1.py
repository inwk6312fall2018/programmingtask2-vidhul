def crime_list():
file=open('Crime.csv')
	l1=[]	
	l2=[]
	d1={}	

	for line in file:
		line.strip()
		for lines in line.split(','):
			l1.append(lines)
	for i in l1: 
		if(i not in d1): 
			d1[i]=1      
		else:
			d1[i]=d1[i]+1   


l3=list(d1.keys())
	for i in range(len(l1)):
		if l1[i] in l3:
		d1[l1[i]]=l1[i+1].strip()
	print ("{:<12} {:<29}".format('k','v')) 
	for k,v in d1.items():   # making a table format
		crime_type=k
		crime_count=v
		print("{:<12} {:<19}".format(crime_type, crime_count))

file_name="Crime.csv"
crime_list(file_name)