from Text_to_speech import textToSpeech
from speech_to_text import speech_recognition
mepco={"entrance":[['mcc',50]],
"mcc":[['office',10],["entrance",50]],
"office":[["mcc",10],['library',20]],
"library":[['civil block',20],['office',20]],
"civil block":[['library',20],['eee block',50]],
"eee block":[['civil block',50],['computer block',30]],
"computer block":[['road1',10],['eee block',30]],
'road1':[['computer block',10],['ece block',30],['bank',50]],
'ece block':[['road1',30],['mech block',50]],
'bank':[['road1',50],['road2',20]],
"road2":[['bramha putra hostel',50],['bank',20]],
'mech block':[['ece block',50],['narmadha hostel',100]],
"narmadha hostel":[['road3',10],['mech block',100]],
"road3":[['narmadha hostel',10],['kaveri hostel',20]],
"kaveri hostel":[['road3',20],['godavari hostel',5]],
'godavari hostel':[['kaveri hostel',5],['krishna hostel',35]],
'krishna hostel':[['bramha putra hostel',5],['godavari hostel',35]],
'bramha putra hostel':[['road2',50],['krishna hostel',5]]
}
vertex=list(mepco.keys())
open=[]
path=[]
visited=[]
initial=''

# initial=input("enter the initial node:")
totalcost=0
def dijstras(open,path,visited,initial):
    list1=mepco[initial]
    visited.append(initial)
    for i in list1:
        open.append([initial,i[1],i[0]])
    while(True):
        if all(item in visited for item in vertex):
           return path
        min=open[0]
        for i in open:
            if(i[1]<min[1]):
                min=i
        if min[2] not in visited:
            path.append(min)
        open.remove(min)
        visited.append(min[2])
        node=mepco[min[2]]
        for i in node:
            if i[0] not in visited:
                open.append([min[2],min[1]+i[1],i[0]])
def pathfinder(visited,destination):
    path=[]
    cost=[]
    a=destination
    while(True):
        if destination==initial:
            path.append(initial)
            cost.append(50)
            break
        for i in visited:
            if i[2]==destination:
                path.append(i[2])
                cost.append(i[1])
                destination=i[0]
    path.reverse()
    for i in visited:
        if i[2]==a:
            totalcost=i[1]
            break
    print('The total cost for the path:',totalcost)
    print("The path obtained:")
    print(path)
    return path,cost,totalcost
def straight(point1,point2):
    line1=['entrance','mcc','library','main office','civil block','eee block', 'computer block','ece block','mech block','narmadha hostel']
    line2=['bank','bramha putra hostel','krishna hostel','kaveri hostel','godavari hostel']
    flag=0
    if point1 in line1:
        if point2 in line2:
            flag=1
    if flag==1:
        return True 
    else:
        return False
def stringmaker(path,cost,totalcost):
    string=''
    count=0
    for i in path:
        if i[0]=='r' and i[1]=='o'and i[2]=='a':
            ind=path.index(i)
            if(straight(path[ind-1],path[ind+1])):
                string=string+'Take '+i+'in'+str(cost[count])
                count+=1
            else:
                string=string+' Avoid '+i+'   which is '+str(cost[count])+'   apart '
                count+=1
        elif (path[len(path)-1]==i):
            string+='    Go straight in   '+str(cost[count])+' meters your will reach '+i+'  which is the destination'
            string+='    The total distance travelled is'+str(totalcost)
            string+='    Its been a pleasure travelling with you sir Thank you sir  '
            count+=1
        elif(count%2==0):
            string=string +'    Proceed Further within '+str(cost[count])+' meters you will find'+i
            count+=1
        else:
            string=string +'    Go straight in  '+str(cost[count])+'  meters you will find '+i
            count+=1
    return string
def frequencyanalyser(initial,destination):
    initial=initial.lower()
    destination=destination.lower()
    initial=initial.strip()
    destination=destination.strip()
    nodes=vertex
    print(nodes)
    frequency=[]
    for i in nodes:
        val=0
        for j in i:
            val+=ord(j)
        frequency.append(val)
    initial_freq=0
    for i in initial:
        initial_freq+=ord(i)
    des_freq=0
    for i in destination:
        des_freq+=ord(i)
    val=0
    for i in frequency:
        diff=i-initial_freq
        if (diff<0):
            diff=-1*diff
        if i<val:
            val=i
    flag=0
    for i in range(len(frequency)):
        diff=frequency[i]-initial_freq
        if diff<0:
            diff=-1*diff
        if diff==val:
            flag=i
            break
    initial=nodes[flag]
    val=0
    for i in frequency:
        diff=i-des_freq
        if (diff<0):
            diff=-1*diff
        if i<val:
            val=i
    flag=0
    for i in range(len(frequency)):
        diff=frequency[i]-des_freq
        if diff<0:
            diff=-1*diff
        if diff==val:
            flag=i
            break
    destination=nodes[flag]
    return initial,destination
        
# string ='Record your input in the form of      source to destination'
# textToSpeech(string)
# input=speech_recognition()
# initial,destination=input.split('to')
# initial='entrance'
# destination=input("enter the destination:")
# initial,destination=frequencyanalyser(initial,destination)
# print(initial)
# print(destination)
initial='entrance'
destination='bramha putra hostel'
path=dijstras(open,path,visited,initial)
for i in path:
    print(i)
path,cost,totalcost=pathfinder(path,destination)
str=stringmaker(path,cost,totalcost) 
textToSpeech(str)
