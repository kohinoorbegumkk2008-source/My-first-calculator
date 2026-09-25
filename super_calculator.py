print('--- Super Calculator ---')
print('ber hote q likho')

while True:
    hisab = input('\nhisab lekho (jemon 10+20*2): ')
    
    if hisab == 'q':
        print('Allah Hafez!')
        break
    
    try:
        result = eval(hisab)
        print('Result =', result)
    except:
        print('Vul hisab diso bhai, abar try koro')
