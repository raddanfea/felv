from math import ceil, floor

word = "aple"
length = len(word)


for row in range(5):
    for col in range(2*length+length//2+1):
        if row + col == 5 or row - col == -1 or col - row == length+2 or row + col == length+6:
            print("*", end='\t')

        elif row == 0 and col == length+1:
            print("*", end='\t')
        elif row == 4 and col == length+1:
            print("*", end='\t')
        elif (row, col) in ((0, 0), (length-1,0),(0,length*2+2), (4, 2*length+2)):
            print("*", end='\t')
        elif row == 2 and 4+length >= col >= 4:
            print(word[col - 4], end='\t')
        else:
            print(".", end='\t')
    print("")