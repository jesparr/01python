temp = input('Vill du ange temperaturen i Fahrenheit eller Celsius? Svara F eller C\n').upper() #Ange vilken temp, ".upper" omvandlar svaret till versal

if temp == 'F':
    fahrenheit = int(input('Ange en temperatur i Fahrenheit\n'))
    celsius = (fahrenheit - 32) / 1.8 # Omvandlar svaret till celsius
    if celsius >= 20:
        print(fahrenheit, 'Grader Fahrenheit blir', celsius, 'grader celsius!, packa badkläder')
    if celsius <= 10:
        print(fahrenheit, 'Grader Fahrenheit blir', celsius, 'grader Celsius, ta på dig vinterkläder')
elif temp == 'C':
    celsius = int(input('Ange en temperatur i Celsius:\n'))
    fahrenheit = 1.8 * celsius + 32
    if fahrenheit >= 68:
        print('Det blir', fahrenheit, 'grader fahrenheit!, packa badkläder')
    if fahrenheit <= 68:
        print('Det blir', fahrenheit, 'grader fahrenheit!, ta på dig vinterkläder!')