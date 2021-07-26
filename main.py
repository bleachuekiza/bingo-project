import random
from time import sleep

number1_15 = []
number16_30 = []
number31_45 = []
number46_60 = []
number61_75 = []
for x in range(75):
    r = x+1
    if r < 16:
        number1_15.append(r)
    elif r < 31:
        number16_30.append(r)
    elif r < 46:
        number31_45.append(r)
    elif r < 61:
        number46_60.append(r)
    elif r < 76:
        number61_75.append(r)


num_table = []
def create_num_table():
    for xnum in range(75):
        num_table.append(xnum+1)


bingo_card = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
    ]
def rm_num_to_card():
    for i in range(25):
        r = i+1
        if r >= 1 and r <= 5:
            randomnumber = random.randint(0, len(number1_15)-1)
            bingo_card[i] = number1_15[randomnumber]
            del number1_15[randomnumber]
        if r >= 6 and r <= 10:
            randomnumber = random.randint(0, len(number16_30)-1)
            bingo_card[i] = number16_30[randomnumber]
            del number16_30[randomnumber]
        if r >= 11 and r <= 15:
            randomnumber = random.randint(0, len(number31_45)-1)
            bingo_card[i] = number31_45[randomnumber]
            del number31_45[randomnumber]
        if r >= 16 and r <= 20:
            randomnumber = random.randint(0, len(number46_60)-1)
            bingo_card[i] = number46_60[randomnumber]
            del number46_60[randomnumber]
        if r >= 21 and r <= 25:
            randomnumber = random.randint(0, len(number61_75)-1)
            bingo_card[i] = number61_75[randomnumber]
            del number61_75[randomnumber]
    bingo_card[12] = 'X'

def show_table():
    print('{:^28}'.format('BINGO GAME'))
    print('|-----------------------------|')
    print('|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(bingo_card[0], bingo_card[5], bingo_card[10], bingo_card[15], bingo_card[20]))
    print('|-----------------------------|')
    print('|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(bingo_card[1], bingo_card[6], bingo_card[11], bingo_card[16], bingo_card[21]))
    print('|-----------------------------|')
    print('|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(bingo_card[2], bingo_card[7], bingo_card[12], bingo_card[17], bingo_card[22]))
    print('|-----------------------------|')
    print('|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(bingo_card[3], bingo_card[8], bingo_card[13], bingo_card[18], bingo_card[23]))
    print('|-----------------------------|')
    print('|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(bingo_card[4], bingo_card[9], bingo_card[14], bingo_card[19], bingo_card[24]))
    print('|-----------------------------|')

def check_bingo():
    # Check vertical
    if bingo_card[0] == 'X' and bingo_card[1] == 'X' and bingo_card[2] == 'X' and bingo_card[3] == 'X' and bingo_card[4] == 'X' or bingo_card[5] == 'X' and bingo_card[6] == 'X' and bingo_card[7] == 'X' and bingo_card[8] == 'X' and bingo_card[9] == 'X' or bingo_card[10] == 'X' and bingo_card[11] == 'X' and bingo_card[12] == 'X' and bingo_card[13] == 'X' and bingo_card[14] == 'X' or bingo_card[15] == 'X' and bingo_card[16] == 'X' and bingo_card[17] == 'X' and bingo_card[18] == 'X' and bingo_card[19] == 'X' or bingo_card[20] == 'X' and bingo_card[21] == 'X' and bingo_card[22] == 'X' and bingo_card[23] == 'X' and bingo_card[24] == 'X':
        sleep(1)
        print('Bingo!!!')
        print('You Win!')
        exit()
    # Check horizontal
    elif bingo_card[0] == 'X' and bingo_card[5] == 'X' and bingo_card[10] == 'X' and bingo_card[15] == 'X' and bingo_card[20] == 'X' or bingo_card[1] == 'X' and bingo_card[6] == 'X' and bingo_card[11] == 'X' and bingo_card[16] == 'X' and bingo_card[21] == 'X' or bingo_card[2] == 'X' and bingo_card[7] == 'X' and bingo_card[12] == 'X' and bingo_card[17] == 'X' and bingo_card[22] == 'X' or bingo_card[3] == 'X' and bingo_card[8] == 'X' and bingo_card[13] == 'X' and bingo_card[18] == 'X' and bingo_card[23] == 'X' or bingo_card[4] == 'X' and bingo_card[9] == 'X' and bingo_card[14] == 'X' and bingo_card[19] == 'X' and bingo_card[24] == 'X':
        sleep(1)
        print('Bingo!!!')
        print('You Win!')
        exit()
    # Check oblique
    elif bingo_card[0] == 'X' and bingo_card[6] == 'X' and bingo_card[12] == 'X' and bingo_card[18] == 'X' and bingo_card[24] == 'X' or bingo_card[20] == 'X' and bingo_card[16] == 'X' and bingo_card[12] == 'X' and bingo_card[8] == 'X' and bingo_card[4]:
        sleep(1)
        print('Bingo!!!')
        print('You Win!')
        exit()
    else:
        random_num()

def random_num():
    input('Input Anykey to continue')
    rnum = random.randint(0, len(num_table)-1)
    print('Number Random : ', num_table[rnum])
    # show_table()
    del num_table[rnum]
    for xi in range(25):
        if bingo_card[xi] == rnum:
            bingo_card[xi] = 'X'
            print('Find : ', rnum)
            sleep(1)
            show_table()
            check_bingo()
    random_num()

if __name__ == "__main__":
    create_num_table()
    rm_num_to_card()
    show_table()
    random_num()