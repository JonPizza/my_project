alive = True

class player:
	def __init__(self, name, hp, inventory):
		hp = self.hp
		inventory = self.inventory
		self.inventory = []
		print('Welcome to ZorkX! A simple parody on Zork written in Python by JonPizza! See my GitHub for more.')
		
	def add_hp(self, gained_hp):
		self.hp += gained_hp
		if self.hp > 100:
			self.hp = 100
	
	def lose_hp(self, lost_hp):
		global alive
		self.hp -= lost_hp
		if self.hp < 0:
			print('Oh well... It appears you have died.\nThanks for playing!')
			alive = False
		
	def get_item(self, item):
		self.inventory.append(item)
	
	def lose_item(self, item):
		try:
			self.inventory.remove(item)
		except:
			print('I dont have that item!')
			
class house:
	def __init__(self, r1, r2, r3, r4, r5):
		self.r1 = r1
		self.r2 = r2
		self.r3 = r3
		self.r4 = r4
		self.r5 = r5
		
		self.r1 = {'items':['old glove', 'brass lantern', 'crystal sword'], 
              'enemies':[],
              'doors':{'s':'r3'},
              'desc':'An ornate ballroom... too bad all the decorations have been smashed and left in ruins.'}

		self.r2 = {'items':['key', 'gold'],
              'enemies':['troll'],
              'doors':{'e':'r3'},
              'desc':'A small vault that appeared to have previously contained vast riches. Some stone gargoyles seem to be staring at you from the corner.'}

		self.r3 = {'items':['wrench', 'page'],
              'enemies':[],
              'doors':{'n':'r1', 'e':'r4', 'w':'r2', 's':'r5'},
              'desc':'A deseted shop, all things of value pilaged!'}

		self.r4 = {'items':['jewel-encrusted gauntlet'],
              'enemies':['cyclops', 'witch', 'theif'],
              'doors':{'w':'r3'},
              'desc':'A labratory left in ruins! Bones and blood are strewn across the floor!'}
		self.r5 = {'items':[],
              'enemies':[],
              'doors':{'n':'r3'},
              'desc':'A small, regular bedroom.'}
	
dungeon = house(1, 2, 3, 4, 5)

def simple_verb(word):
	if word in ['grab', 'get']:
		r_word = 'get'
	elif word in ['throw', 'drop']:
		r_word = 'drop'
	elif word in ['go', 'walk', 'move', 'run']:
		r_word = 'go'
	elif word in ['n', 'north']:
		r_word = 'n'
	elif word in ['s', 'south']:
		r_word = 's'
	elif word in ['w', 'west']:
		r_word = 'w'
	elif word in ['e', 'east']:
		r_word = 'e'
	elif word in ['slay', 'kill', 'hit']:
		r_word = 'hit'
	else:
		return word
	return r_word

def list_commands():
	print('''n/north = go north\n
				 e/east = go east\n
				 s/south = go south\n
				 w/west = go west\n
				 go/walk/move/run <DIRECTION> = Move in a certain direction\n
				 grab/get <ITEM> = Pick up an item\n
				 drop/throw <ITEM> = Drop a item in the room\n''')

def check_dir(word):
  if word in 'nswe':
    return True
  else:
    return False

def parse(command):
  s_command = command.split(' ')
  simple_c = []
  for w in s_command:
    simple_c.append(simple_verb(w))
  for i in simple_c:
    if check_dir(i):
      return ('dir', i)
