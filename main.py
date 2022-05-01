from random import *
 
list = []
throws = 100
sixes = 0
fives = 0
fours = 0
threes = 0
twos = 0
ones = 0

for i in range(throws):
 list.append(randint(1,6))
 
for i in list:
 if i == 6:
   sixes += 1

for i in list:
 if i == 5:
   fives += 1

for i in list:
 if i == 4:
   fours += 1

for i in list:
 if i == 3:
  threes += 1

for i in list:
 if i == 2:
  twos += 1

for i in list:
 if i == 1:
  ones += 1
 
print('Amount of sixes: ', sixes)

print('Amount of fives: ', fives)

print('Amount of fours: ', fours)

print('Amount of threes: ', threes)

print('Amount of twos: ', twos)

print('Amount of ones: ', ones)