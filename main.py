import os
import time

symb = {
    1:'O',
    -1:'X',
    0:'_'
}

def setup():
    mat = []
    for _ in range(7):
        name = [0]*7
        mat.append(name)

    return mat

def visual(mat:list):
    print('   ',end = '')

    for n in range(7):
        print(f'[{n}]',end = '')
    print('')

    for index in [5,4,3,2,1,0]:
        print(f'{[index]}',end='')  
        for ll in mat:
            print(f' {symb[ll[index]]} ',end = '')
        print('')

def animate(mat, num, player):
    count = 5
    while(count != mat[num][6]):
        os.system('cls')
        
        print('   ',end = '')
        for n in range(7):
            print(f'[{n}]',end = '')
        print('')
        for index in [5,4,3,2,1,0]:
            print(f'{[index]}',end='')  
            for col in range(7):
                if(index == count and col == num):
                    print(f' {symb[player]} ',end = '')
                else:
                    print(f' {symb[mat[col][index]]} ',end = '')
            print('')
        count = count-1
        time.sleep(0.05)
        

    print('   ',end = '')

    for n in range(7):
        print(f'[{n}]',end = '')
    print('')

    for index in [5,4,3,2,1,0]:
        print(f'{[index]}',end='')  
        for ll in mat:
            print(f' {symb[ll[index]]} ',end = '')
        print('')
    

def check_dir(x,y,player,mat,col,row):
    if(col+x > 6 or (col+x) < 0 or (row+y) < 0 or row+y >5 or mat[col+x][row+y]*player <=0):
        count = 0
        return count
    
    if(mat[col+x][row+y]==player):
        count = 1
    return count+check_dir(x,y,player,mat,col+x,row+y)

def check(mat,num,player):
    h = check_dir(1,0,player,mat,num,mat[num][6]-1)+check_dir(-1,0,player,mat,num,mat[num][6]-1)
    v = check_dir(0,1,player,mat,num,mat[num][6]-1)+check_dir(0,-1,player,mat,num,mat[num][6]-1)
    dl = check_dir(-1,1,player,mat,num,mat[num][6]-1)+check_dir(1,-1,player,mat,num,mat[num][6]-1)
    dr = check_dir(1,1,player,mat,num,mat[num][6]-1)+check_dir(-1,-1,player,mat,num,mat[num][6]-1)
    if(h >= 3 or v >= 3 or dl >=3 or dr >= 3):
        return player
    else:
        return 0

if __name__ == '__main__':
    W = 0
    
    os.system('cls')

    mat = setup()
    player = -1

    while(W == 0):
        player = -player
        visual(mat)
        print('TYPE "end" TO END THIS GAME')
        num = input(f'player {symb[player]} input column number . . . ')
        
        if(num == 'end'):
            break

        try:
            num = int(num)
        except ValueError:
            print(f"That's not an int!")
            continue
        if(num >=7 or mat[num][6]>5):
            print(f"Wrong number!")
            continue
        
        animate(mat, num, player)

        mat[num][mat[num][6]] = player
        mat[num][6] = mat[num][6]+1

        W = check(mat,num,player)
        os.system('cls')
    
    os.system('cls')
    visual(mat)
    print(f'PLAYER {symb[player]} WIN')