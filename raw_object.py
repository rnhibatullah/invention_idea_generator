class RawObject:
	
	def __init__(self, name, cost,novelty, size, skill, viable ):
		
		self.name = name

		if  cost <15 and cost > 0 :
			self.cost = cost
		else :
			print("cost of {} {} not in range of 1 - 10 ".format(self.name,self.cost))
			return

		if  novelty <10 and cost >0 :
			self.novelty = novelty
		else :
			print("novelty of {} {} not in range of 1 - 10 ".format(self.name,self.novelty))
			return

		if size <5 and size > 0:
			self.size = size
		else:
			print("size of {} {} not in range of 1 - 5 " .format(self.name,self.size))
			return

		if  skill<30 and skill > 0 :
			self.skill = skill
		else :
			print("skill {} {} not in range of 1 - 30 ".format(self.name,self.skill))
			return
		
		if  viable <40 and viable > 0 :
			self.viable = viable
		else :
			print("viability {} {} not in range of 1 - 30 ".format(self.name,self.viable))
			return

	def calculate_total(raw_obj):
		return raw_obj.cost + raw_obj.novelty + raw_obj.size + raw_obj.skill + raw_obj.viable 

