#!/usr/bin/env python

from random import randint


import datetime
import time

# timer for duration, see bottom of code
start_time = time.time()


dices = {1: 4, 2: 6, 3: 8, 4: 12, 5: 20}

target_dice = [00,10, 20, 30, 40,50,60,70,80,90]
# print 'target_dice= ' +  str(target_dice[3])

# just loop outside loop incr. by 10, no need for array / list etc.
# tendices = {10, 20, 30, 40, 50, 60, 70, 80, 90}

def die(ns):
    # more on % and formatting https://docs.python.org/2/tutorial/inputoutput.html
    for dice in dices:
        num = randint(1, ns)
    return num

# ??? no work random.seed()
# ??? Put in rolling the raven

#  for dividing line
div_line = '-' * 14


# Number of throws
throws = 1000
# - - - - - -


alldice = ''
highroll = 0
total = 0
product = 1


marathon10 = 0
marathon20 = 0
marathon30 = 0
marathon40 = 0
marathon50 = 0
marathon60 = 0
marathon70 = 0
marathon80 = 0
marathon90 = 0



count = 0

print div_line
print time.strftime("%c") + ' ** Based on [' + '{:,}'.format(throws) + '] throws of all 5 Platonic Dice.'
print div_line


while count < throws:

    alldice = ''
    product = 1
    total = 0
    count += 1  # This is the same as count = count + 1
    marathon_detected = ""

    roll_string = str(count) + ' Summary: '


    for dice in dices:
        alldice = ''
        n = die(dices[dice])
        total = total + n
        product = product * n
        # This is HOW you can print out the number like 01) then the dice
        # print '%2d) %02d sided dice' % (dice, dices[dice]) + '     showing: ' + str(n) + '  product: ' + '  total: ' + str([total])


        # print '%dd' % (dices[dice]) + ':' +  str(n)
        roll_string = roll_string + '%dd' % (dices[dice]) + ':' +  str(n) + ' '

    # print div_line

    if product <= 90:
        marathon90 = marathon90 + 1
        marathon_detected = ' * Marathon detected <= 90 '

    if product <= 80:
        marathon80 = marathon80 + 1
        marathon_detected = ' * Marathon detected < =80  +++++++++++ '

    if product <= 70:
        marathon_detected = ' * Marathon detected <= 90 '

    if product <= 80:
        marathon_detected = ' * Marathon detected <= 70  +++++++++++ '


    if product <= 60:
        marathon_detected = ' * Marathon detected <= 60 '

    if product <= 50:
        marathon_detected = ' * Marathon detected <= 50  +++++++++++ '


    if product <= 40:
        marathon_detected = ' * Marathon detected <= 40 '

    if product <= 30:
        marathon_detected = ' * Marathon detected <= 30  +++++++++++ '


    if product <= 20:
        marathon_detected = ' * Marathon detected <= 20 '

    if product <= 10:
        marathon_detected = ' * Marathon detected <= 10  +++++++++++ '




    #
    #
    # if product <= 90:
    #     # print '***                                                   Marathon 90 ***  occured, product total dice = ' + str(total)
    #     marathon_detected = ' * Marathon detected < 90 '
    #     marathon90 =  marathon90 + 1
    # else:
    #     marathon_detected = ''
    #
    #
    # if product <= 80:
    #     # print '***                                                   Marathon 90 ***  occured, product total dice = ' + str(total)
    #     marathon_detected = ' * Marathon detected < 80 '
    #     marathon90 =  marathon90 + 1
    # else:
    #     marathon_detected = ''
    #
    # if product <= 70:
    #     # print '***                                                   Marathon 90 ***  occured, product total dice = ' + str(total)
    #     marathon_detected = ' * Marathon detected < 70 '
    #     marathon90 =  marathon90 + 1
    # else:
    #     marathon_detected = ''



    print roll_string + ' ( total: ' + str([total]) + '   product:   ' + str([product]) +')' + marathon_detected

#p = '{:.2%}'

print div_line

print 'Percent for < 90 = ' + '{:.2%}'.format(float(marathon90)/float(throws))
# print div_line

print div_line

# This is way better, easy to adust, shorter, ??? Fix all
#percent = float(marathon90) / float(throws) * 100
#print '\npercent for < 90 = ' + p.format(float(marathon90) / float(throws))








# percent = float(marathon90) / float(throws) * 100
# print '\npercent for < 90 = ' +  str(float(marathon90) / float(throws) * 100) + ' % \n'

count= 0
alldice = ''
highroll = 0
total = 0
product = 1

marathon10 = 0
marathon20 = 0
marathon30 = 0
marathon40 = 0
marathon50 = 0
marathon60 = 0
marathon70 = 0
marathon80 = 0
marathon90 = 0


