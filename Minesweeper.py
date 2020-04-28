from random import randint

def Minesweeper(size_X = 15, size_Y = 10, mines = 10):
    Discord_dictionary = [':zero:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:']
    
    EmptySign = "||:zero:||"
    Mine = "||:bomb:||"
    Grid = []

    if size_X * size_Y < mines * 4:
        mines = (size_X * size_Y) /4

    if size_X * size_Y > mines * 7:
         mines = (size_X * size_Y) /6
    
    #Seting mines
    MinesList = []
    mi = 1
    while mi <= mines:
        MineList_a = [randint(0,size_Y-1), randint(0,size_X-1)]
        if not MineList_a in MinesList:
            MinesList.append(MineList_a)
            #Grid[MineList_a[0]][MineList_a[1]] = Mine
            mi += 1

    #Field
    for Y in range(size_Y):
        row = []
        #print(MinesList)
        for X in range(size_X):
            number = 0
            for XB in range(-1,2):
                for YB in range(-1,2):
                    #print("{0} {1}".format(Y + YB, X + XB))
                    if [Y, X] in MinesList:
                        number = -10
                    elif [Y + YB, X + XB] in MinesList:
                        number += 1
            if number < 0:
                row.append(Mine)
            if number == 0:
                row.append(EmptySign)
            if number > 0:
                row.append("||{0}||".format(Discord_dictionary[number]))
                
        Grid.append(row)

    

    
    
            

    #Printout
    Line = "Size: {0} x {1} \nMines: {2}\n".format(size_X,size_Y,len(MinesList))
    for Y in range(size_Y):
        for X in range(size_X):
            Line = Line + Grid[Y][X]
        Line = Line + '\n'
    print(Line)
    return Line

    




