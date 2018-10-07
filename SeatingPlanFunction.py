import csv
import sys 
import random
import re

def generate_score(TopTable, Spriga, Sprigb, Name, compatibilitymatrix):
	Best_score=0
	for TestPlace in range(1,188):
		if TestPlace < 27 and TestPlace!=13 and TestPlace!=14:
			if TopTable[TestPlace]!="X":
				if TestPlace<26:
					if TopTable[TestPlace+1]!="X" and TopTable[TestPlace+1]!="Bride (Ellie)" and TopTable[TestPlace+1]!="Groom (Stewart)":
						name_num_plus=Name.index(TopTable[TestPlace+1])
						Best_score+=int(compatibilitymatrix[TopTable[TestPlace]][name_num_plus])
				SprigNum=round(TestPlace/3)
				if Spriga[SprigNum][1]!="X":
					name_num_plus=Name.index(Spriga[SprigNum][1])
					Best_score+=int(compatibilitymatrix[TopTable[TestPlace]][name_num_plus])
				if Sprigb[SprigNum][1]!="X":
					name_num_plus=Name.index(Sprigb[SprigNum][1])
					Best_score+=int(compatibilitymatrix[TopTable[TestPlace]][name_num_plus])
		if TestPlace>27:
			SprigNum=round((TestPlace-27)/18)
			TableSide=(TestPlace-27)%18
			if TableSide<9:
				side="a"
			else:
				side="b"
			if side=="a":
				if TableSide<8:
					if Spriga[SprigNum][TableSide]!="X":
						if Spriga[SprigNum][TableSide+1]!="X":
							name_num_plus=Name.index(Spriga[SprigNum][TableSide+1])
							Best_score+=int(compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_plus])
						if Sprigb[SprigNum][TableSide]!="X":
							name_num_plus=Name.index(Sprigb[SprigNum][TableSide])
							Best_score+=int(compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_plus])
						if Sprigb[SprigNum][TableSide+1]!="X":
							name_num_plus=Name.index(Sprigb[SprigNum][TableSide+1])
							Best_score+=int(compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_plus])
	return Best_score;


