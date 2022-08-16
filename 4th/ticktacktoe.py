l = ['*']*9
def display():
    for i in range(len(l)):
        if i%3==0:
            print()
        print(l[i],end="\t")
    print()

def getinput(player):
    print("{} SHOW TIME".format(player))
    pos = int(input("Enter pos = "))
    while pos<1 or pos>9 or l[pos-1]!='*':
        pos = int(input("Re-enter pos = "))
    l[pos-1] = players[player]

def check(player):
    win=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in win:
        if l[x[0]]==l[x[1]]==l[x[2]]==players[player]:
            return player
    else:
        return False

display()
players = {'Player1':'X','Player2':'O'}
moves = 1
while moves<10:
    if moves%2==1:
        player = 'Player1'
        getinput(player)
    else:
        player = 'Player2'
        getinput(player)
    display()
    if moves>=5:
        if(check(player)):
            print("We got a winner {} = {} ".format(player,players[player]))
            break
    moves +=1
else:
    print("Match draw")