import turtle

import time
import os



m=0
s=0

water=0

coffee=0

bloom=0


clear = lambda: os.system('cls')
brkln = lambda: print ("=============================")
clear()

print ("Lex's totally not nerdy \nCoffee Calculator!")
brkln()
print ("\nLet's make a V60 \n ")

water = float(input("How many mugs of coffee do you want?"))

water = water*300

coffee = water/16

print ("========COFFEE RECIPE========")
print ("\nUse", coffee, "g of coffee and ", water," mls of water")

time.sleep(2)

brkln()
print ("\nLet's get started")

time.sleep(1)

print ("\nRinse your V60 paper with hot water and discard the water")

time.sleep(1)
print ("Grind your coffee to a med-fine consistency")

time.sleep(1)

print ("\nPour your ground coffee into the filter and we're ready to start")

time.sleep(1)

input("\nPress enter to continue")

time.sleep(1)

clear()
s = s+1

bloom=coffee*2

print ("Start off by pouring about", bloom , "g of hot water onto the bed and pausing for 30 seconds\n ")

print ("\nStart in 3")

time.sleep(1)

print ("2")

time.sleep(1)

print ("1")

time.sleep(1)

print ("Go!")

print ("\nLetting it bloom will help more flavour develop in the brew\n")

s=0

while s<30:

  s = s+1

  print ("Bloom time:", s
)
  time.sleep(1)
  
  if s==20:

    water = (water-bloom)/3

    print ("Get ready to pour on about 1/3 of the remaining water in 10 seconds (", water, "g of water)\n"
)
if s==30:

  print ("\nIt's time to pour", water, "grams of water onto the coffee\n"
)
while s<60:

  print ("Next pour of water in ", 60-s, "seconds"
)
  time.sleep(5)

  s = s+5

if s==60:

  print ("\nNow pour another ", water, "grams of water into the brewer\n ")

  m = m+1
while s<90:

  print ("Next pour of water in ", 90-s, "seconds")
  time.sleep(5)

  s = s+5

if s==90:

  print ("\nOk it's time to pour the last ", water, "grams of water\n "
)
time.sleep(2)

s = s+2

print ("\nWith all the water in, just give it a gentle stir with a spoon")

time.sleep(2)

s = s+2

print ("\nThis will keep coffee in the brew for longer")

time.sleep(1)

s = s+1

print ("\nNow it should just be a case of waiting. \nThe goal time is about 2 minutes 15 seconds or 135 seconds\n")

while s<210:

  print ("Total Brew time:", m , ":", (s-(m*60
)))
  s=s+5

  time.sleep(5)
  if s == ((m+1)*60):
    m = m+1
  if s==135:

    print ("\nThe last few drops should be coming through now\n ")

  if s==210:

    print ("\nIf your coffee is still brewing, try a courser grind next time\n ")

print ("\nThanks for brewing coffee with me!\n \nCopyright The Coffee Vagabond 2019")