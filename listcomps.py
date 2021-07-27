cards = [str(card) for card in range(2, 11)] + list('JQKA')
#print(cards)

symbols = '$#!()&'
tup = tuple(ord(symbol) for symbol in symbols)
#print(tup)

import array

arr = array.array('I', (ord(symbol) for symbol in symbols))
#print(arr)

colors = ['white', 'black']
sizes = ['s', 'm', 'l', 'xs', 'xl', 'xxs', 'xxl']
for tshirt in ('%s, %s' % (s, c) for c in colors for s in sizes):
    #print(tshirt)
