def main():
    
    grid = [[1,2,3,4,5],
            [3,3,4,5,6],
            [4,4,5,6,7],
            [5,5,6,7,0],
            [6,6,7,0,9]]
    transpose(grid)
    print(grid)

def transpose(grid):
    
    z = []

    for i in range(5):
        y = []
        for j in range(5):

            y.append(grid[j][i])
        
        z.append(y)
    print(z)

    return z

if __name__ == "__main__":
    main()