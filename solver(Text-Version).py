board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#fourth fun
#The algo part to solve the sudoku using recursion and backtraking

def solve(bo):
    find=find_empty(bo);
    if(not find):
        return True;
    else:
        row,col=find;

    for i in range(1,10):
        if(valid(bo,i,(row,col))):
            bo[row][col]=i;

            if(solve(bo)):
                return True;
            bo[row][col]=0;
    return False;

#third fun
#check if board is valid or not.checking all the three rules of sudoku. 
def valid(bo,num,pos): #pos is tuple (row,col) and num is the input user is filling
    
    #check row
    for i in range(len(bo[0])):                   #pos[0] means current row no. || bo[pos[0]][i]=bo[row][i]
        if((bo[pos[0]][i]==num) and (pos[1]!=i)): #(pos[1]!=i) means we wont check the postion we just inserted. 
            return False;                       #this loop is checking if the number inserted is present in that row or not
                                                      
    #check column
    for i in range(len(bo)):                    #pos[1] means current column no. || bo[i][pos[1]]=bo[i][column]
        if((bo[i][pos[1]]==num) and pos[0]!=i): #(pos[1]!=i) means we wont check the postion we just inserted. 
            return False;                    #this loop is checking if the number inserted is present in that column or not
    
    #check box
    box_x=pos[1]//3;  #we are naming all the the 9 boxes
    box_y=pos[0]//3;  # [00 , 01 ,02], [10,11,12], [20,21,22]

    #since we know the current box number, we will loop in each box checking all 9 elements if they aren't same

    for i in range(box_y*3,box_y*3+3):      #box_y*3 is starting index to start with 0,0 element in that box.
        for j in range(box_x*3,box_x*3+3):  #since loop ends one step back we will complte only 2 col,
            if(bo[i][j] == num and (i,j)!=pos):#thats why loops end is box_y*3+3 to include the last col
                return False;
    
    return True; #if true all the sudoku rule is valid. and num can be inserted at that postion

#first fun
#print board
def print_board(bo):
    for i in range(len(bo)):
        if ((i%3==0) and i!=0): #row printing
            print("- - - - - - - - - - - - - ");
        for j in range(len(bo[0])): #col printing
            if ((j%3==0) and j!=0):
                print(" | ",end="");

            if(j==8):
                print(bo[i][j]); #for new line
            else:
                print(str(bo[i][j])+" ",end="");
        
#This function Prints the Sudoku board
#print_board(board); 


#second fun
#find empty cell in sudoku(here empty cell is zero)
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(bo[i][j]==0):
                return (i,j); # returning tuple
                              # returning (row,col)
    return None;

#main function
#calling all functions

print_board(board);
solve(board);
print("_______________________________");
print_board(board);