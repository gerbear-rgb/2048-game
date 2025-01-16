import random

#used to make the control printing easier
def print_function(control1, control2, direction):
    print('Use {} or {} to move {}'.format(control1, control2, direction))
    
def start_game():
    #makes the basic board layout
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    #print the controls for the user
    print('Controls are as follows:')
    print_function('W', 'w', 'Up')
    print_function('S', 's', 'Down')
    print_function('A', 'a', 'Left')
    print_function('D', 'd', 'Right')
    
    #calls a function defined in a later part of the code 
    add_new_2(mat)
    return mat
    
#function to add a new 2 to a random empty block every return
def add_new_2(mat):
    #makes the code pick a point at random
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    
    #checks that the spot chosen is 0 and if it isn't it picks a new spot
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
     
    #changes the spot to a two
    mat[r][c] = 2 
        
#checks if the game is lost or won
def get_current_state(mat):
    #the game works that if any cell in the grid has 2048 you win 
    #if you can't do any more moves then you lose
    
    #checks if the game is won 
    for i in range(0, 3):
        for j in range(0, 3):
            if mat[i][j] == 2048:
                return 'WON'
               
    #checks that the game isn't over           
    for i in range(0, 3):
        for j in range(0, 3):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    
    #continues checking if the game is not over 
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
    for i in range(3):
        if mat[3][i] == mat[3][i + 1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'
            
    #check that the game is over
    return 'GAME OVER'
    
#function to compress the grid before and after merging cells
def compress(mat):
    
    #variable to determine if a change has happened or not 
    changed = False
    
    #empty grid with empty cells
    new_mat = [[0] * 4 for i in range(4)]
    
    #shift entries to their extreme row by row
    #loop to traverse rows
    for i in range(4):
        pos = 0
        
        #loop to traverse collumn in each row
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    #changes the changed var to true 
                    changed = True
            #increases the pos by 1 
                pos += 1 
            
    #returning the new mat and the flag var
    return new_mat, changed
    
#function to merge cells after compressing
def merge(mat):
    
    changed = False
    
    #loop to go through each cell and the one next to it 
    for i in range(4):
        for j in range(3):
            
            #if the current cell has the same value and the next one and they are not 0 then it merges them
            if mat[i][j] == mat[i][j + 1] and not mat[i][j] == 0:
                
                #double the current value and get rid of one 
                mat[i][j] = mat[i][j] * 2 
                mat[i][j + 1] = 0 
                #change the var to true 
                changed = True 
    return mat, changed
    
#function to reverse the board by taking each index and putting it at the opposite end 
def reverse(mat):
    #makes a new board to return once the changes are made
    new_mat = []
    for i in range(4):
        new_mat.append([])
        #reverses new_mat
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    #returns new_mat
    return new_mat

#function to get the transpose of matrix (interchanging rows and collumns)

def transpose(mat):
    new_mat = []
    
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
    
#function to move Left
def move_left(grid):
    
    #first compress the grid
    new_grid, changed1 = compress(grid)
    
    #next merge the cells
    new_grid, changed2 = merge(new_grid)
    changed = changed1
    #compress again after merging
    new_grid, temp = compress(new_grid)
    
    #return the grid and the changed var
    return new_grid, changed

#function to move Right
def move_right(grid):
    
    #first reverse the grid
    new_grid = reverse(grid)
    
    #then move left since the grid is reversed
    new_grid, changed = move_left(new_grid)
    
    #then reverse again so that its moved Right
    new_grid = reverse(new_grid)
    return new_grid, changed
    
    
#function to move Up
def move_up(grid):
    #to move up just take the transpose of the grid and move left
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    
    #transpose again so that its oriented right way
    new_grid = transpose(new_grid)
    return new_grid, changed

#function to move Down
def move_down(grid):
    #pretty much the same as for up just you do right instead of left
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

#thats all the logic in the file we then use this to put the game together in 2048.py file