# Function to turn a string of numbers into an array
# Upper limit of 9999
def strToList(stringOfInts):
    # Converts string into an array
    numsRaw = []
    for i in stringOfInts:
        numsRaw.append(i)

    # Will be added to with numbers
    numsFinal = []

    # Iterations to skip so not to repeat numbers
    wait = 0

    
    for i in range(len(numsRaw) - 1):
        if numsRaw[i] == ' ':
            continue
        elif wait > 0:
            wait -= 1
            continue

        # Gets full length of number
        if numsRaw[i + 1] == ' ' or numsRaw[i + 1] == '\n':
            numsFinal.append(int(numsRaw[i]))
            i += 1
        elif numsRaw[i + 2] == ' 'or numsRaw[i + 2] == '\n':
            numsFinal.append(int(numsRaw[i] + numsRaw[i + 1]))
            wait = 1
        elif numsRaw[i + 3] == ' ' or numsRaw[i + 3] == '\n':
            numsFinal.append(int(numsRaw[i] + numsRaw[i + 1] + numsRaw[i + 2]))
            wait = 2
        elif numsRaw[i + 4] == ' ' or numsRaw[i + 4] == '\n':
            numsFinal.append(int(numsRaw[i] + numsRaw[i + 1] + numsRaw[i + 2] + numsRaw[i + 3]))
            wait = 3
            
    return numsFinal

lis = "1 2 3 333 22 456 653 22 -4\n"
print(strToList(lis))
