class Player():
	
	def __init__(self,name,age,team,position):
		self.name = name
		self.age = age
		self.team = team
		self.position = position

	def coach(self):
		
		print(f"this is best coah of {self.team}")

New_Player = Player("Sabaly",322,"Man City","left winger")

print(New_Player.name)
print(New_Player.age)
print(New_Player.position)
print(New_Player.team)
	