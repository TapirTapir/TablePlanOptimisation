import csv
import sys 
import random
import re

from SeatingPlanFunction import generate_score
from SeatingPlanFunction import find_swap

f = open("Desktop/Guest_list_test.csv", 'rb')
reader=csv.reader(f, delimiter="\t")

Category=list()
Adult=list()
Name=list()
Staying=list()
Diet=list()
Family=list()

for row in reader:
	Category.append(row[0])
	Adult.append(row[1])
	Name.append(row[2])
	Staying.append(row[3])
	Diet.append(row[4])
	Family.append(row[5])

#Test for duplicates in the list of names
x=0
for testduplicate in Name:
	y=0
	for j in Name:
		if testduplicate==j and x<>y:
			print(j+"   "+testduplicate+" are duplicates! This willbreak things")
		y=y+1
	x=x+1

TopTable=list()
Spriga = dict()
Sprigb = dict()

compatibilitymatrix=dict()

for name in Name:
	compatibilitymatrix[name]=list()
	for name1 in Name:
		x=Name.index(name)
		y=Name.index(name1)
		Person1Cat = Category[x]
		Person2Cat = Category[y]
		Person1Fam = Family[x]
		Person2Fam = Family[y]
		if name1==name:
			compatibilitymatrix[name].append("1000")
		elif Person1Cat==Person2Cat and Person1Fam!=Person2Fam:
			compatibilitymatrix[name].append("10")
		elif Person1Fam==Person2Fam:
			compatibilitymatrix[name].append("50")
		else:	
			compatibilitymatrix[name].append("0")



for i in range(0,27):
	TopTable.append("X")

for i in range(0,9):
	Spriga[i]={}
	Sprigb[i]={}
	for j in range(0,9):
		Spriga[i][j]="X"
		Sprigb[i][j]="X"

for name in Name:
	FoundPlace= False
	while FoundPlace==False:
		TestPlace = random.randint(1,188)
		if TestPlace < 27:
			if TopTable[TestPlace]=="X":	
				TopTable[TestPlace] = name
				FoundPlace= True
		if TestPlace > 27:
			SprigNum = round((TestPlace-27)/18)
			TableSide=(TestPlace-27)%18
			if TableSide<9:
				 side="a" 
			else: 
				side="b"
			if side=="a":
				if Spriga[SprigNum][TableSide]=="X":
					Spriga[SprigNum][TableSide]=name
					FoundPlace= True
			if side=="b":
				if Sprigb[SprigNum][TableSide-9]=="X":
					Sprigb[SprigNum][TableSide-9]=name
					FoundPlace= True

f = open("comp_matrix.csv", 'rb')
reader1=csv.reader(f, delimiter="\t")

rownum=0
compatibility=dict()
for row in reader1:
	if rownum == 0:
		comp_names=row
	else:
		compatibility[rownum]=row
	rownum+=1



#For rereading in compatibility matrix
for name1 in Name:
	countname=0
	for name2 in Name:
		rownum=1
		for read_name1 in comp_names:
			colnum=0
			for read_name2 in comp_names:
				if name1==read_name1 and name2==read_name2:
					if compatibility[rownum][colnum]<>"":
						compatibilitymatrix[name1][countname]=compatibility[rownum][colnum]				
				colnum+=1
			rownum+=1
		countname+=1




for i in range(1, 25):
	firstname_x=random.randint(0,len(Name)-1)
	firstname_y=random.randint(0,len(Name)-1)
	while firstname_x==firstname_y:
		firstname_y=random.randint(0, len(Name)-1)
	score = raw_input('How will '+Name[firstname_x]+' and '+Name[firstname_y]+' get along? Existing score is: '+compatibilitymatrix[Name[firstname_x]][firstname_y]+' Enter score: ')
	compatibilitymatrix[Name[firstname_x]][firstname_y]=score
	compatibilitymatrix[Name[firstname_y]][firstname_x]=score

keys=sorted(compatibilitymatrix.keys())
with open("comp_matrix.csv", "wb") as outfile:
	writer=csv.writer(outfile, delimiter="\t")
	writer.writerow(keys)
	writer.writerows(zip(*[compatibilitymatrix[key] for key in keys]))


Best_score=0

parent_a_score = generate_score(TopTable, Spriga, Sprigb, Name, compatibilitymatrix)


#print TopTable
print parent_a_score			

for Swaps in range(1,500):
	
#	print("Swaps = "+str(Swaps))
	
	parent_a_score = generate_score(TopTable, Spriga, Sprigb, Name, compatibilitymatrix)
#	print "parent a"
#	print parent_a_score
	Swap_a=find_swap(TopTable, Spriga, Sprigb)
	Swap_b=find_swap(TopTable, Spriga, Sprigb)

#	print Swap_a, Swap_b

	if Swap_a["table"]=="TT":
#		print "top table"
#		print TopTable
		TopTable[Swap_a["place"]]=Swap_b["name"]
