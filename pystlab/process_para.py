import os , argparse
import collections
import builtins
from collections import ChainMap
pylookup = ChainMap(locals(), globals(), vars(builtins))


# os fundamental path functions
print("file name of current terminal:", os.path.basename(__file__))
print('home directory:', os.environ.get('HOME', 'N/A'))
print('home directory (alternative):', os.path.expanduser('~'))

a={'a':1, 'b':2, 'c':3, 'd':4,}
b={'c':5, 'd':6, 'e':7, 'f':8,}
e={'d':9, 'e':10, 'f':11, 'g':12}

# new_child function and chain map
m1=collections.ChainMap(a,b)
m2=collections.ChainMap(e)
m3=m2.new_child()

print("m1:", m1)
print("m2:", m2)
print("m3:", m3)

# combined method
combined=a.copy()
combined.update(b)
combined.update(e)
print(combined)

# extract keys and values
print("chains",list(m1.keys()))
print(" values",list(m1.values()))
print(m1)
print(m2)
print(m3)
z=m3.parents
print("m3 parents",z)
# 
m3['c'] = 'D'
print('m1["a"]={}'.format(m1['a']))
print("M2",m2)
print("M3",m3)

print(m1.maps)
m1.maps=list(reversed(m1.maps))
print(m1.maps)

#letting user specify cmd line args over the enviroment var

# defaults = {'color': 'blue', 'user': 'guest'}

# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

# combined = ChainMap(defaults,command_line_args, os.environ )
# print(combined['color'])
# print(combined['user'])

# counter objects
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabets')
print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)