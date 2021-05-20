file = "Cac.gff"
dict = {}
chrlist = []
lines = open(file,"r")
# -------------------------------------------------------------------------------
for line in lines:
	cc = line.split()
	dict[cc[1]] = cc[0] + "\t" + cc[2] + "\t" + cc[3]
	chrlist.append(cc[1])
lines.close()
# -------------------------------------------------------------------------------
tfile = "similarSequences.txt"
lines = open(tfile,"r") 
outtxt= open("out.txt","w")
dlist = []
for line in lines:
	cc = line.split()
	if cc[2] == "Cac" and cc[3] == "Cac" and cc[0] != cc[1]:
		if float(cc[-2]) >= 50 and float(cc[-1]) >= 70:
			aaa = dict[cc[0]]
			bbb = dict[cc[1]]
			if aaa.split()[0] == bbb.split()[0]:
				alist = []
				alist.append(int(aaa.split()[1]))
				alist.append(int(aaa.split()[2]))
				alist.append(int(bbb.split()[1]))
				alist.append(int(bbb.split()[2]))
				alist = sorted(alist)
				ccc = abs(chrlist.index(cc[0])-chrlist.index(cc[1])-1)
				if alist[2] - alist[1] <= 100000 and ccc < 10:
					blist = sorted([cc[0],cc[1]])
					if blist not in dlist:
						dlist.append(blist)
						outtxt.write(("\t").join(blist) + "\n")
lines.close()
outtxt.close()
# -------------------------------------------------------------------------------
lines = open("out.txt","r")
outtxt = open("out2.txt","w")
klist = []
for line in lines:
	cc = line.split()
	if cc[0] not in klist and cc[1] not in klist:
		if len(klist) > 0:
			klist = sorted(klist)
			outtxt.write(("\t").join(klist)	+ "\n")
		klist = []
		klist.append(cc[0])
		klist.append(cc[1])
	else:
		if cc[0] not in klist:
			klist.append(cc[0])
		if cc[1] not in klist:
			klist.append(cc[1])
lines.close()
outtxt.write(("\t").join(klist) + "\n")
outtxt.close()

	
		
		
