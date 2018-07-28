#import pylab as plt
import matplotlib.pyplot as plt
import numpy as np

from gnrtEqList import *

plt.figure('line')   #plt.figure(arguments) genrate seprate windows for figure with argument name if it exist it will override that
plt.plot(x,linear)
plt.xlabel('x-points')    #make label of axis  in seprate window only
plt.ylabel('y-points')    #''    ''   ''  ''
plt.title('Linnear graph') # give title to graph in seprate window if you will...


plt.figure('quadrootic')
plt.plot(x,quad)
plt.xlabel('x-points')    #make label of axis  in seprate window only
plt.ylabel('y-points')    #''    ''   ''  ''
plt.title('quadrootic  graph') # give title to graph in seprate window if you will...

plt.figure('cubic')
plt.plot(x,cube)
plt.xlabel('x-points')    #make label of axis  in seprate window only
plt.ylabel('y-points')    #''    ''   ''  ''
plt.title('cubic graph') # give title to graph in seprate window if you will...



plt.figure('exponential')
plt.plot(x,exp)
plt.xlabel('x-points')    #make label of axis  in seprate window only
plt.ylabel('y-points')    #''    ''   ''  ''
plt.title('exponential  graph') # give title to graph in seprate window if you will...


plt.figure('lograthmic')
plt.plot(x,log)
plt.xlabel('x-points')    #make label of axis  in seprate window only
plt.ylabel('y-points')    #''    ''   ''  ''
plt.title('lograthmic graph') # give title to graph in seprate window if you will...



# to be aware of thing that appeared from previous stuffs you have to clear wimdos using'' plt.clf()''  below each window opening

#we can use plot.ylim(0,1000) under opening of window comand of each plot to make limit for y axis

#we can also use labling graph so that it will let me know which one is what                                here how:  plt.plot(x,y,label='name of graph')
#     now where it will show label box depends on plt.legend(loc='upper left') default will decided by      python or pylab
