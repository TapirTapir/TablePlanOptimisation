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
					if TopTable[TestPlace+1]!="X":
						name_num_plus=0
						for name in Name:
							if name==TopTable[TestPlace+1]:
								Best_score+=int(compatibilitymatrix[TopTable[TestPlace]][name_num_plus])
							name_num_plus+=1
				SprigNum=round(TestPlace/3)
				if Spriga[SprigNum][1]!="X":
					name_num_plus=0
					for name in Name:
						if name==Spriga[SprigNum][1]:
							Best_score+=int(compatibilitymatrix[TopTable[TestPlace]][name_num_plus])
						name_num_plus+=1
				if Sprigb[SprigNum][1]!="X":
					name_num_plus=0
					for name in Name:
						if name==Sprigb[SprigNum][1]:
							Best_score+=int(compatibilitymatrix[TopTable[TestPlace]][name_num_plus])
						name_num_plus+=1
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
							name_num_plus=0
							for name in Name:
								if name==Spriga[SprigNum][TableSide+1]:
									Best_score+=int(compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_plus])
								name_num_plus+=1
						if Sprigb[SprigNum][TableSide]!="X":
							name_num_plus=0
							for name in Name:
								if name==Sprigb[SprigNum][TableSide]:
									Best_score+=int(compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_plus])
								name_num_plus+=1
						if Sprigb[SprigNum][TableSide+1]!="X":
							name_num_plus=0
							for name in Name:
								if name==Sprigb[SprigNum][TableSide+1]:
									Best_score+=int(compatibilitymatrix[Spriga[SprigNum][TableSide]][name_num_plus])
								name_num_plus+=1
	return Best_score;


def find_swap(TopTable, Spriga, Sprigb):
	TestPlace = random.randint(1,188)
	while TestPlace == 27 or (TestPlace>10 and TestPlace<=16):
		TestPlace = random.randint(1,188)
	Swap_a={}
	if (TestPlace < 27 and TestPlace >16) or TestPlace<=10 :
		Swap_a["name"]=TopTable[TestPlace]
		Swap_a["table"] ="TT"
		Swap_a["place"] = TestPlace
	if TestPlace > 27:
		SprigNum = round((TestPlace-27)/18)
		TableSide=(TestPlace-27)%18
		if TableSide<9:
			side="a" 
		else: 
			side="b"
		if side=="a":
				Swap_a["name"]=Spriga[SprigNum][TableSide]
				Swap_a["table"] = SprigNum
				Swap_a["tableside"]="a"
				Swap_a["place"]=TableSide
		if side=="b":
				Swap_a["name"]=Sprigb[SprigNum][TableSide-9]
				Swap_a["table"]= SprigNum
				Swap_a["tableside"]="b"
				Swap_a["place"]=TableSide
	return Swap_a;
