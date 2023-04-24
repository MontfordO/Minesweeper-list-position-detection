# Creating 'minesweeper_grid' list
# The size of the grid is determined by user input

number_check = False
while number_check is False :
    try :
        grid_size = int(input("How many squares would you like your grid? : "))
    except ValueError :
        print("The input is not a number.")
        print("------------------------------")
    else :
        number_check = True

if grid_size < 4 or grid_size > 30 :
    grid_size_check = False
else :
    grid_size_check = True

while grid_size_check == False :
    if grid_size < 4 :
        print("------------------------------")
        print("The grid size you have selected is too small. Please choose a grid size between 4 and 30")
        try :
            grid_size = int(input("How many squares would you like your grid? : "))
        except ValueError :
            print("The input is not a number.")
            print("------------------------------")
        else :
            number_check = True
    elif grid_size > 30 :
        print("------------------------------")
        print("The grid size you have selected is too big. Please choose a grid size between 4 and 30")
        try :
            grid_size = int(input("How many squares would you like your grid? : "))
        except ValueError :
            print("The input is not a number.")
            print("------------------------------")
        else :
            number_check = True
    else : 
        grid_size_check = False
        break

# Using the 'grid_size' variable, the grid is made by using a for loop to create a row for the number in 'grid_size'
# Alongside a column for the identical 'grid_size' variable
# This means the grid will always be square (equal sides) 
# However, it would be easy to take two variables instead, creating a rectangular grid

minesweeper_grid = [["x"] * grid_size for _ in range(grid_size)]

# To determine which of the items in the grid are mines, I use the random.randint() in the random module
# As a base range, I used (0,2) giving 3 different number options
# I then use a for loop with enumerate to run this randomizer for every item in the list
# If the number is 0, the item will be a mine ('#'). This means the mines will generate at a 1/3 chance. Anything else is set to '-'
# This loop could take a variable to be used in the random.randint() function, in order to make the mines more or less common
# I found information on this function and the random module here:
# https://www.programiz.com/python-programming/examples/random-number

import random
for count_row, row in enumerate(minesweeper_grid, start=0):
    for count_col, value in enumerate(row, start=0):
        random_number = random.randint(0,2)
        if random_number == 0 :
            minesweeper_grid[count_row][count_col] = "#"
        else :
            minesweeper_grid[count_row][count_col] = "-"

# The 'minesweeper_grid' list printed to the user without the numbers
# As the grid size is chosen by the user, the grid can be presented with versality in a for loop with enumerate
# I also used the .join and map() functions with str() to present the grid in a presentable fashion
# I found the information on how to do this on this website:
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.

print("------------------------------------------------------------")
print("The starting grid for this Minesweeper session is: ")
for count_row, row in enumerate(minesweeper_grid, start=0):
    print("  ".join(map(str,minesweeper_grid[count_row])))

#############################

# These functions are used through each item that is '#'
# They will check the relevant adjacent positions to the mine
# Using a set of if/elif statements, the value in the designated spot is changed accordingly
# If the adjacent spot is set as '-', it cannot have a number added as it is a string and is also technically 0, so it's set to 1
# If the adjacent spot is set as '#', it shouldn't be changed to anything as it is a mine, so this is passed
# If the adjacent spot is anything else, which in this case, would be a number, 1 is added to the current value
# Once this has been determined and the relevant position has been changed, it is returned as the new value of that postion

def nw_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row-1][count_col-1] == "-" :
        minesweeper_grid[count_row-1][count_col-1] = 1
    elif minesweeper_grid[count_row-1][count_col-1] == "#" :
        pass
    else :
        minesweeper_grid[count_row-1][count_col-1] += 1
    return minesweeper_grid[count_row-1][count_col-1]
def n_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row-1][count_col] == "-" :
        minesweeper_grid[count_row-1][count_col] = 1
    elif minesweeper_grid[count_row-1][count_col] == "#" :
        pass
    else :
        minesweeper_grid[count_row-1][count_col] += 1
    return minesweeper_grid[count_row-1][count_col]
def ne_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row-1][count_col+1] == "-" :
        minesweeper_grid[count_row-1][count_col+1] = 1
    elif minesweeper_grid[count_row-1][count_col+1] == "#" :
        pass
    else :
        minesweeper_grid[count_row-1][count_col+1] += 1
    return minesweeper_grid[count_row-1][count_col+1]
def w_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row][count_col-1] == "-" :
        minesweeper_grid[count_row][count_col-1] = 1
    elif minesweeper_grid[count_row][count_col-1] == "#" :
        pass
    else :
        minesweeper_grid[count_row][count_col-1] += 1
    return minesweeper_grid[count_row][count_col-1]