def find_swap(TopTable, Spriga, Sprigb, Name, compatibilitymatrix):
	TestPlace = random.randint(1,188)
	while TestPlace == 27 or (TestPlace>10 and TestPlace<=16):
		TestPlace = random.randint(1,188)
	Swap_a={}
	Swap_a["name"]=[]
	Swap_a["table"]=[]
	Swap_a["place"]=[]
	Swap_a["tableside"]=[]
	number_of_people=1
	found_all_matches=False 
	while found_all_matches==False:
		TestPlace=int(TestPlace)
		if (TestPlace < 27 and TestPlace >16) or TestPlace<=10:
			if number_of_people==1:
				Swap_a["name"].append(TopTable[TestPlace])
				Swap_a["table"].append("TT")
				Swap_a["place"].append(TestPlace)
			if TestPlace>1 and TopTable[TestPlace-1]!="X" and TopTable[TestPlace]!="X":
				name_num_a = Name.index(TopTable[TestPlace-1])
				if compatibilitymatrix[TopTable[TestPlace]][name_num_a]=="50" and TopTable[TestPlace-1] not in Swap_a["name"]:
					Swap_a["name"].append(TopTable[TestPlace-1])
					Swap_a["table"].append("TT")
					Swap_a["place"].append(TestPlace-1)
			if TestPlace<26 and TopTable[TestPlace+1]!="X" and TopTable[TestPlace]!="X":
				name_num_b = Name.index(TopTable[TestPlace+1])
				if compatibilitymatrix[TopTable[TestPlace]][name_num_b]=="50" and TopTable[TestPlace+1] not in Swap_a["name"]:
					Swap_a["name"].append(TopTable[TestPlace+1])
					Swap_a["table"].append("TT")
					Swap_a["place"].append(TestPlace+1)
		if TestPlace > 27:
			SprigNum = round((TestPlace-27)/18)
			TableSide=(TestPlace-27)%18
			if TableSide<9:
				side="a" 
			else: 
				side="b"
			if side=="a":
					if number_of_people==1:	
						Swap_a["name"].append(Spriga[SprigNum][TableSide])
						Swap_a["table"].append(SprigNum)
						Swap_a["tableside"].append("a")
						Swap_a["place"].append(TableSide)
					if TableSide>=1 and Spriga[SprigNum][TableSide-1]!="X" and Spriga[SprigNum][TableSide]!="X":
						name_num_a=Name.index(Spriga[SprigNum][TableSide-1])
						if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50" and Spriga[SprigNum][TableSide-1] not in Swap_a["name"]:
							Swap_a["name"].append(Spriga[SprigNum][TableSide-1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("a")
							Swap_a["place"].append(TableSide-1)
					if TableSide<8 and Spriga[SprigNum][TableSide+1]!="X" and Spriga[SprigNum][TableSide]!="X":
						name_num_a=Name.index(Spriga[SprigNum][TableSide+1])
						if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50" and Spriga[SprigNum][TableSide+1] not in Swap_a["name"]:
							Swap_a["name"].append(Spriga[SprigNum][TableSide+1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("a")
							Swap_a["place"].append(TableSide+1)
					if Spriga[SprigNum][TableSide]!="X" and Sprigb[SprigNum][TableSide]!="X":
						name_num_a=Name.index(Sprigb[SprigNum][TableSide])
						if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50" and Sprigb[SprigNum][TableSide] not in Swap_a["name"]:
							Swap_a["name"].append(Sprigb[SprigNum][TableSide])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("b")
							Swap_a["place"].append(TableSide)
			if side=="b":
					if number_of_people==1:	
						Swap_a["name"].append(Sprigb[SprigNum][TableSide-9])
						Swap_a["table"].append(SprigNum)
						Swap_a["tableside"].append("b")
						Swap_a["place"].append(TableSide)
					if TableSide-9>=1 and Sprigb[SprigNum][TableSide-9-1]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
						name_num_a=Name.index(Sprigb[SprigNum][TableSide-9-1])
						if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50" and Sprigb[SprigNum][TableSide-9-1] not in Swap_a["name"]:
							Swap_a["name"].append(Sprigb[SprigNum][TableSide-9-1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("b")
							Swap_a["place"].append(TableSide-1)
					if TableSide-9<8 and Sprigb[SprigNum][TableSide-9+1]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
						name_num_a=Name.index(Sprigb[SprigNum][TableSide-9+1])
						if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50" and Sprigb[SprigNum][TableSide-9+1] not in Swap_a["name"]:
							Swap_a["name"].append(Sprigb[SprigNum][TableSide-9+1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("b")
							Swap_a["place"].append(TableSide+1)
					if Spriga[SprigNum][TableSide-9]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
						name_num_a=Name.index(Spriga[SprigNum][TableSide-9])
						if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50" and Spriga[SprigNum][TableSide-9] not in Swap_a["name"]:
							Swap_a["name"].append(Spriga[SprigNum][TableSide-9])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("a")
							Swap_a["place"].append(TableSide)
		if len(Swap_a["name"])>number_of_people:
			if Swap_a["table"][number_of_people]=="TT":
				TestPlace=Swap_a["place"][number_of_people]
			else:
				TestPlace=Swap_a["place"][number_of_people]+(Swap_a["table"][number_of_people])*18+27
			number_of_people=number_of_people+1
		else: 
			found_all_matches=True 
	return Swap_a;


def find_second_swap(TopTable, Spriga, Sprigb, Name, compatibilitymatrix, Swap_1):
	TestPlace = random.randint(1,188)
	while TestPlace == 27 or (TestPlace>10 and TestPlace<=16):
		TestPlace = random.randint(1,188)
	TestPlace = random.randint(1,188)
	while TestPlace == 27 or (TestPlace>10 and TestPlace<=16):
		TestPlace = random.randint(1,188)
	Swap_a={}
	Swap_a["name"]=[]
	Swap_a["table"]=[]
	Swap_a["place"]=[]
	Swap_a["tableside"]=[]
	number_of_people=1
	found_all_matches=False 
	while found_all_matches==False:
		TestPlace=int(TestPlace)
		if (TestPlace < 27 and TestPlace >16) or TestPlace<=10:
			if number_of_people==1:
				Swap_a["name"].append(TopTable[TestPlace])
				Swap_a["table"].append("TT")
				Swap_a["place"].append(TestPlace)
			if TestPlace>1 and TopTable[TestPlace-1]!="X" and TopTable[TestPlace]!="X":
				name_num_a = Name.index(TopTable[TestPlace-1])
				if compatibilitymatrix[TopTable[TestPlace]][name_num_a]=="50" and TopTable[TestPlace-1] not in Swap_a["name"]:
					Swap_a["name"].append(TopTable[TestPlace-1])
					Swap_a["table"].append("TT")
					Swap_a["place"].append(TestPlace-1)
			if TestPlace<26 and TopTable[TestPlace+1]!="X" and TopTable[TestPlace]!="X":
				name_num_b = Name.index(TopTable[TestPlace+1])
				if compatibilitymatrix[TopTable[TestPlace]][name_num_b]=="50" and TopTable[TestPlace+1] not in Swap_a["name"]:
					Swap_a["name"].append(TopTable[TestPlace+1])
					Swap_a["table"].append("TT")
					Swap_a["place"].append(TestPlace+1)
		if TestPlace > 27:
			SprigNum = round((TestPlace-27)/18)
			TableSide=(TestPlace-27)%18
			if TableSide<9:
				side="a" 
			else: 
				side="b"
			if side=="a":
					if number_of_people==1:	
						Swap_a["name"].append(Spriga[SprigNum][TableSide])
						Swap_a["table"].append(SprigNum)
						Swap_a["tableside"].append("a")
						Swap_a["place"].append(TableSide)
					if TableSide>=1 and Spriga[SprigNum][TableSide-1]!="X" and Spriga[SprigNum][TableSide]!="X":
						name_num_a=Name.index(Spriga[SprigNum][TableSide-1])
						if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50" and Spriga[SprigNum][TableSide-1] not in Swap_a["name"]:
							Swap_a["name"].append(Spriga[SprigNum][TableSide-1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("a")
							Swap_a["place"].append(TableSide-1)
					if TableSide<8 and Spriga[SprigNum][TableSide+1]!="X" and Spriga[SprigNum][TableSide]!="X":
						name_num_a=Name.index(Spriga[SprigNum][TableSide+1])
						if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50" and Spriga[SprigNum][TableSide+1] not in Swap_a["name"]:
							Swap_a["name"].append(Spriga[SprigNum][TableSide+1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("a")
							Swap_a["place"].append(TableSide+1)
					if Spriga[SprigNum][TableSide]!="X" and Sprigb[SprigNum][TableSide]!="X":
						name_num_a=Name.index(Sprigb[SprigNum][TableSide])
						if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50" and Sprigb[SprigNum][TableSide] not in Swap_a["name"]:
							Swap_a["name"].append(Sprigb[SprigNum][TableSide])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("b")
							Swap_a["place"].append(TableSide)
			if side=="b":
					if number_of_people==1:	
						Swap_a["name"].append(Sprigb[SprigNum][TableSide-9])
						Swap_a["table"].append(SprigNum)
						Swap_a["tableside"].append("b")
						Swap_a["place"].append(TableSide)
					if TableSide-9>=1 and Sprigb[SprigNum][TableSide-9-1]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
						name_num_a=Name.index(Sprigb[SprigNum][TableSide-9-1])
						if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50" and Sprigb[SprigNum][TableSide-9-1] not in Swap_a["name"]:
							Swap_a["name"].append(Sprigb[SprigNum][TableSide-9-1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("b")
							Swap_a["place"].append(TableSide-1)
					if TableSide-9<8 and Sprigb[SprigNum][TableSide-9+1]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
						name_num_a=Name.index(Sprigb[SprigNum][TableSide-9+1])
						if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50" and Sprigb[SprigNum][TableSide-9+1] not in Swap_a["name"]:
							Swap_a["name"].append(Sprigb[SprigNum][TableSide-9+1])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("b")
							Swap_a["place"].append(TableSide+1)
					if Spriga[SprigNum][TableSide-9]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
						name_num_a=Name.index(Spriga[SprigNum][TableSide-9])
						if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50" and Spriga[SprigNum][TableSide-9] not in Swap_a["name"]:
							Swap_a["name"].append(Spriga[SprigNum][TableSide-9])
							Swap_a["table"].append(SprigNum)
							Swap_a["tableside"].append("a")
							Swap_a["place"].append(TableSide)
		if len(Swap_a["name"])>number_of_people:
			if Swap_a["table"][number_of_people]=="TT":
				TestPlace=Swap_a["place"][number_of_people]
			else:
				TestPlace=Swap_a["place"][number_of_people]+(Swap_a["table"][number_of_people])*18+27
			number_of_people=number_of_people+1
		else: 
			found_all_matches=True 
	if len(Swap_1["name"])==len(Swap_a["name"]):
		print Swap_1, Swap_a

#	if (TestPlace < 27 and TestPlace >16) or TestPlace<=10:
#		Swap_a["name"].append(TopTable[TestPlace])
#		Swap_a["table"].append("TT")
#		Swap_a["place"].append(TestPlace)
#		if TestPlace>1 and TopTable[TestPlace-1]!="X" and TopTable[TestPlace]!="X":
#			name_num_a = Name.index(TopTable[TestPlace-1])
#			if compatibilitymatrix[TopTable[TestPlace]][name_num_a]=="50":
#				print "50",TopTable[TestPlace], TopTable[TestPlace-1]
#				Swap_a["name"].append(TopTable[TestPlace-1])
#				Swap_a["table"].append("TT")
#				Swap_a["place"].append(TestPlace-1)
#		if TestPlace<26 and TopTable[TestPlace+1]!="X" and TopTable[TestPlace]!="X":
#			name_num_b = Name.index(TopTable[TestPlace+1])
#			if compatibilitymatrix[TopTable[TestPlace]][name_num_b]=="50":
#				print "50", TopTable[TestPlace], TopTable[TestPlace+1]
#				Swap_a["name"].append(TopTable[TestPlace+1])
#				Swap_a["table"].append("TT")
#				Swap_a["place"].append(TestPlace+1)
#	if TestPlace > 27:
#		SprigNum = round((TestPlace-27)/18)
#		TableSide=(TestPlace-27)%18
#		if TableSide<9:
#			side="a" 
#		else: 
#			side="b"
#		if side=="a":
#				Swap_a["name"].append(Spriga[SprigNum][TableSide])
#				Swap_a["table"].append(SprigNum)
#				Swap_a["tableside"].append("a")
#				Swap_a["place"].append(TableSide)
#				if TableSide>1 and Spriga[SprigNum][TableSide-1]!="X" and Spriga[SprigNum][TableSide]!="X":
#					name_num_a=Name.index(Spriga[SprigNum][TableSide-1])
#					if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50":
#						print "50", Spriga[SprigNum][TableSide], Spriga[SprigNum][TableSide-1] 
#						Swap_a["name"].append(Spriga[SprigNum][TableSide-1])
#						Swap_a["table"].append(SprigNum)
#						Swap_a["tableside"].append("a")
#						Swap_a["place"].append(TableSide-1)
#				if TableSide<8 and Spriga[SprigNum][TableSide+1]!="X" and Spriga[SprigNum][TableSide]!="X":
#					name_num_a=Name.index(Spriga[SprigNum][TableSide+1])
#					if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50":
#						print "50", Spriga[SprigNum][TableSide], Spriga[SprigNum][TableSide+1] 
#						Swap_a["name"].append(Spriga[SprigNum][TableSide+1])
#						Swap_a["table"].append(SprigNum)
#						Swap_a["tableside"].append("a")
#						Swap_a["place"].append(TableSide+1)
#				if Spriga[SprigNum][TableSide]!="X" and Sprigb[SprigNum][TableSide]!="X":
#					name_num_a=Name.index(Sprigb[SprigNum][TableSide])
#					if compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_a]=="50":
#						print "50", Spriga[SprigNum][TableSide], Sprigb[SprigNum][TableSide] 
#						Swap_a["name"].append(Sprigb[SprigNum][TableSide])
#						Swap_a["table"].append(SprigNum)
#						Swap_a["tableside"].append("b")
#						Swap_a["place"].append(TableSide)
#		if side=="b":
#				Swap_a["name"].append(Sprigb[SprigNum][TableSide-9])
#				Swap_a["table"].append(SprigNum)
#				Swap_a["tableside"].append("b")
#				Swap_a["place"].append(TableSide)
#				if TableSide-9>1 and Sprigb[SprigNum][TableSide-9-1]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
#					name_num_a=Name.index(Sprigb[SprigNum][TableSide-9-1])
#					if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50":
#						print "50", Sprigb[SprigNum][TableSide-9], Spriga[SprigNum][TableSide-9-1] 
#						Swap_a["name"].append(Sprigb[SprigNum][TableSide-9-1])
#						Swap_a["table"].append(SprigNum)
#						Swap_a["tableside"].append("b")
#						Swap_a["place"].append(TableSide-1)
#				if TableSide-9<8 and Sprigb[SprigNum][TableSide-9+1]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
#					name_num_a=Name.index(Sprigb[SprigNum][TableSide-9+1])
#					if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50":
#						print "50", Sprigb[SprigNum][TableSide-9], Sprigb[SprigNum][TableSide-9+1] 
#						Swap_a["name"].append(Sprigb[SprigNum][TableSide-9+1])
#						Swap_a["table"].append(SprigNum)
#						Swap_a["tableside"].append("b")
#						Swap_a["place"].append(TableSide+1)
#				if Spriga[SprigNum][TableSide-9]!="X" and Sprigb[SprigNum][TableSide-9]!="X":
#					name_num_a=Name.index(Spriga[SprigNum][TableSide-9])
#					if compatibilitymatrix[Sprigb[SprigNum][TableSide-9]][name_num_a]=="50":
#						print "50", Spriga[SprigNum][TableSide-9], Sprigb[SprigNum][TableSide-9] 
#						Swap_a["name"].append(Spriga[SprigNum][TableSide-9])
#						Swap_a["table"].append(SprigNum)
#						Swap_a["tableside"].append("a")
#						Swap_a["place"].append(TableSide)
#	print Swap_a
	return Swap_a;
