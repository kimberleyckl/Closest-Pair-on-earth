## UPI: clin834
## ID: 955333969
## Name: Chien-Li LIN
## Find the closest pair using earth lat & long (Haversine formula)
## input a instance of (n) and find the next n stores' closest pair, 
## output Scenario num, name, distance.
import math
def main():
    count = 0
    x = input()
    while x!= "0":
        instance = int(x)
        count= count+1                                  # Scenario number
        l = get(instance)                           # l =  [[name,long,lat],...] c=[[long,lat],...]
        dis,store = cal(l)                         # main calculation
        dis = dis *6371
        store.sort()
        out(dis,store,count)
        x= input()

def cal(c):
    #coordinate = [[long,lat],[long,lat]]
    #cut half
    length = len(c)
    if length > 3:                          # length = 3+
        halflength = (length//2)
        if length %2 == 1:                  # if length is odd num
            left = c[: halflength+1]       # left =[1,2,3] right=[1,2]
            right = c[halflength+1:]
            midx = (c[halflength][0] + c[halflength+1][0])/2
        else:                               # if length is even num
            left = c[: halflength]
            right = c[halflength:]
            midx = (c[halflength][0] + c[halflength-1][0])/2
        disleft, outleft = cal(left)
        disright,outright = cal(right)        
        if disleft <= disright:
            n, out = disleft,outleft
        else:
            n,out = disright,outright

        # handle mid area
        midn, outn = middle(c,n,midx)
        if midn < n:
            n = midn
            out = outn
        return(n, out)
    elif length == 2:                       # length = 2 
        dis = finddis(c[0][0],c[0][1],c[1][0],c[1][1])
        return(dis,[c[0][2],c[1][2]])
    else:                                   # length = 3
        dis1 = finddis(c[0][0],c[0][1],c[1][0],c[1][1])
        dis2 = finddis(c[1][0],c[1][1],c[2][0],c[2][1])
        dis3 = finddis(c[0][0],c[0][1],c[2][0],c[2][1])
        if (dis1 <= dis2 and dis1 <= dis3):
            return (dis1, [c[0][2],c[1][2]])
        elif (dis2 <= dis3 and dis2 <= dis1):
            return (dis2, [c[1][2],c[2][2]])
        else:   
            return(dis3,[c[0][2],c[2][2]])

def middle(c,n,midx):
    # left = [[1,2],[2,2],[3,1]] (originally sorted by x)
    n = (n)/(0.00872664625) 
    candidatelist=[]    
    # candidateleft=[]
    # candidateright=[]
    for pts in c:   
        if finddis(pts[0],pts[1],midx,pts[1]) < n:                   # if pts in midx zone
            candidatelist.append(pts) 
            # candidateleft.append(pts) 


    # cl = len(candidateleft)
    # cr = len(candidateright)

    
    # candidateleft = sorted(candidateleft, key = lambda x: x[1])
    # candidateright = sorted(candidateright, key = lambda x: x[1])
    candidatelist  =sorted(candidatelist, key = lambda x: x[1])
    outdis = 200400
    out = []  
    for i in range(0,len(candidatelist)-3):
        for j in range(1,4):
            m = finddis(candidatelist[i][0],candidatelist[i][1],candidatelist[i+j][0],candidatelist[i+j][1])
            if m < n and m<outdis:
                outdis = m
                out = [candidatelist[i][2],candidatelist[i+j][2]]
    m = finddis(candidatelist[-2][0],candidatelist[-2][1],candidatelist[-1][0],candidatelist[-1][1])
    if m < n and m<outdis:
        outdis = m
        out = [candidatelist[-2][2],candidatelist[-1][2]]    
    return(outdis,out)
    


def out(d,store,count):
    print("Scenario %d:" %count)
    print("Closest pair:",store[0],store[1])
    print("Distance: %.1f" % d)


def finddis(ax,ay,bx,by):
    # find smallest c
    a = math.sin((by-ay)*0.00872664625)*math.sin((by-ay)*0.00872664625) + math.cos(ay*0.01745329251) * math.cos(by*0.01745329251) * math.sin((bx-ax)*0.00872664625) * math.sin((bx-ax)*0.00872664625)
    c =  2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    # c = 6371 * c
    return c

def get(x):
    coordinates = []
    listOfStores = []
    for i in range(0,x):
        string = input().split()            # name = string[0],     lat = string[1],        long = string[2]
        listOfStores.append([float(string[-1]),float(string[-2]),''.join(string[0:-2])])              # listOfStore = [[long,lat,name],[long,lat,name]]
    listOfStores.sort()
    return (listOfStores)

main()

