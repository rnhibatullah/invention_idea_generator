from raw_object import RawObject

class InventionObject:
	
	def __init__(self, obj_1, obj_2, obj_3 ):

		self.name = obj_1.name + " " + obj_2.name + " " + obj_3.name

		self.totalscore =  obj_1.calculate_total() + obj_2.calculate_total() + obj_3.calculate_total()

	def write_methode(self):

		invention_file = open("invention_list.txt","w+")
		invention_file.write(" Invention name : {} , totalscore : {} ".format(self.name, self.totalscore))
