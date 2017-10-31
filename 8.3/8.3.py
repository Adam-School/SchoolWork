def main():
    alpha = [None]*26
    for i in range(26):
        alpha[i] = 0
    str = input('Plase enter a string: ')
    print(str)
    str = str.upper()
    for i in range(0, len(str)):
        if str[i] == 'A':
            alpha[0] += 1
        elif str[i] == 'B':
            alpha[1] += 1
        elif str[i] == 'C':
            alpha[2] += 1
        elif str[i] == 'D':
            alpha[3] += 1
        elif str[i] == 'E':
            alpha[4] += 1
        elif str[i] == 'F':
            alpha[5] += 1
        elif str[i] == 'G':
            alpha[6] += 1
        elif str[i] == 'H':
            alpha[7] += 1
        elif str[i] == 'I':
            alpha[8] += 1
        elif str[i] == 'J':
            alpha[9] += 1
        elif str[i] == 'K':
            alpha[10] += 1
        elif str[i] == 'L':
            alpha[11] += 1
        elif str[i] == 'M':
            alpha[12] += 1
        elif str[i] == 'N':
            alpha[13] += 1
        elif str[i] == 'O':
            alpha[14] += 1
        elif str[i] == 'P':
            alpha[15] += 1
        elif str[i] == 'Q':
            alpha[16] += 1
        elif str[i] == 'R':
            alpha[17] += 1
        elif str[i] == 'S':
            alpha[18] += 1
        elif str[i] == 'T':
            alpha[19] += 1
        elif str[i] == 'U':
            alpha[20] += 1
        elif str[i] == 'V':
            alpha[21] += 1
        elif str[i] == 'W':
            alpha[22] += 1
        elif str[i] == 'X':
            alpha[23] += 1
        elif str[i] == 'Y':
            alpha[24] += 1
        elif str[i] == 'Z':
            alpha[25] += 1
    print(alpha)
    max_value = max(alpha)
    max_index = alpha.index(max_value)
    if(max_index == 0):
        print('A is the most repeated')
    if(max_index == 1):
        print('B is the most repeated')
    if(max_index == 2):
        print('C is the most repeated')
    if(max_index == 3):
        print('D is the most repeated')
    if(max_index == 4):
        print('E is the most repeated')
    if(max_index == 5):
        print('F is the most repeated')
    if(max_index == 6):
        print('G is the most repeated')
    if(max_index == 7):
        print('H is the most repeated')
    if(max_index == 8):
        print('I is the most repeated')
    if(max_index == 9):
        print('J is the most repeated')
    if(max_index == 10):
        print('K is the most repeated')
    if(max_index == 11):
        print('L is the most repeated')
    if(max_index == 12):
        print('M is the most repeated')
    if(max_index == 13):
        print('N is the most repeated')
    if(max_index == 14):
        print('O is the most repeated')
    if(max_index == 15):
        print('P is the most repeated')
    if(max_index == 16):
        print('Q is the most repeated')
    if(max_index == 17):
        print('R is the most repeated')
    if(max_index == 18):
        print('S is the most repeated')
    if(max_index == 19):
        print('T is the most repeated')
    if(max_index == 20):
        print('U is the most repeated')
    if(max_index == 21):
        print('V is the most repeated')
    if(max_index == 22):
        print('W is the most repeated')
    if(max_index == 23):
        print('X is the most repeated')
    if(max_index == 24):
        print('Y is the most repeated')
    if(max_index == 25):
        print('Z is the most repeated')
main()
