N_squares,N_coins=map(int,input().split())
chess_board=[]
for _ in range(N_squares):
    chess=[0]*N_squares
    chess_board.append(chess)
for _ in range(N_coins):
    coins1,coins2=map(int,input().split())
    chess_board[coins1][coins2]=1
out=0
store=[]
for i in range(N_squares):
    row=0
    col=i
    while(col>=0):
        if(chess_board[row][col]==1):
            store.append(1)
        col=col-1
        row=row+1
    out=out+(len(store)*(len(store)-1))//2
    store=[]
for i in range(1,N_squares):
    row=i
    col=N_squares-1
    while(row<N_squares):
        if(chess_board[row][col]==1):
            store.append(1)
        col=col-1
        row=row+1
    out = out + (len(store) * (len(store) - 1)) // 2
    store = []
for i in range(N_squares):
    row=i
    col=N_squares-1
    while(row>=0):
        if (chess_board[row][col] == 1):
            store.append(1)
        row=row-1
        col=col-1
    out = out + (len(store) * (len(store) - 1)) // 2
    store = []
for i in range(1,N_squares):
    row=i
    col=0
    while(row<=N_squares-1):
        if (chess_board[row][col] == 1):
            store.append(1)
        row=row+1
        col=col+1
    out = out + (len(store) * (len(store) - 1)) // 2
    store = []
print(out)

