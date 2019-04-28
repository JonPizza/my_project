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
      print('Oh well...\nIt appears you have died.\nThanks for playing!')
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
    r1 = self.r1
    r2 = self.r2
    r3 = self.r3
    r4 = self.r4
    r5 = self.r5
    
    self.r1 = {'items':['gloves', 'lantern', 'sword'], 'enemies':[]}
    self.r2 = {'items':['key', 'gold'], 'enemies':['troll']}
    self.r3 = {'items':['wrench', 'page'], 'enemies':[]}
    self.r4 =
    self.r5 = 
  
    
    
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
         drop/throw <ITEM> = Drop a item in the room'''

def parse(command):
  s_command = command.split(' ')
  
  
  
  
  
