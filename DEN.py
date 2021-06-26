un = input("Enter the username in lowercase....")
sum = []
for i in range(0,len(un)):
	if(un[i]=='a' or un[i]=='b' or un[i]=='c'):
    		sum.append(2)
	elif(un[i]=='d' or un[i]=='e' or un[i]=='f'):
    		sum.append(3)
	elif(un[i]=='g' or un[i]=='h' or un[i]=='i'):
    		sum.append(4)
	elif(un[i]=='j' or un[i]=='k' or un[i]=='l'):
	        sum.append(5)
	elif(un[i]=='m' or un[i]=='n' or un[i]=='o'):
	        sum.append(6)
	elif(un[i]=='p' or un[i]=='q' or un[i]=='r' or un[i]=='s'):
                sum.append(7) 
	elif(un[i]=='t' or un[i]=='u' or un[i]=='v'):
    		sum.append(8)
	elif(un[i]=='w' or un[i]=='x' or un[i]=='y' or un[i]=='z'):
    		sum.append(9)
	else:
    		print("invalid name")
print("your dialpad code is...",sum)
