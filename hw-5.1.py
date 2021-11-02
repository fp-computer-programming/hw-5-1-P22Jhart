#question 1

import random

print(random.randint(30,50))

random.seed (1)

print(random.randrange(30,50))

#question 2



number_even=(random.randint(2,75))*2
print(number_even)
random.seed (0)

print(random.randrange(2,75))



#question 3



number_odd=(random.randint(20,30))*2+1
print(number_odd)
random.seed (4)

print(random.randrange(20,30))

#question 4

dice_roll=(random.randint(0,8))
print(dice_roll)
random.seed (2)

print(random.randrange(0,8))

#question 5

dice_roll=(random.randint(0,20))
print(dice_roll)
random.seed (2)

print(random.randrange(0,20))

#question 6

print(random.randrange('cat', 'dog', 'sheep', 'cow', 'chicken', 'pig'))

#question 7





#question 8






#question 9

cards = '(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52)'

random.shuffle(cards)

print(cards)
