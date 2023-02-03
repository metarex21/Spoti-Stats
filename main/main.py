#libraries and modules
import json
from collections import Counter

#user-defined functions
def top(lis,x):
    new=sorted(range(len(lis)), key=lambda i: lis[i])[-x:]  #returns list of index of top 'x' 
    return new    

def ms2m(ms):
    return ms//60000

#importing the JSON
with open(r"D:\...Personal Data\Spotify streaming history\MyData\TotalStreamingHistory.json", encoding="utf8") as f:
    data= json.load(f)

#variables
ms=0
arts=[]
trks=[]
msln=[]
link=[]
tlen=[]
link_dict={}

#extracting data
for i in range(len(data)):
    a=data[i]['artistName']
    b=data[i]['trackName']
    c=data[i]['msPlayed'] 
    link_dict[b]=a
    arts.append(a)                      #extracts all artists that have been streamed (duplicates exists. stores in list)
    trks.append(b)                      #extracts all tracks that have been streamed  (duplicates exists. stores in list)
    msln.append(c)                     
    # link.append([b,a])                #extracts all track-artist pairs in [<track>,<artist>] format
    # tlen.append([b,data[i]['msPlayed']]) #extracts all track-length pairs in [<track>,<length>] format
    ms+=data[i]['msPlayed']             #extracts total ms of track streamed

#artists
dict_art=Counter(arts)
uarts=list(dict_art.keys())             #list of all unique artists
uartno=list(dict_art.values())          #list of no. of plays




#tracks
dict_trk=Counter(trks)
utrks=list(dict_trk.keys())             #list of all unique tracks
utrkno=list(dict_trk.values())          #list of no. of plays



#mod1
atot=[0]*len(uarts)                     #list of miliseconds streamed
ttot=[0]*len(utrks)
for i in range(len(trks)):
    track,artist,length=trks[i],arts[i],msln[i]
    aloc=uarts.index(artist)
    atot[aloc]+=length
    tloc=utrks.index(track)
    ttot[tloc]+=length
    






#__main__
mins=ms2m(ms)
hours= mins//60
rmin=mins%60
print("\n--------------------------------------------------------------------------------------\nMinutes played:",ms2m(ms),"Minutes\nor\nHours played:",hours,"Hours",rmin,"Minutes\n--------------------------------------------------------------------------------------")
print('Number of Unique Tracks Streamed:', len(utrks))
print('\nNumber of Unique Artists Streamed:', len(uarts))
#top artists
x=int(input("Enter no. of top artists you wanna see:(by no. of streams)"))
print("\n--------------------------------------------------------------------------------------\nTop Artists(by no. of streams):\n--------------------------------------------------------------------------------------\n")
c=1
for i in top(uartno,x)[::-1]:
    print(c,". Artist: ",uarts[i]," || Tracks Streamed: ",uartno[i],' Streams\n',sep=''); c+=1


#top artists by no. of minutes streamed
z=int(input("enter no. of top artists you wanna see:(by no. minutes of streamed)"))
print("\n--------------------------------------------------------------------------------------\nTop Artists(by no. minutes of streamed):\n--------------------------------------------------------------------------------------\n")
c=1
for i in top(atot,z)[::-1]:
    print(c,". Artist: ",uarts[i]," || Minutes Streamed: ",ms2m(atot[i]),' Minutes\n',sep=''); c+=1


#top tracks by no. of times streamed
y=int(input("enter no. of top tracks you wanna see:(by no. of streams)"))
print("\n--------------------------------------------------------------------------------------\nTop tracks:(by no. of streams)\n--------------------------------------------------------------------------------------\n")
c=1
for i in top(utrkno,y)[::-1]:
    artc=link_dict[utrks[i]]
    print(c,". Track: ",utrks[i],"|| Artist: ",artc," || No. of time Streamed: ",utrkno[i],' Streams\n',sep=''); c+=1


#top tracks by no. of minutes streamed
y=int(input("enter no. of top tracks you wanna see:(by no. of streams)"))
print("\n--------------------------------------------------------------------------------------\nTop tracks(by no. minutes of streamed):\n--------------------------------------------------------------------------------------\n")
c=1
for i in top(utrkno,y)[::-1]:
    artc=link_dict[utrks[i]]
    print(c,". Track: ",utrks[i],"|| Artist: ",artc," || Minutes Streamed: ",ms2m(ttot[i]),' Minutes\n',sep=''); c+=1

