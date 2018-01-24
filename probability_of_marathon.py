#!/usr/bin/env python

from random import randint

#dices = {1: 4, 2: 6, 3: 8, 4: 10, 5: 12, 6: 20}


def die(ns):
	try:

		#for dice in dices:
		#	print '%d) %02d sided die' % (dice, dices[dice])
		#use = input('\n>>> ')
		num = randint(1, ns)
		return num
        #return num
	except:
		return '\nOops, try again!'


# ??? Put in rolling the raven

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
throws = 10000
print '\nD&D Dice Roller: throws = ' + str(throws)



while count < throws:
  #  print ' Roll # ' + str(count)

    alldice = ''
    count += 1  # This is the same as count = count + 1

    highroll = 0

    total = 0
    ns = 20
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



#print ' ==== \n **Marathon occured < 90 : ' + str(marathon90) + ' Percentage: ' + str((marathon90 / throws) * 100 ) + ' precent '

#print ' ==== \n **Marathon occured < 10 : ' + str(marathon10)
