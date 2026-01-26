tal1 = int(input('Ge mig ett tal\n'))
tal2 = int(input('Ge mig ett tal till\n'))
tal3 = int(input('Ge mig ett tredje tal\n'))

if tal1 > tal2 and tal1 > tal3:
    print(tal1, 'är det största talet')
elif tal2 > tal1 and tal2 > tal3:
    print(tal2, 'är störst')
else:
    print(tal3, 'är det största talet')