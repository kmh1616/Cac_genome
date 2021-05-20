# coding: utf-8
import re
st = ""
bool = 0
num = 1
st2 = ""
tmptmp = 0
tmptmp1 = 0
listtmp = []
itmp = 0
st11 = st22 = ""
with open ("Lachesis_order.gff") as f:
	for line1 in f:
			list1 = line1.split()
			with open ("GT_final.gff3") as f2:
				for line2 in f2:
					if 'scaffold'not in line2:
						continue
########带+的contig,是从该位置往后延伸的
					if "ERR" in line1:
						matchObj = re.match( r'(.*)_(.*)POS(\d+)', list1[1], re.M|re.I)
						st11 = matchObj.group(1)
						st22 = matchObj.group(3)
					if "+" in line1 and (st11 in line2):
						tmp1 = int(st22)
						tmp2 = int(list1[3])-int(list1[2])
						list2 = line2.split()
						list2[0]=list1[0]
				#####处理负链					
						if list1[4] != '0':#判断这条contig是不是正链
							if list2[6]=='+':
								list2[6] ="-"
								if	int(list2[3]) >= int(tmp1) and int(list2[4]) <= int(tmp2)+int(tmp1):
									tmp3 = tmp2 - int(list2[4]) + int(tmp1) #起始
									tmp4 = tmp2 - int(list2[3]) + int(tmp1)#起始终止对调
									list2[3]=int(tmp3)  + int(list1[2]) + 1
									list2[4]=int(tmp4)  + int(list1[2]) + 1
									list2[3]=str(list2[3])
									list2[4]=str(list2[4])
									st += '	'.join(list2) + "\n"
									continue
							elif  (int(list2[3])<=int(tmp1) and int(list2[4])>= int(tmp1)) or (int(list2[3])<=int(tmp1) + int(tmp2) and int(list2[4])>= int(tmp1)+int(tmp2) ):
								st2 += ' '.join(list2) + "\n"  #回收断的基因
								continue
							else:
								list2[6]="+"
							if	int(list2[3]) >= int(tmp1) and int(list2[4]) <= int(tmp2) +int(tmp1):
								tmp3 = tmp2 - int(list2[4]) + int(tmp1) #起始
								tmp4 = tmp2 - int(list2[3]) + int(tmp1)#起始终止对调
								list2[3]=tmp3 + int(list1[2]) +1
								list2[4]=tmp4 + int(list1[2]) +1
								list2[3]=str(list2[3])
								list2[4]=str(list2[4])
								st += '	'.join(list2) + "\n"
								continue
							elif  (int(list2[3])<=int(tmp1) and int(list2[4])>= int(tmp1)) or (int(list2[3])<=int(tmp1) + int(tmp2) and int(list2[4])>= int(tmp1)+int(tmp2) ):
								st2 += ' '.join(list2) + "\n"  #回收断的基因
								continue
		##############			
				########处理正链						
						if	int(list2[3]) >= int(tmp1) and int(list2[4]) <= int(tmp2) + int(tmp1):
								list2[3]=int(list2[3])+int(list1[2])-int(tmp1) -1
								list2[4]=int(list2[4])+int(list1[2])-int(tmp1) -1
								list2[3]=str(list2[3])
								list2[4]=str(list2[4])
								list2[0]=list1[0]
								st += '	'.join(list2) + "\n"
								continue
						elif  (int(list2[3])<=int(tmp1) and int(list2[4])>= int(tmp1)) or (int(list2[3])<=int(tmp1) + int(tmp2) and int(list2[4])>= int(tmp1)+int(tmp2) ):
							st2 += ' '.join(list2) + "\n"  #回收断的基因
							continue
								
								
								
								
		#############打断的contig
					if (st11 in line2 and "ERROPOS" in line1) and ('+' not in line1): 
						
						tmp1 = int(st22)
						tmp2 = int(list1[3])-int(list1[2])
						list2 = line2.split()
						list2[0]=list1[0]
				#######处理负链					
						if list1[4] != '0':#判断这条contig是不是正链
							if list2[6]=='+':
								list2[6] ="-"
								if	int(list2[3]) >= int(tmp1) -int(tmp2) and int(list2[4]) <= int(tmp1):
									tmp3 = tmp1 - int(list2[4]) #起始
									tmp4 = tmp1 - int(list2[3])#起始终止对调
									list2[3]=int(tmp3)  + int(list1[2]) 
									list2[4]=int(tmp4)  + int(list1[2]) 
									list2[3]=str(list2[3])
									list2[4]=str(list2[4])
									st += '	'.join(list2) + "\n"
									continue
							elif  (int(list2[3])<=int(tmp1) and int(list2[4])>= int(tmp1)):
								st2 += ' '.join(list2) + "\n"  #回收断的基因
								continue
							else:
								list2[6]="+"
							if	int(list2[3]) >= int(tmp1) -int(tmp2) and int(list2[4]) <= int(tmp1):
								tmp3 = tmp1 - int(list2[4])  #起始
								tmp4 = tmp1 - int(list2[3]) #起始终止对调
								list2[3]=tmp3 + int(list1[2]) 
								list2[4]=tmp4 + int(list1[2]) 
								list2[3]=str(list2[3])
								list2[4]=str(list2[4])
								st += '	'.join(list2) + "\n"
								continue
							elif  (int(list2[3])<=int(tmp1) and int(list2[4])>= int(tmp1)) :
								st2 += ' '.join(list2) + "\n"  #回收断的基因
								continue
		############			
				#######处理正链						
						if	int(list2[3]) >= int(tmp1) - int(tmp2) and int(list2[4]) <= int(tmp1):
							list2[3]=int(list2[3])+int(list1[2])-int(tmp1)+int(tmp2)
							list2[4]=int(list2[4])+int(list1[2])-int(tmp1)+int(tmp2)
							list2[3]=str(list2[3])
							list2[4]=str(list2[4])
							list2[0]=list1[0]
							st += '	'.join(list2) + "\n"
						elif  (int(list2[3])<=int(tmp1) and int(list2[4])>= int(tmp1)) or (int(list2[3])<=int(tmp1) - int(tmp2) and int(list2[4])>= int(tmp1)- int(tmp2) ):
								st2 += ' '.join(list2) + "\n"  #回收断的基因
								continue
		
	###########未打断的contig
					if list1[1] in line2 and "ERROPOS" not in line2: #判断contig是不是在这条染色体中
	#判断这条链是不是正链

						list2 = line2.split()
						list2[0]=list1[0]
	#负链					
						if list1[4] != '0':
							if list2[6]=='+':
								list2[6] ="-"
								tmp3 = int(list1[3])-int(list1[2]) - int(list2[4]) #起始
								tmp4 = int(list1[3])-int(list1[2]) - int(list2[3]) #起始终止对调
								list2[3]=tmp3+int(list1[2]) + 1
								list2[4]=tmp4+int(list1[2]) + 1
								list2[3]=str(list2[3])
								list2[4]=str(list2[4])
								st += '	'.join(list2) + "\n"
								continue				
							else:
								list2[6]="+"
								tmp3 = int(list1[3])-int(list1[2]) - int(list2[4]) #起始
								tmp4 = int(list1[3])-int(list1[2]) - int(list2[3]) #起始终止对调
								list2[3]=tmp3+int(list1[2]) + 1
								list2[4]=tmp4+int(list1[2]) + 1
								list2[3]=str(list2[3])
								list2[4]=str(list2[4])
								st += '	'.join(list2) + "\n"
								continue							

						
	#正链
						list2[3]=int(list2[3])+int(list1[2]) -1
						list2[4]=int(list2[4])+int(list1[2]) -1
						list2[3]=str(list2[3])
						list2[4]=str(list2[4])
						st += '	'.join(list2) + "\n"	

			num +=1
					
outtxt = open("result_v5","w")
outtxt.write(st)
outtxt.close()

outtxt = open("result_cutgene_v5","w")
outtxt.write(st2)
outtxt.close()
