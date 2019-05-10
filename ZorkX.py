alive = True

print('Welcome to ZorkX! A simple parody on Zork written in Python by JonPizza! See my GitHub for more.')

class player:
  def __init__(self, hp=100, inventory=[], room='r1'):
    self.hp = hp
    self.inventory = inventory
    self.room = room
    
  def add_hp(self, gained_hp):
    self.hp += gained_hp
    if self.hp > 100:
      self.hp = 100
  
  def lose_hp(self, lost_hp):
    global alive
    self.hp -= lost_hp
    if self.hp < 0:
      print('Oh well... It appears you have died.\nThanks for playing!') # Ask Restart?
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
    
    self.r1 = {'items':['glove', 'lantern', 'sword'], 
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
  
dungeon = house(1, 2, 3, 4, 5) # Create Dungeon
user = player() # Create Player

def room(r):
  if r == 'r1':
    return dungeon.r1
  elif r == 'r2':
    return dungeon.r2
  elif r == 'r3':
    return dungeon.r3
  elif r == 'r4':
    return dungeon.r4
  else: # r = r5
    return dungeon.r5

def simple_verb(word): # todo: inventory & hp/diagnose
  if word in ['grab', 'get', 'take']:
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
  elif word in ['hp', 'health', 'diagnose', 'inventory']:
    r_word = 'diagnose'
  else:
    return word
  return r_word

def list_commands(): # ADD: Diagnose
  print('''n/north = go north\n
         e/east = go east\n
         s/south = go south\n
         w/west = go west\n
         go/walk/move/run <DIRECTION> = Move in a certain direction\n
         grab/get <ITEM> = Pick up an item\n
         drop/throw <ITEM> = Drop a item in the room\n
         commands = This\n
         hit/slay/kill <MONSTER> = Hit an enemy\n
         --\n
         TIP: Use only up to 2 letter words\n''')

def check_dir(word):
  if word in 'nswe':
    return True
  else:
    return False

def check_drop(word):
  if word == 'drop':
    return True
  else:
    return False

def check_hit(word): # The above few commands were me being a dumb*ss. Ik how to do it correct but dont wanna redo working code
  if word == 'hit':
    return True
  else:
    return False

def parse(command): # Need to add some more commands here
  s_command = command.split(' ')
  simple_c = []
  for w in s_command:
    simple_c.append(simple_verb(w))
  for i in simple_c:
    if i != 'go':
      if check_dir(i):
        return ('dir', i)
      elif check_hit(i):
        return ('hit', simple_c[1])
      elif check_drop(i):
        return ('drop', simple_c[1])
      elif i == 'commands' or i == 'command':
        return ('commands')
      else:
        return ('unknown')

def run_parsed(command):
  global dungeon # TODO: Not use this as global... Don't think will be patched in time tho
  global user
  curr_room = user.room
  print(command) # TODO: Remove line
  if command[0] == 'dir':
    for key, value in curr_room['doors'].items():
      if key == command[1]:
  #placeholder, need to interact with dungeon
        user.room = command[1]
        print(room(user.room)['desc'])
      else:
        print(f'I can\'t go that way!')
    #return # Doesn't exist, TODO: try/except block
  elif command[0] == 'hit':
    for i in room(user.room)['enemies']:
      if command[1] == i:
        room(user.room)['enemies'].remove(i)
        print('The ' + str(i) + 'has perished.')
      else:
        print('I see no ' + str(i) + ' here!')
  elif command[0] == 'commands':
    list_commands()
  elif command[0] == 'get':
    #TODO: Move item from commands[1] in house to player
    for item in room(user.room)['items']:
      if item == command[1]:
        user.inventory.append(item)
        print('Grabed ' + str(command[1]) + '.')
      else:
        print('I see no ' + str(command[1]) + ' here!')
  elif command[0] == 'diagnose':
    print(f'Your status:\nHealth:{user.hp}\nInventory:')
    for i in user.inventory:
      print(i)
  elif command[0] == 'drop':
    try:
      user.inventory.remove(command[1])
      print('Dropped ' + str(command[1]))
    except IndexError:
      print('I don\'t have that item!')
  else:
    #Command must = 'unknown'
    print('I dont understand!')

while alive:
  joe_input = input('>>>')
  try:
    run_parsed(parse(joe_input))
  except IndexError:
    print('Add a noun!')
