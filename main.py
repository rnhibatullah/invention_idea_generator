from raw_object import RawObject
from invention_object import InventionObject
import csv
import random


raw_invention_list = []
invention_list=[]

with open('raw_item.csv','r') as file :
	reader = csv.reader(file, delimiter=',')
	for row in reader :
		try:
			raw_obj = RawObject(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]), int(row[5]))
			raw_invention_list.append(raw_obj)
		except:
		 continue

for i in range(len(raw_invention_list)):
	obj_1 = random.choice(raw_invention_list)
	obj_2 = random.choice(raw_invention_list)
	obj_3 = random.choice(raw_invention_list)
	inv_obj = InventionObject(obj_1,obj_2,obj_3)
	invention_list.append(inv_obj)
	inv_obj.write_methode()

	print ("ivention Idea: {} {} {}" .format(obj_1.name, obj_2.name, obj_3.name))






