from random import randint as ran
from time import sleep

lookuptbl = [[1,2,3],
             [4,5,6],
             [7,8,9]]

gridvl    = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]



grid = """
-------
|"""+gridvl[1-1]+"""|"""+gridvl[2-1]+"""|"""+gridvl[3-1]+"""|
-------
|"""+gridvl[4-1]+"""|"""+gridvl[5-1]+"""|"""+gridvl[6-1]+"""|
-------
|"""+gridvl[7-1]+"""|"""+gridvl[8-1]+"""|"""+gridvl[9-1]+"""|
-------
"""

bot = input("Do you want to play against a computer (y/n): ")
if bot.lower() == "y" or bot.lower() == "yes":
    bot = True
else:
    bot = False

modetbl = []

if bot:
    modetbl = ["P", "C"]
else:
    modetbl  = ["X", "O"]

currmode = modetbl[ran(0,1)]

gridwintest = [[0,1,2],
               [3,4,5],
               [6,7,8],
               
               [0,3,6],
               [1,3,7],
               [2,5,8],
               
               [0,4,8],
               [2,4,6]
               ]

def check_grid(grid,check):
    global gridwintest
    for chkgrid in gridwintest:
        correct = True
        for index in chkgrid:
            if grid[index] == check:
                correct = correct and True
            else:
                correct = False
        if correct:
            break
        
    return correct
            
while True:
    retry = False
    grid = """
    -------
    |"""+gridvl[1-1]+"""|"""+gridvl[2-1]+"""|"""+gridvl[3-1]+"""|
    -------
    |"""+gridvl[4-1]+"""|"""+gridvl[5-1]+"""|"""+gridvl[6-1]+"""|
    -------
    |"""+gridvl[7-1]+"""|"""+gridvl[8-1]+"""|"""+gridvl[9-1]+"""|
    -------
    """
    
    print(grid)
    
    selectfield = input("Player "+currmode+",what field do you want to select? (Layout: 'row,column') ").split(",")
    if len(selectfield) != 2:
        print("The input specified contains more/less than 2 dimensions")
        retry = True
        sleep(2)
        
    
    if gridvl[lookuptbl[int(selectfield[0])-1][int(selectfield[1])-1]-1] == " ":
        gridvl[lookuptbl[int(selectfield[0])-1][int(selectfield[1])-1]-1] = currmode
    else:
        retry = True
    
    invcurrmode = ""
    if currmode == modetbl[0]:
        invcurrmode = modetbl[1]
    elif currmode == modetbl[1]:
        invcurrmode = modetbl[0]
    
    if check_grid(gridvl, currmode):
        print("You won, "+currmode+"!")
        quit()
    elif check_grid(gridvl, invcurrmode):
        print("Try again, "+currmode+".")
        quit()

    
    if not retry:
        currmode = invcurrmode
    
    