#		print TopTable
	elif Swap_a["tableside"]=="a":
#		print Swap_a["table"]
#		print Spriga[Swap_a["table"]]
		Spriga[Swap_a["table"]][Swap_a["place"]]=Swap_b["name"]
#		print Spriga[Swap_a["table"]]
	elif Swap_a["tableside"]=="b":
#		print Swap_a["table"]
#		print Sprigb[Swap_a["table"]]
		Sprigb[Swap_a["table"]][Swap_a["place"]-9]=Swap_b["name"]
#		print Sprigb[Swap_a["table"]]	
	if Swap_b["table"]=="TT":
#		print "top table"
#		print TopTable
		TopTable[Swap_b["place"]]=Swap_a["name"]
#		print TopTable
	elif Swap_b["tableside"]=="a":
#		print Swap_b["table"]
#		print Spriga[Swap_b["table"]]
		Spriga[Swap_b["table"]][Swap_b["place"]]=Swap_a["name"]
#		print Spriga[Swap_b["table"]]
	elif Swap_b["tableside"]=="b":
#		print Swap_b["table"]
#		print Sprigb[Swap_b["table"]]
		Sprigb[Swap_b["table"]][Swap_b["place"]-9]=Swap_a["name"]
#		print Sprigb[Swap_b["table"]]
	
	parent_b_score = generate_score(TopTable, Spriga, Sprigb, Name, compatibilitymatrix)
#	print "parent b"
#	print parent_b_score

	if parent_a_score>parent_b_score:
		if Swap_a["table"]=="TT":
#			print "top table"
#			print TopTable
			TopTable[Swap_a["place"]]=Swap_a["name"]
#			print TopTable
		elif Swap_a["tableside"]=="a":
#			print Swap_a["table"]
#			print Spriga[Swap_a["table"]]
			Spriga[Swap_a["table"]][Swap_a["place"]]=Swap_a["name"]
#			print Spriga[Swap_a["table"]]
		elif Swap_a["tableside"]=="b":
#			print Swap_a["table"]
#			print Sprigb[Swap_a["table"]]
			Sprigb[Swap_a["table"]][Swap_a["place"]-9]=Swap_a["name"]
#			print Sprigb[Swap_a["table"]]
		if Swap_b["table"]=="TT":
#			print "top table"
#			print TopTable
			TopTable[Swap_b["place"]]=Swap_b["name"]
#			print TopTable
		elif Swap_b["tableside"]=="a":
#			print Swap_b["table"]
#			print Spriga[Swap_b["table"]]
			Spriga[Swap_b["table"]][Swap_b["place"]]=Swap_b["name"]
#			print Spriga[Swap_b["table"]]
		elif Swap_b["tableside"]=="b":
#			print Swap_b["table"]
#			print Sprigb[Swap_b["table"]]
			Sprigb[Swap_b["table"]][Swap_b["place"]-9]=Swap_b["name"]
#			print Sprigb[Swap_b["table"]]

parent_a_score = generate_score(TopTable, Spriga, Sprigb, Name, compatibilitymatrix)
print "Final score = "
print parent_a_score

