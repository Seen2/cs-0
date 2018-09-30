s0=input('enter a string:')
print('s0=',s0)
s1=s0
print('s1=s0->:',s1)
print(' i m going to append s1.. but as you know string is immutable so it cause error try to look out comment in code..')
#s1.append('append')

print('i am converting it in list')
s0=list(s0)
print('s0=',s0,'s1=',s1)
print('string and touples are immutable hence above happened now look below for list they are mutable')
s2=s0
print('i make s2=s0\n here below\n',s0,'\n',s2)

print('now i am appending s2..')
s2.append('my fear')

print('and this is\n s0=',s0,'\ns2=',s2)

print('both changed they are mutateable..\n now you can copy s0 as s3=s0[:]')
s3=s0[:]
print('and this is\n s0=',s0,'\ns3=',s3)

print('now i am appending s3..')
s3.append('my fear')
print('and this is\n s0=',s0,'\ns3=',s3)
print('you get the idea all what that it is..')
