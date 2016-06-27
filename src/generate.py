import json
from collections import OrderedDict

all_mine = {}

def pop(parent,mine, obj):
  left_side =  parent.replace('[','').replace(']','-')
  if left_side[-1:] == "-": left_side = left_side[:-1]

  if isinstance(obj, dict):
    for x in obj:
      mine = "{}-{}".format(mine,x)
      pop("{}[{}]".format(parent,x), mine, obj[x])
  elif isinstance(obj, basestring):
    all_mine[left_side] = parent
  elif isinstance(obj, int):
    all_mine[left_side] = parent
  else:
    print "# UNKNOWN ", type(obj)


#log.json contains ONE alert record from eve.json
with open('log.json','r') as f:
  c = f.read()
  pop('', '', json.loads(c))


#So I can see them in order at the end, made the blog post easier.
od = OrderedDict(sorted(all_mine.items()))

#This is what I want them to look like after.
#"kernel_packets" => "%{stats[capture][kernel_packets]}"
for mine in od:
  print "         \"{}\" => \"%{{{}}}\"    ".format(mine, all_mine[mine])