while count < throws:

    alldice = ''
    count += 1  # This is the same as count = count + 1

    highroll = 0

    total = 0
    product = 1

    n = die(4)
    total = total + n
    product = product * n
    alldice = alldice + ' d4: ' + str(n)


    n = die(6)
    total = total + n
    product = product * n
    alldice = alldice + ' d6: ' + str(n)


    n = die(8)
    total = total + n
    product = product * n
    alldice = alldice +  ' d8: ' + str(n)

    n = die(12)
    total = total + n
    product = product * n
    alldice = alldice + ' d12: ' + str(n)

    n = die(20)
    total = total + n
    product = product * n
    alldice = alldice + ' d20: ' + str(n)

    print  ' > Roll # ' + str(count) + alldice + ' Sum=  ' + str(total) + ' Product =  ' + str(product)





    # print ' ==== \nTotal ' + str(total)

   # print ' ==== \nProduct (all dice multiplied) =  ' + str(product)

   #  print ' ==== \nMax Product ' + str(20 * 12 * 8 * 6 * 4 * 3)



    if product <= 90:
        print '***                                                   Marathon 90 ***  occured, product total dice = ' + str(total)
        marathon90 =  marathon90 + 1


    if product <= 80:
        print '***                                                   Marathon 80 ***  occured, product total dice = ' + str(total)
        marathon80 =  marathon80 + 1


    if product <= 70:
        print '***                                                   Marathon 70 ***  occured, product total dice = ' + str(total)
        marathon70 =  marathon70 + 1

    if product <= 60:
        print '***                                                   Marathon 60 ***  occured, product total dice = ' + str(total)
        marathon60 =  marathon60 + 1

    if product <= 50:
        print '***                                                   Marathon 50 ***  occured, product total dice = ' + str(total)
        marathon50 = marathon50 + 1

    if product <= 40:
        print '***                                                   Marathon 40 ***  occured, product total dice = ' + str(total)
        marathon40 = marathon40 + 1

    if product <= 30:
        print '***                                                   Marathon 30 ***  occured, product total dice = ' + str(total)
        marathon30 = marathon30 + 1

    if product <= 20:
        print '***                                                   Marathon 20 ***  occured, product total dice = ' + str(total)
        marathon20 = marathon20 + 1


    if product <= 10:
        print '***                                                   Marathon 10 ***  occured, product total dice = ' + str(total)
        marathon10 = marathon10 + 1


# percent = float(marathon90) / float(throws) * 100
# print '\npercent for < 90 = ' +  str(float(marathon90) / float(throws) * 100) + ' %'

print '\n Based on ' + '{:,}'.format(throws) + ' throws of all 5 Platonic Dice:'



# {:.2%}'.format(points/total)

p = '{:.2%}'

# This is way better, easy to adust, shorter, ??? Fix all



percent = float(marathon90) / float(throws) * 100
print '\npercent for < 90 = ' + p.format(float(marathon90) / float(throws))


percent = float(marathon90) / float(throws) * 100
print '\npercent for < 90 = ' +  str(float(marathon90) / float(throws) * 100) + ' %'

percent = float(marathon80) / float(throws) * 100
print '\npercent for < 80 = ' +  str(float(marathon80) / float(throws) * 100) + ' %'


percent = float(marathon70) / float(throws) * 100
print '\npercent for < 70 = ' +  str(float(marathon70) / float(throws) * 100) + ' %'


percent = float(marathon60) / float(throws) * 100
print '\npercent for < 60 = ' +  str(float(marathon60) / float(throws) * 100) + ' %'


percent = float(marathon50) / float(throws) * 100
print '\npercent for < 50 = ' +  str(float(marathon50) / float(throws) * 100) + ' %'


percent = float(marathon40) / float(throws) * 100
print '\npercent for < 40 = ' +  str(float(marathon40) / float(throws) * 100) + ' %'


percent = float(marathon30) / float(throws) * 100
print '\npercent for < 30 = ' +  str(float(marathon30) / float(throws) * 100) + ' %'


percent = float(marathon20) / float(throws) * 100
print '\npercent for < 20 = ' +  str(float(marathon20) / float(throws) * 100) + ' %'

percent = float(marathon10) / float(throws) * 100
print '\npercent for < 10 = ' +  str(float(marathon10) / float(throws) * 100) + ' %'



print div_line
#  how long does it take to run ---------------
print('Plato\'s Dice Game Simulation Rolls: ' + '{:,}'.format(throws) +'.  Executed in: %.5f seconds' % (time.time() - start_time))
print div_line
