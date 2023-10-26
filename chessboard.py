#Chess
def create_chessboard():
    chess_board = []

    row_1 =["Br","Bk","Bb","Bq","Bk","Bb","Bk","Br"]
    row_2 = ["Bp","Bp","Bp","Bp","Bp","Bp","Bp","Bp"]
    row_3 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row_4 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row_5 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row_6 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row_7 = ["Wp","Wp","Wp","Wp","Wp","Wp","Wp","Wp"]
    row_8 =["Wr","Wk","Wb","Wq","Wk","Wb","Wk","Wr"]

    chess_board.append(row_1)
    chess_board.append(row_2)
    chess_board.append(row_3)
    chess_board.append(row_4)
    chess_board.append(row_5)
    chess_board.append(row_6)
    chess_board.append(row_7)
    chess_board.append(row_8)
    return chess_board


def print_board (chess_board):
    print("  1  2  3  4  5  6  7  8")
    index=1
    for row in chess_board:
        print(str(index) + " ", end="")
        for piece in row:
            print(piece + " ", end="")
        print()
        index = index+1

def pawn_check_w(chess_board, current_row,current_col,new_row,new_col):
    current_piece = chess_board[current_row][current_col]
    if(current_row-1 == new_row) and (current_col+1 == new_col): 
        if(chess_board[new_row][new_col] )!= "":
           print("Piece captured: "+ chess_board[new_row][new_col])
           chess_board[new_row][new_col] = current_piece
           chess_board[current_row][current_col] = ""
        else:
            print("Illegal Move")
            return False
    elif current_col != new_col:
        print("Illegal Move 1")
        return False
    elif (new_row - current_row) != -1:
        print("Illegal Move 2")
        return False
    else:
        print("Piece Moved")
        chess_board[new_row][new_col] = current_piece
        chess_board[current_row][current_col] = "  "
        return chess_board
          
    
def move_piece(chess_board):
    current_row = int(input("Please enter the row number of the piece you would like to move:"))
    current_row = current_row-1
    current_col = int(input("Please enter the column number of the piece you would like to move:"))
    current_col = current_col-1
    
    new_row = int(input("Please enter the new row number you would like to move to:"))
    new_row = new_row - 1
    new_col = int(input("Please enter the new column number you would like to move to:"))
    new_col = new_col - 1

    if 'p' in chess_board[current_row][current_col]:

        if 'W' in chess_board[current_row][current_col]:
            new_board = pawn_check_w(chess_board,current_row,current_col,new_row,new_col)
            if new_board:
                chess_board = new_board
    return chess_board
                

current_board = create_chessboard()
game=True
while(game == True):
    print_board(current_board)
    current_board = move_piece(current_board)
    print_board(current_board)
    
