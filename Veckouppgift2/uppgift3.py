print('Matchen är över, nu ska vi räkna ut resultatet!')

tottenham = int(input('Hur många mål gjorde Tottenham?\n'))
liverpool = int(input('Hur många mål gjorde Liverpool?\n'))

if tottenham > liverpool:
    print('Tottenham vann')
elif liverpool > tottenham:
    print('Liverpool vann')
else:
    print('Det blev oavgjort!')

