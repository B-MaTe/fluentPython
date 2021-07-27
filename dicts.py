# tt = (1, 2, (32, 44)) # -1039766173
# tl = (1, 2, [32, 44]) # Unhasable list
# tf = (1, 2, frozenset([30, 40])) # -1323036024

dicta = dict(one=1, two=2, three=3)
dictb = {'one':1,'two':2,'three':3}
dictc = dict(zip(['one','two','three'], [1,2,3]))
dictd = dict([('one', 1), ('two', 2), ('three', 3)])
dicte = dict({'one':1,'two':2,'three':3})
print(dicta == dictb == dictc == dictd == dicte)
