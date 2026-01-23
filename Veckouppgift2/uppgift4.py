temp = input('Vill du ange temperaturen i Fahrenheit eller Celsius? Svara F eller C\n').upper() #Ange vilken temp, ".upper" omvandlar svaret till versal

if temp == 'F':
    fahrenheit = int(input('Ange en temperatur i Fahrenheit\n'))
    celsius = (fahrenheit - 32) / 1.8 # Omvandlar svaret till celsius
    #celsius = (fahrenheit - 32) * 5/9
    print('Det blir', celsius, 'grader celsius!')
elif temp == 'C':
    celsius = int(input('Ange en temperatur i Celsius:\n'))
    fahrenheit = 1.8 * celsius + 32
    #fahrenheit = (celsius * 9 / 5) + 32
    print('Det blir', fahrenheit, 'grader fahrenheit!')