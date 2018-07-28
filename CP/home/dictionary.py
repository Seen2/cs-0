def createDict(lyricss):
    myDict={}
    for word in lyricss:
        if word in myDict:
            myDict[word] +=1

        else:
            myDict[word]=1

    return myDict



lyrics="he they were wake up still moves to work the work till the death if they work for others so be the person to work together not everyone have utility to change the world it is is only to those who believe in themselves they have to wakeup again and work till the word start changing in front of them like the way they did for this world"

lyricss=lyrics.split()

print(createDict(lyricss))
Dict=createDict(lyricss)

print('Max occured word is')

print(max(Dict))

print('Min occured word',min(Dict))



val=Dict.values()
ke=Dict.keys()
print('Frequency of max ocurred value is', end='')
print(max(val))

for words in ke:

    if Dict[words]==max(val):
        print('word "{}" occured is maximum'.format(words))
        break
    else:
        pass


print('frequency of minimum occured word is:',(min(val)))
for words in ke:
    if Dict[words]==min(val):
        print('minimum occurred word is:',words)
        break