print(" "+TopTable[0]+" "+Spriga[0][0]+" "+Spriga[0][1]+" "+Spriga[0][2]+" "+Spriga[0][3]+" "+Spriga[0][4]+" "+Spriga[0][5]+" "+Spriga[0][6]+" "+Spriga[0][7]+" "+Spriga[0][8]+" \n")
print(" "+TopTable[1]+" "+Sprigb[0][0]+" "+Sprigb[0][1]+" "+Sprigb[0][2]+" "+Sprigb[0][3]+" "+Sprigb[0][4]+" "+Sprigb[0][5]+" "+Sprigb[0][6]+" "+Sprigb[0][7]+" "+Sprigb[0][8]+" \n")
print(" "+TopTable[2]+" \n")
print(" "+TopTable[3]+" "+Spriga[1][0]+" "+Spriga[1][1]+" "+Spriga[1][2]+" "+Spriga[1][3]+" "+Spriga[1][4]+" "+Spriga[1][5]+" "+Spriga[1][6]+" "+Spriga[1][7]+" "+Spriga[1][8]+" \n")
print(" "+TopTable[4]+" "+Sprigb[1][0]+" "+Sprigb[1][1]+" "+Sprigb[1][2]+" "+Sprigb[1][3]+" "+Sprigb[1][4]+" "+Sprigb[1][5]+" "+Sprigb[1][6]+" "+Sprigb[1][7]+" "+Sprigb[1][8]+" \n")
print(" "+TopTable[5]+" \n")
print(" "+TopTable[6]+" "+Spriga[2][0]+" "+Spriga[2][1]+" "+Spriga[2][2]+" "+Spriga[2][3]+" "+Spriga[2][4]+" "+Spriga[2][5]+" "+Spriga[2][6]+" "+Spriga[2][7]+" "+Spriga[2][8]+" \n")
print(" "+TopTable[7]+" "+Sprigb[2][0]+" "+Sprigb[2][1]+" "+Sprigb[2][2]+" "+Sprigb[2][3]+" "+Sprigb[2][4]+" "+Sprigb[2][5]+" "+Sprigb[2][6]+" "+Sprigb[2][7]+" "+Sprigb[2][8]+" \n")
print(" "+TopTable[8]+" \n")
print(" "+TopTable[9]+" "+Spriga[3][0]+" "+Spriga[3][1]+" "+Spriga[3][2]+" "+Spriga[3][3]+" "+Spriga[3][4]+" "+Spriga[3][5]+" "+Spriga[3][6]+" "+Spriga[3][7]+" "+Spriga[3][8]+" \n")
print(" "+TopTable[10]+" "+Sprigb[3][0]+" "+Sprigb[3][1]+" "+Sprigb[3][2]+" "+Sprigb[3][3]+" "+Sprigb[3][4]+" "+Sprigb[3][5]+" "+Sprigb[3][6]+" "+Sprigb[3][7]+" "+Sprigb[3][8]+" \n")
print(" "+TopTable[11]+" \n")
print(" "+TopTable[12]+" "+Spriga[4][0]+" "+Spriga[4][1]+" "+Spriga[4][2]+" "+Spriga[4][3]+" "+Spriga[4][4]+" "+Spriga[4][5]+" "+Spriga[4][6]+" "+Spriga[4][7]+" "+Spriga[4][8]+" \n")
print(" "+TopTable[13]+" "+Sprigb[4][0]+" "+Sprigb[4][1]+" "+Sprigb[4][2]+" "+Sprigb[4][3]+" "+Sprigb[4][4]+" "+Sprigb[4][5]+" "+Sprigb[4][6]+" "+Sprigb[4][7]+" "+Sprigb[4][8]+" \n")
print(" "+TopTable[14]+" \n")
print(" "+TopTable[15]+" "+Spriga[5][0]+" "+Spriga[5][1]+" "+Spriga[5][2]+" "+Spriga[5][3]+" "+Spriga[5][4]+" "+Spriga[5][5]+" "+Spriga[5][6]+" "+Spriga[5][7]+" "+Spriga[5][8]+" \n")
print(" "+TopTable[16]+" "+Sprigb[5][0]+" "+Sprigb[5][1]+" "+Sprigb[5][2]+" "+Sprigb[5][3]+" "+Sprigb[5][4]+" "+Sprigb[5][5]+" "+Sprigb[5][6]+" "+Sprigb[5][7]+" "+Sprigb[5][8]+" \n")
print(" "+TopTable[17]+" \n")
print(" "+TopTable[18]+" "+Spriga[6][0]+" "+Spriga[6][1]+" "+Spriga[6][2]+" "+Spriga[6][3]+" "+Spriga[6][4]+" "+Spriga[6][5]+" "+Spriga[6][6]+" "+Spriga[6][7]+" "+Spriga[6][8]+" \n")
print(" "+TopTable[19]+" "+Sprigb[6][0]+" "+Sprigb[6][1]+" "+Sprigb[6][2]+" "+Sprigb[6][3]+" "+Sprigb[6][4]+" "+Sprigb[6][5]+" "+Sprigb[6][6]+" "+Sprigb[6][7]+" "+Sprigb[6][8]+" \n")
print(" "+TopTable[20]+" \n")
print(" "+TopTable[21]+" "+Spriga[7][0]+" "+Spriga[7][1]+" "+Spriga[7][2]+" "+Spriga[7][3]+" "+Spriga[7][4]+" "+Spriga[7][5]+" "+Spriga[7][6]+" "+Spriga[7][7]+" "+Spriga[7][8]+" \n")
print(" "+TopTable[22]+" "+Sprigb[7][0]+" "+Sprigb[7][1]+" "+Sprigb[7][2]+" "+Sprigb[7][3]+" "+Sprigb[7][4]+" "+Sprigb[7][5]+" "+Sprigb[7][6]+" "+Sprigb[7][7]+" "+Sprigb[7][8]+" \n")
print(" "+TopTable[23]+" \n")
print(" "+TopTable[24]+" "+Spriga[8][0]+" "+Spriga[8][1]+" "+Spriga[8][2]+" "+Spriga[8][3]+" "+Spriga[8][4]+" "+Spriga[8][5]+" "+Spriga[8][6]+" "+Spriga[8][7]+" "+Spriga[8][8]+" \n")
print(" "+TopTable[25]+" "+Sprigb[8][0]+" "+Sprigb[8][1]+" "+Sprigb[8][2]+" "+Sprigb[8][3]+" "+Sprigb[8][4]+" "+Sprigb[8][5]+" "+Sprigb[8][6]+" "+Sprigb[8][7]+" "+Sprigb[8][8]+" \n")
print(" "+TopTable[26]+" \n")

#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
#XXXXXXXXXX
#XXXXXXXXXX
#X
