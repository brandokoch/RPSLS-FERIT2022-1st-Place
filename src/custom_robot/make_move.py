import random

def get_robot1_move(A,B,idx):

    if A[-1]==4:
        return 3
    elif A[-1]==2:
        return 2
    elif A[-1]==1:
        return 1
    else:
        return 5   

def get_robot2_move(A,B,idx):
    if A[-1]==-1:
        return 5
    else:
        return A[-1]

def get_robot3_move(A,B,idx):
    if A[-1]==-1:
        return 4
    if A[-1]==5:
        return 4
    else:
        return 5

def get_robot4_move(A,B,idx):

    if A[-1]==4:
        return 3
    elif A[-1]==2:
        return 5
    elif A[-1]==4:
        return 5
    else:
        return 4

def get_robot10_move(A,B,idx):
    if A[-1]==-1:
        return 2
    elif A[-1]==4:
        return 3
    elif A[-1]==2:
        return 5
    elif A[-1]==1:
        return 5
    else:
        return random.randint(1,5)

def get_robot11_move(A,B,idx):
    if A[-1]==-1:
        return 5

    if A[-1]==5:
        return 4

    if A[-1]==3:
        return 1

    if A[-1]==1:
        return 3

    if A[-1]==2:
        return 2

    if A[-1]==4:
        return 4

    return 5

def get_robot12_move(A,B,idx):
    return random.randint(1,5)

    
def get_robot13_move(A,B,idx):
    if len(A)==0 and len(B)==0:
        return 2
    
    if len(A)>10 and A[-3]==2:
        return 2
    
    if len(A)>30:
        return A[-1]
    
    if len(A)>3 and A[-2]==5:
        return 1
    
    return 5

def get_robot14_move(A,B,idx):
    if len(A)==0 and len(B)==0:
        return 2
    
    if len(A)>10 and A[-3]==2:
        return 2
    
    if len(A)>30:
        return A[-1]
    
    if len(A)>5 and A[-4]==5:
        return 1
    
    return 5

def get_robot15_move(A,B,idx):
    if len(A)<10:
        return 5
    else:
        return A[-3]

def get_robot16_move(A,B,idx):
    if len(A)<10:
        return 5


    if A[-1]==5 and A[-2]==5:
        return 4

    if A[-1]==3 and A[-2]==3:
        return 1

    if A[-1]==1:
        return 3

    if A[-1]==2:
        return 2

    if A[-1]==4:
        return 4

    return 5

def get_robot20_move(A,B,i):
    out=5
    if i%10==0: out=1
    if i%10==1: out=2
    if i%10==2: out=2
    if i%10==3: out=3
    if i%10==4: out= 4
    if A[-1]==5: out= 4
    return out

def get_robot21_move(A,B,i):
    out=5
    if i%10==0: out=2
    if i%10==1: out=2
    if i%3==2: out=5
    if i%10==3: out=2
    if i%10==4: out= 2
    if A[-1]==5: out= 4
    return out

def get_robot22_move(A,B,i):
    out=5
    if i%2==0: out=1
    if i%3==0: out=5
    if i%5==0: out=3
    if i%7==0: out=4
    if A[-1]==5: out= 4
    return out

def get_robot23_move(A,B,i):
    out=5
    if i%10==0: out=2
    if i%10==1: out=2
    if i%10==2: out=2
    if i%10==3: out=2
    if i%10==4: out= 2
    if A[-1]==5: out= 4
    return out

def get_robot24_move(A,B,i):
    if A[-1]==5: return 4
    if i%2==0: return 1
    if i%3==0: return 5
    if i%5==0: return 3
    if i%7==0: return 4

    return 5


robots={
    'robot1':get_robot1_move,
    'robot2':get_robot2_move,
    'robot3':get_robot3_move,
    'robot4':get_robot4_move,
    'robot10':get_robot10_move,
    'robot11':get_robot11_move,
    'robot12':get_robot12_move,
    'robot13':get_robot13_move,
    'robot14':get_robot14_move,
    'robot15':get_robot15_move,
    'robot16':get_robot16_move,
    'robot20':get_robot20_move,
    'robot21':get_robot21_move,
    'robot22':get_robot22_move,
    'robot23':get_robot23_move,
    'robot24':get_robot24_move,
}