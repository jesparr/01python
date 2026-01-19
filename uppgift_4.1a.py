speed = int(input('Hur många km/h ska du köra?\n'))

distance = 470

timmar = distance / speed
minuter = timmar * 60


print(f'Det kommer ta {timmar} timmar till Stockholm')
print(f'I minuter blir det {minuter}')

heltalsdivision = int(timmar // 1)
modulo = int((timmar % 1) * 60)

print(f'Resan tar {heltalsdivision} timmar och {modulo} minuter')



