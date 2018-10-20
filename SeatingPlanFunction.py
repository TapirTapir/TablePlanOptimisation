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
							Swap_a["place"].append(TableSide+9)
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
							Swap_a["place"].append(TableSide-9)
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
	foundmatch=False
	while foundmatch==False:
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
								Swap_a["place"].append(TableSide+9)
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
								Swap_a["place"].append(TableSide-9)
			if len(Swap_a["name"])>number_of_people:
				if Swap_a["table"][number_of_people]=="TT":
					TestPlace=Swap_a["place"][number_of_people]
				else:
					TestPlace=Swap_a["place"][number_of_people]+(Swap_a["table"][number_of_people])*18+27
				number_of_people=number_of_people+1
			else: 
				found_all_matches=True 
		if len(Swap_1["name"])-len(Swap_a["name"])==1:
			print Swap_1, Swap_a
			Max_swap_a = int(max(Swap_a["place"]))
			Min_swap_a = int(min(Swap_a["place"]))
			added = 0
			if Swap_a["table"][0]=="TT":
				if (Max_swap_a+1<27 and Max_swap_a+1>16) or Max_swap_a+1<=10:
					if ((Max_swap_a+2<27 and Max_swap_a+2>16) or Max_swap_a+2<=10) and TopTable[Max_swap_a+2]!="X" and TopTable[Max_swap_a+1]!="X":
						name_num_a=Name.index(TopTable[Max_swap_a+2])
						print TopTable[Max_swap_a+2]
						print compatibilitymatrix[TopTable[Max_swap_a+1]][name_num_a]
						if int(compatibilitymatrix[TopTable[Max_swap_a+1]][name_num_a])!=50:
							print "entered here", compatibilitymatrix[TopTable[Max_swap_a+1]][name_num_a]
							Swap_a["name"].append(TopTable[Max_swap_a+1])
							Swap_a["table"].append("TT")
							Swap_a["tableside"].append("TT")
							Swap_a["place"].append(Max_swap_a+1)
							added=added+1
					else:
						print "entered here", Max_swap_a+1
						Swap_a["name"].append(TopTable[Max_swap_a+1])
						Swap_a["table"].append("TT")
						Swap_a["tableside"].append("TT")
						Swap_a["place"].append(Max_swap_a+1)
						added=added+1
				if added<1:
					if (Min_swap_a-1>=0 and Min_swap_a-1<10) or Min_swap_a-1>=16:
						if ((Min_swap_a-2>=0 and Min_swap_a-2<10) or Min_swap_a-2>=16) and TopTable[Min_swap_a-2]!="X" and TopTable[Min_swap_a-1]!="X":
							name_num_a=Name.index(TopTable[Min_swap_a-2])
							print TopTable[Min_swap_a-2], TopTable[Min_swap_a-1]
							print compatibilitymatrix[TopTable[Min_swap_a-1]][name_num_a]
							if int(compatibilitymatrix[TopTable[Min_swap_a-1]][name_num_a])!=50:
								print "entered here", compatibilitymatrix[TopTable[Min_swap_a-1]][name_num_a]
								Swap_a["name"].append(TopTable[Min_swap_a-1])
								Swap_a["table"].append("TT")
								Swap_a["tableside"].append("TT")
								Swap_a["place"].append(Min_swap_a-1)
								added=added+1
						else:
							print "entered here", Min_swap_a-1
							Swap_a["name"].append(TopTable[Min_swap_a-1])
							Swap_a["table"].append("TT")
							Swap_a["tableside"].append("TT")
							Swap_a["place"].append(Min_swap_a-1)
							added=added+1
			if Swap_a["table"][0]!="TT":
				tableside=Swap_a["tableside"][Swap_a["place"].index(Max_swap_a)]
				table=Swap_a["table"][0]
				if Max_swap_a+1<9:
					if tableside=="a":
						if Max_swap_a+2<9 and Spriga[table][Max_swap_a+1]!="X" and Spriga[table][Max_swap_a+2]!="X" and Sprigb[table][Max_swap_a+1]!="X":
							name_num_a=Name.index(Spriga[table][Max_swap_a+2])
							name_num_b=Name.index(Sprigb[table][Max_swap_a+1])
							print Spriga[table][Max_swap_a+2]
							print int(compatibilitymatrix[Spriga[table][Max_swap_a+1]][name_num_a])
							if int(compatibilitymatrix[Spriga[table][Max_swap_a+1]][name_num_a])!=50 and int(compatibilitymatrix[Spriga[table][Max_swap_a+1]][name_num_b])!=50:
								print "entered here", compatibilitymatrix[Spriga[table][Max_swap_a+1]][name_num_a]
								Swap_a["name"].append(Spriga[table][Max_swap_a+1])
								Swap_a["table"].append(table)
								Swap_a["tableside"].append(tableside)
								Swap_a["place"].append(Max_swap_a+1)
								added=added+1
						else:
							if Sprigb[table][Max_swap_a+1]!="X" and Spriga[table][Max_swap_a+1]!="X":
								name_num_b=Name.index(Sprigb[table][Max_swap_a+1])
								if int(compatibilitymatrix[Spriga[table][Max_swap_a+1]][name_num_b])!=50:
									print "2nd X a", Spriga[table][Max_swap_a+1], Sprigb[table][Max_swap_a+1]
									Swap_a["name"].append(Spriga[table][Max_swap_a+1])
									Swap_a["table"].append(table)
									Swap_a["tableside"].append(tableside)
									Swap_a["place"].append(Max_swap_a+1)
									added=added+1
							else:
								print "2nd X d", Spriga[table][Max_swap_a+1]
								Swap_a["name"].append(Spriga[table][Max_swap_a+1])
								Swap_a["table"].append(table)
								Swap_a["tableside"].append(tableside)
								Swap_a["place"].append(Max_swap_a+1)
								added=added+1
					if tableside=="b":
						if Max_swap_a+2-9<9 and Sprigb[table][Max_swap_a+1-9]!="X" and Sprigb[table][Max_swap_a+2-9]!="X" and Spriga[table][Max_swap_a+1-9]!="X":
							name_num_a=Name.index(Sprigb[table][Max_swap_a+2-9])
							name_num_b=Name.index(Spriga[table][Max_swap_a+1-9])
							print Sprigb[table][Max_swap_a+2-9]
							print int(compatibilitymatrix[Sprigb[table][Max_swap_a+1-9]][name_num_a])
							if int(compatibilitymatrix[Sprigb[table][Max_swap_a+1-9]][name_num_a])!=50 and int(compatibilitymatrix[Sprigb[table][Max_swap_a+1-9]][name_num_b])!=50:
								print "entered here", compatibilitymatrix[Sprigb[table][Max_swap_a+1-9]][name_num_a]
								print "tableside b", Sprigb[table]
								Swap_a["name"].append(Sprigb[table][Max_swap_a+1-9])
								Swap_a["table"].append(table)
								Swap_a["tableside"].append(tableside)
								Swap_a["place"].append(Max_swap_a+1)
								added=added+1
						else:
							if Spriga[table][Max_swap_a+1-9]!="X":
								name_num_b=Name.index(Spriga[table][Max_swap_a+1-9])
								if int(compatibilitymatrix[Sprigb[table][Max_swap_a+1-9]][name_num_b])!=50:
									print "2nd", Sprigb[table][Max_swap_a+1-9]
									Swap_a["name"].append(Sprigb[table][Max_swap_a+1-9])
									Swap_a["table"].append(table)
									Swap_a["tableside"].append(tableside)
									Swap_a["place"].append(Max_swap_a+1)
									added=added+1
							else:
								print "2nd", Sprigb[table][Max_swap_a+1-9]
								Swap_a["name"].append(Sprigb[table][Max_swap_a+1-9])
								Swap_a["table"].append(table)
								Swap_a["tableside"].append(tableside)
								Swap_a["place"].append(Max_swap_a+1)
								added=added+1
				if added<1:
					if Min_swap_a-9-1>=0:
						if tableside=="a":
							if ((Min_swap_a-2>=0 and Min_swap_a-2<10) or Min_swap_a-2>16) and Spriga[table][Min_swap_a-1]!="X" and Spriga[table][Min_swap_a-2]!="X" and Sprigb[table][Min_swap_a-1]!="X":
								name_num_a=Name.index(Spriga[table][Min_swap_a-2])
								name_num_b=Name.index(Sprigb[table][Min_swap_a-1])
								print Spriga[table][Min_swap_a-2]
								print int(compatibilitymatrix[Spriga[table][Min_swap_a-1]][name_num_a])
								if int(compatibilitymatrix[Spriga[table][Min_swap_a-1]][name_num_a])!=50 and int(compatibilitymatrix[Spriga[table][Min_swap_a-1]][name_num_b])!=50:
									print "entered here", compatibilitymatrix[Spriga[table][Min_swap_a-1]][name_num_a]
									Swap_a["name"].append(Spriga[table][Min_swap_a-1])
									Swap_a["table"].append(table)
									Swap_a["tableside"].append(tableside)
									Swap_a["place"].append(Min_swap_a-1)
									added=added+1
							else:
								if Sprigb[table][Min_swap_a-1]!="X":
									name_num_b=Name.index(Sprigb[table][Min_swap_a-1])
									if int(compatibilitymatrix[Spriga[table][Min_swap_a-1]][name_num_b])!=50:
										print "2nd", Spriga[table][Min_swap_a-1]
										Swap_a["name"].append(Spriga[table][Min_swap_a-1])
										Swap_a["table"].append(table)
										Swap_a["tableside"].append(tableside)
										Swap_a["place"].append(Min_swap_a-1)
										added=added+1
								else:
									print "2nd", Spriga[table][Min_swap_a-1]
									Swap_a["name"].append(Spriga[table][Min_swap_a-1])
									Swap_a["table"].append(table)
									Swap_a["tableside"].append(tableside)
									Swap_a["place"].append(Min_swap_a-1)
									added=added+1
						if tableside=="b":
							if Min_swap_a-2-9>=0 and Sprigb[table][Min_swap_a-1-9]!="X" and Sprigb[table][Min_swap_a-2-9]!="X" and Spriga[table][Min_swap_a-1-9]!="X":
								name_num_a=Name.index(Sprigb[table][Min_swap_a-2-9])
								name_num_b=Name.index(Spriga[table][Min_swap_a-1-9])
								print Sprigb[table][Min_swap_a-2-9]
								print int(compatibilitymatrix[Sprigb[table][Min_swap_a-1-9]][name_num_a])
								if int(compatibilitymatrix[Sprigb[table][Min_swap_a-1-9]][name_num_a])!=50 and int(compatibilitymatrix[Sprigb[table][Min_swap_a-1-9]][name_num_b])!=50:
									print "entered here", compatibilitymatrix[Sprigb[table][Min_swap_a-1-9]][name_num_a]
									print "minus 1 b", Sprigb[table]
									Swap_a["name"].append(Sprigb[table][Min_swap_a-1-9])
									Swap_a["table"].append(table)
									Swap_a["tableside"].append(tableside)
									Swap_a["place"].append(Min_swap_a-1)
									added=added+1
							else:	
								if Spriga[table][Min_swap_a-1-9]!="X" and Sprigb[table][Min_swap_a-1-9]!="X":
									name_num_b=Name.index(Spriga[table][Min_swap_a-1-9])
									if int(compatibilitymatrix[Sprigb[table][Min_swap_a-1-9]][name_num_b])!=50:
										print "2nd", Spriga[table][Min_swap_a-1-9]
										Swap_a["name"].append(Sprigb[table][Min_swap_a-1-9])
										Swap_a["table"].append(table)
										Swap_a["tableside"].append(tableside)
										Swap_a["place"].append(Min_swap_a-1)
										added=added+1
								else:
									print "2nd", Spriga[table][Min_swap_a-1-9]
									Swap_a["name"].append(Sprigb[table][Min_swap_a-1-9])
									Swap_a["table"].append(table)
									Swap_a["tableside"].append(tableside)
									Swap_a["place"].append(Min_swap_a-1)
									added=added+1
		print len(Swap_1["name"]), len(Swap_a["name"])
		if len(Swap_1["name"])==len(Swap_a["name"]):	
			print Swap_1, Swap_a
			foundmatch=True
			
	return Swap_a;
