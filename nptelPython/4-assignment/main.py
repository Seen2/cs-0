def orangecap(d):
    scoreCard={}
    for match in d:
        for player in d[match]:
            
            if(player in scoreCard):
                scoreCard[player] += d[match][player]
            else:
                scoreCard[player]=d[match][player]
    highestScore=max(scoreCard.values())

    for player in scoreCard:
        if scoreCard[player]==highestScore:
            return (player,highestScore)
    
    return None

def addpoly(p1,p2):
    p=[]
    for term1,term2 in zip(p1,p2):
        if term1[1]==term2[1]:
            if term1[0]+term2[0] !=0:
                p.append((term1[0]+term2[0],term1[1]))
            else:
                pass
        else:
            p.append(term1)
            p.append(term2)

    p.sort()
    return  p

def multpoly(p1,p2):
    p=[]
    for term1 in p1:
        for term2 in p2:
            p.append((term1[0]*term2[0],+term1[1]+term2[1]))
    for term in p[:len(p)//2]:
        for check in p[len(p)//2:]:
            if term[1]==check[1]:
                del p[p.index(term)]
                del p[p.index(check)]
                if term[0]+check[0] !=0:
                    p.append((term[0]+check[0],term[1]))

                
    return p

print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))

