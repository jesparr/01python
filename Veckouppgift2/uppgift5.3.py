tal1 = int(input('Ge mig ett tal\n'))
tal2 = int(input('Ge mig ett tal till\n'))
tal3 = int(input('Ge mig ett tredje tal\n'))

if tal1 == tal2 and tal3:
    print('Alla tre talen är samma')
elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
    print('Två av talen är samma')
else:
    print('Inga tal är samma')