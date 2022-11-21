def generateArray(height, width, type='integer'):
    output = []
    count = 0
    for i in range(height):
        row = []
        for j in range(width):
            if type == 'letter':
                row.append(chr(ord('a') + count))
            elif type == 'integer':
                row.append(count)
            count += 1
        output.append(row)
    return output

def pretty(arr):
    for row in arr:
        for col in row:
            print(str(col).rjust(4), end=' ')
        print()

def rotateArray(arr, step):

    output = arr.copy()

    height = len(arr)
    width = len(arr[0])
    iter = min(height, width) // 2
    for x in range(iter):
        slice = []
        for i in range(x, width - 1 - x):
            slice.append(arr[x][i] )

        for i in range(x, height - 1 - x):
            slice.append(arr[i][-1 - x])
        
        for i in range(x, width-1 -x):
            slice.append(arr[-1-x][-1-i])
        
        for i in range(x, height - 1 - x):
            slice.append(arr[-1-i][x])


        slice = slice[step:] + slice[:step]

        counter = 0
        
        for i in range(x, width - 1 - x):
            output[x][i] = slice[counter]
            counter += 1

        for i in range(x, height - 1 - x):
            output[i][-1 - x] = slice [counter]
            counter += 1
        
        for i in range(x, width-1 -x):
            output[-1-x][-1-i] = slice[counter]
            counter += 1
        
        for i in range(x, height - 1 - x):
            output[-1-i][x] = slice[counter]
            counter += 1


    return output

letters = generateArray(4,5, 'letter')

pretty(letters)

print()
letters = rotateArray(letters, 3)
pretty (letters)