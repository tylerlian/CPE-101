def validate_row(grid):
    for i in range (len(grid)):
        tf_list=[]
        x=len(grid)
        if grid[i]!=0:
            while x>0:
                tf_list.append(bool(grid[i]!=grid[x-1]))
                x=x-1
        if tf_list.count(False)>1:
            return False
    return True

def validate_rows(grid):
    tf_list=[]
    grid_copy=list(grid)
    while len(grid_copy)>0:
        row=[grid_copy.pop(0),grid_copy.pop(0),grid_copy.pop(0),grid_copy.pop(0),grid_copy.pop(0)]                                           
        tf_list.append(validate_row(row))
    if tf_list.count(False)!=0:
        return False
    else:
        return True

def validate_cols(grid):
    column_grid=[grid[0],grid[5],grid[10],grid[15],grid[20],\
    grid[1],grid[6],grid[11],grid[16],grid[21],\
    grid[2],grid[7],grid[12],grid[17],grid[22],\
    grid[3],grid[8],grid[13],grid[18],grid[23],\
    grid[4],grid[9],grid[14],grid[19],grid[24]]
    return validate_rows(column_grid)

def validate_cage(grid,cage):
    cage_sum=int(cage[0])
    cage_n_of_cells=int(cage[1])
    x=0
    empty_cells=0
    for i in range(2,len(cage)):
        grid_pos=int(cage[i])
        if grid[grid_pos]!=0:
            x+=grid[grid_pos]
        else:
            empty_cells+=1
    if cage_n_of_cells>len(cage[2: ]):
        if x<cage_sum:
            return True
        else:
            return False
    if empty_cells!=0:
        if x<cage_sum:
            return True
        else:
            return False
    else:
        if x==cage_sum:
            return True
        else:
            return False
            
def validate_cages(grid,cages):
    bool_list=[]
    for i in range (len(cages)):
        cage=[]
        cages_i_string=cages[i]
        while 0<cages_i_string.count(' '):
            z=cages_i_string.find(' ')
            cage.append(cages_i_string[ :z])
            cages_i_string=cages_i_string[z+1: ]
            if cages_i_string.count(' ')==0:
                cage.append(cages_i_string)
        bool_list.append(validate_cage(grid,cage))
    if bool_list.count(True)==len(cages):
        return True
    else:
        return False

def validate_all(grid,cages):
    if validate_rows(grid)==True and validate_cols(grid)==True\
    and validate_cages(grid,cages)==True:
        return True
    else:
        return False

def main():
    cage_count=int(input())
    cages=[]
    x=0
    grid=[]
    while x<cage_count:
        cages.append(input())
        x+=1
    x=0
    while x<25:
        grid.append(0)
        x+=1
    x=0
    while x<len(grid):
        grid[x]+=1
        while validate_all(grid,cages)!=True:
            grid[x]+=1
            if grid[x]>5:
                grid[x]=0
                x=x-2
                break
        x+=1   
    print (grid[0],' ',grid[1],' ',grid[2],' ',grid[3],' ',grid[4])
    print (grid[5],' ',grid[6],' ',grid[7],' ',grid[8],' ',grid[9])
    print (grid[10],' ',grid[11],' ',grid[12],' ',grid[13],' ',grid[14])
    print (grid[15],' ',grid[16],' ',grid[17],' ',grid[18],' ',grid[19])
    print (grid[20],' ',grid[21],' ',grid[22],' ',grid[23],' ',grid[24])

if __name__ == '__main__':
    main()