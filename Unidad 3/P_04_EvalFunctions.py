'''
    Notacion Infija:
        3 + 5

    Notacion Prefija:
        + 3 5

    Notacino Postfija:
        3 5 +

'''

infija = '3 + 5 / 8 * 2'
prefija = '+ 3 5'
postfija = '3 5 +'

r1 = eval(infija)

print(r1)
