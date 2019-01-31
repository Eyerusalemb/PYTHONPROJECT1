import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

import sys
print ('Name is :'sys.argv[1])
print ('PayRate:'sys.argv[2])
print ('Hours :'sys.argv[3])

Name=sys.argv[1]
PayRate=sys.argv[2]
Hours=sys.argv[3]

if Hours <= 40:
  pay=payrate*hours
  
  else:
  othours=houres-40
  pay=40*payrate+othours*[1.5] payrate
  print("pay is ",pay)
  