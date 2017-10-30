str = input('Please enter a phone number in letters: (AAA-BBB-CCCC): ')
print(str)
str = str.upper()
# this loop will go through all of the letters in str and then the if statements will check if a letter is present in that spot and replacing it with the right number
for i in range(0, len(str)):
    if 'A' in str:
        str = str.replace('A', '2', i)
    if 'B' in str:
        str = str.replace('B', '2', i)
    if 'C' in str:
        str = str.replace('C', '2', i)
    if 'D' in str:
        str = str.replace('D', '3', i)
    if 'E' in str:
        str = str.replace('E', '3', i)
    if 'F' in str:
        str = str.replace('F', '3', i)
    if 'G' in str:
        str = str.replace('G', '4', i)
    if 'H' in str:
        str = str.replace('H', '4', i)
    if 'I' in str:
        str = str.replace('I', '4', i)
    if 'J' in str:
        str = str.replace('J', '5', i)
    if 'K' in str:
        str = str.replace('K', '5', i)
    if 'L' in str:
        str = str.replace('L', '5', i)
    if 'M' in str:
        str = str.replace('M', '6', i)
    if 'N' in str:
        str = str.replace('N', '6', i)
    if 'O' in str:
        str = str.replace('O', '6', i)
    if 'P' in str:
        str = str.replace('P', '7', i)
    if 'Q' in str:
        str = str.replace('Q', '7', i)
    if 'R' in str:
        str = str.replace('R', '7', i)
    if 'S' in str:
        str = str.replace('S', '7', i)
    if 'T' in str:
        str = str.replace('T', '8', i)
    if 'U' in str:
        str = str.replace('U', '8', i)
    if 'V' in str:
        str = str.replace('V', '8', i)
    if 'W' in str:
        str = str.replace('W', '9', i)
    if 'X' in str:
        str = str.replace('X', '9', i)
    if 'Y' in str:
        str = str.replace('Y', '9', i)
    if 'Z' in str:
        str = str.replace('Z', '9', i)

print(str)
