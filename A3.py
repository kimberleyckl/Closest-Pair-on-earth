## UPI: clin834
## ID: 955333969
## Name: Chien-Li LIN
## Find the closest pair using earth lat & long (Haversine formula)
## input a instance of (n) and find the next n stores' closest pair, output in alphabet order of name.

import time
import math

def main():
    count = 0
    x = input()
    start_time = time.time()
    while x!= "0":
        instance = int(x)
        count= count+1                                  # Scenario number
        l,c,s = get(instance)                           # l =  [[name,long,lat],...] c=[[long,lat],...]
        dis,coordinate = cal(c)                         # main calculation
        # print("cal(c): ",cal(c))
        store = findstore(l,coordinate)                 # given coordinate and find the store name.
        out(dis,store,count)
        x= input()


def cal(c):
    #coordinate = [[long,lat],[long,lat]]
    #cut half
    length = len(c)
    if length > 3:                          # length = 3+
        if length %2 == 1:                  # if length is odd num
            left = c[: (length//2)+1]       # left =[1,2,3] right=[1,2]
            right = c[(length//2)+1:]
            midx = (c[(length//2)][0] + c[(length//2)+1][0])/2
        else:                               # if length is even num
            left = c[: (length//2)]
            right = c[(length//2):]
            midx = (c[(length//2)][0] + c[(length//2)-1][0])/2
        disleft, outleft = cal(left)
        disright,outright = cal(right)        
        if disleft <= disright:
            # print ("disleft,outleft: ", disleft,outleft)
            # return (disleft,outleft)
            n, out = disleft,outleft
        else:
            # print ("disright,outright: ", disright,outright)
            # return (disright,outright)
            n,out = disright,outright
        # handle mid area
        midn, outn = middle(left,right,n,midx)
        if midn < n:
            n = midn
            out = outn
            # print("midn, outn: ", midn, outn)
        return(n, out)
    elif length == 2:                       # length = 2 
        dis = finddis(c[0][0],c[0][1],c[1][0],c[1][1])
        # print(dis)
        # print("3: ", dis,c)
        return(dis,c)
    else:                                   # length = 3
        dis1 = finddis(c[0][0],c[0][1],c[1][0],c[1][1])
        dis2 = finddis(c[1][0],c[1][1],c[2][0],c[2][1])
        dis3 = finddis(c[0][0],c[0][1],c[2][0],c[2][1])
        if (dis1 <= dis2 and dis1 <= dis3):
            # print("4: ", dis1,c[:2])
            return (dis1, c[:2])
        elif (dis2 <= dis3 and dis2 <= dis1):
            # print("5: ", dis2,c[1:])
            return (dis2, c[1:])
        else:   
            return(dis3,[[c[0][0],c[0][1]],[c[2][0],c[2][1]]])

def middle(left,right,n,midx):
    # left = [[1,2],[2,2],[3,1]] (originally sorted by x)
    n = (n/6371) /(math.pi/180)
    candidatelist=[]    
    candidateleft=[]
    candidateright=[]
    for pts in left:   
        if pts[0] > (midx-n):                   # if pts in left in midx-n
            candidatelist.append(pts) 
            candidateleft.append(pts) 
    for pts in right:
        if pts[0] < (midx+n):                    # if pts in right in midx+n
            candidatelist.append(pts)
            candidateright.append(pts) 
    if len(candidateleft) == 0:
        return (100000000,"none")
    if len(candidateright) == 0:
        return (100000000,"none")
    if len(candidatelist) < 2:
        return (100000000,"none")

    candidateleft = sorted(candidateleft, key = lambda x: x[1])
    candidateright = sorted(candidateright, key = lambda x: x[1])  
    outdis = 1000000000
    out = []  
    for i in range(len(candidateleft)):
        can = candidateright[:]                         # construct a list that will pop the no use value
        for j in range(len(candidateright)):
            if (candidateright[j][1] < (candidateleft[i][1] - n)):
                # redundant value
                can.pop(0)   
            else:
                if (candidateright[j][1] <= (candidateleft[i][1] + n)):
                    # find dis
                    dis = finddis(candidateleft[i][0],candidateleft[i][1],candidateright[j][0],candidateright[j][1])
                    if outdis > dis:
                        outdis = dis
                        out = [[candidateleft[i][0],candidateleft[i][1]],[candidateright[j][0],candidateright[j][1]]]
        candidateright = can                            # assign list without redundant value
        #find closest y in candidateright (3 value) and find dis
    return(outdis,out)

    # check length of candidatelist (no point construct box for 3- num in candidate)
    # if len(candidatelist) < 2:
    #     return (1000000, "none")
    # elif len(candidatelist) == 2:
    #     re = finddis(candidatelist[0][0],candidatelist[0][1],candidatelist[1][0],candidatelist[1][1])
    #     if n <= re:
    #         return (1000000, "none")
    #     else:
    #         print ("when candidatelist has 2: ", re,candidatelist)
    #         return (re,candidatelist)
    
    # sorted(candidatelist, key = lambda x: x[1])  # candidatelist = [[3,1],[1,2],[2,2]...] (sort by y and in mid+-n)

def out(d,store,count):
    print("Scenario %d:" %count)
    print("Closest pair:",store[0],store[1])
    print("Distance: %.1f" % d)


def findstore(l,coordinate):
    stores = []

    for i in range(len(l)):
        if l[i][0] == coordinate[0][0]:
            if l[i][1] == coordinate[0][1]:
                stores.append(l[i][2]) 
        if l[i][0] == coordinate[1][0]:
            if l[i][1] == coordinate[1][1]:
                stores.append(l[i][2])
    # print(stores)
    stores.sort()
    return stores

def finddis(ax,ay,bx,by):
    # find smallest c
    a = math.sin((by-ay)*0.00872664625)*math.sin((by-ay)*0.00872664625) + math.cos(ay*0.01745329251) * math.cos(by*0.01745329251) * math.sin((bx-ax)*0.00872664625) * math.sin((bx-ax)*0.00872664625)
    c =  2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    c = 6371 * c
    # c = math.sqrt((bx-ax)*(bx-ax) + (by-ay)*(by-ay))
    return c

def get(x):
    coordinates = []
    stores = []
    listOfStores = []
    for i in range(0,x):
        string = input().split()            # name = string[0],     lat = string[1],        long = string[2]
        listOfStores.append([float(string[-1]),float(string[-2]),''.join(string[0:-2])])              # listOfStore = [[long,lat,name],[long,lat,name]]
        coordinates.append([float(string[-1]),float(string[-2])])     #coordinate = [[long,lat],[long,lat]]
        stores += ([''.join(string[0:-2])])      #stores = [name,name]
    coordinates.sort()
    return (listOfStores,coordinates,stores)

    






main()