def e_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row][count_col+1] == "-" :
        minesweeper_grid[count_row][count_col+1] = 1
    elif minesweeper_grid[count_row][count_col+1] == "#" :
        pass
    else :
        minesweeper_grid[count_row][count_col+1] += 1
    return minesweeper_grid[count_row][count_col+1]
def sw_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row+1][count_col-1] == "-" :
        minesweeper_grid[count_row+1][count_col-1] = 1
    elif minesweeper_grid[count_row+1][count_col-1] == "#" :
        pass
    else :
        minesweeper_grid[count_row+1][count_col-1] += 1
    return minesweeper_grid[count_row+1][count_col-1]
def s_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row+1][count_col] == "-" :
        minesweeper_grid[count_row+1][count_col] = 1
    elif minesweeper_grid[count_row+1][count_col] == "#" :
        pass
    else :
        minesweeper_grid[count_row+1][count_col] += 1
    return minesweeper_grid[count_row+1][count_col]
def se_pos_add(minesweeper_grid,count_col,count_row) :
    if minesweeper_grid[count_row+1][count_col+1] == "-" :
        minesweeper_grid[count_row+1][count_col+1] = 1
    elif minesweeper_grid[count_row+1][count_col+1] == "#" :
        pass
    else :
        minesweeper_grid[count_row+1][count_col+1] += 1
    return minesweeper_grid[count_row+1][count_col+1]

# A for loop is run through the 'minesweeper_grid' list variable
# The first for loop runs through the items in 'minesweeper_grid' (rows)
# Then the nested for loop runs through the items in each 'minesweeper_grid' list item (columns)
# As each item in the grid is checked, the following is carried out:

for count_row, row in enumerate(minesweeper_grid, start=0):
    for count_col, value in enumerate(row, start=0):
        # If the value is '-', the string is turned into an int with a value of zero   
        # This is more of a failsafe for if not every item is not adjacent to a mine, which is very likely the case
        # It means there will be no values left as '-', once the for loop is complete
        if value == "-" :
            minesweeper_grid[count_row][count_col] = 0
        # If the value is '#', all adjacent positions are added to by 1
        # This is done through the _pos_add functions explained above
        # In order to not increase the values of any indexes outside the grid, 
        # if statements are run using the current count_row and count_col values
        # These may be viewed in some sense as 1 below or 1 above the min and max index values of each row and column
        # The if statements are run 8 times (for each adjacent position)
        # If the if statement proves that the position being checked is outside the bounds of the grid, 
        # the addition to the value is passed
        # In the case that the position being checked is within the bounds, 
        # the position will then be adjusted using the relevant directional function
        elif value == "#" :

            if (count_row-1) < 0 or (count_col-1) < 0 :
                pass
            else :
                minesweeper_grid[count_row-1][count_col-1] = nw_pos_add(minesweeper_grid,count_col,count_row)
                
            if (count_row-1) < 0 :
                pass
            else :
                minesweeper_grid[count_row-1][count_col] = n_pos_add(minesweeper_grid,count_col,count_row)

            if (count_row-1) < 0 or (count_col+1) > (grid_size-1) :
                pass
            else :
                minesweeper_grid[count_row-1][count_col+1] = ne_pos_add(minesweeper_grid,count_col,count_row)

            if (count_col-1) < 0 :
                pass
            else :
                minesweeper_grid[count_row][count_col-1] = w_pos_add(minesweeper_grid,count_col,count_row)

            if (count_col+1) > (grid_size-1) :
                pass
            else :
                minesweeper_grid[count_row][count_col+1] = e_pos_add(minesweeper_grid,count_col,count_row)
            
            if (count_row+1) > (grid_size-1) or (count_col-1) < 0 :
                pass
            else :
                minesweeper_grid[count_row+1][count_col-1] = sw_pos_add(minesweeper_grid,count_col,count_row)

            if (count_row+1) > (grid_size-1) :
                pass
            else :
                minesweeper_grid[count_row+1][count_col] = s_pos_add(minesweeper_grid,count_col,count_row)

            if (count_row+1) > (grid_size-1) or (count_col+1) > (grid_size-1) :
                pass
            else :
                minesweeper_grid[count_row+1][count_col+1] = se_pos_add(minesweeper_grid,count_col,count_row)
        # If the value is neither '-' or '#', meaning it's a number, no checks or changes need to be made
        # This position is passed
        else :
            pass

# As shown previously, the grid is printed again
# It now has the items set as numbers to represent the positions of the mines

print("------------------------------------------------------------")
print("The Minesweeper grid with numbers revealed: ")
for count_row, row in enumerate(minesweeper_grid, start=0):
    print("  ".join(map(str,minesweeper_grid[count_row])))

#############################

# Although the grid size adjustment and mine position randomizer weren't necessary to the task
# I felt that adding these was important for me to understand how to use 2D lists with versatility