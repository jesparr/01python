print('Matchen är över, nu ska vi räkna ut resultatet!')

tottenham_goals = int(input('Hur många mål gjorde Tottenham?\n'))
liverpool_goals = int(input('Hur många mål gjorde Liverpool?\n'))

if tottenham_goals > liverpool_goals:
    goal_diff = tottenham_goals - liverpool_goals # Här räknar vi ut hur många måls skillnad det blev
    print('Tottenham vann med', goal_diff, 'mål') # Lägger sen in den variabeln tillsammans med strängen
elif liverpool_goals > tottenham_goals:
    goal_diff = liverpool_goals - tottenham_goals
    print('Liverpool vann med', goal_diff, 'mål')
else:
    print('Det blev oavgjort!') # Alla andra utfall där inget lag gjorde fler mål än det andra skriver ut att det blev oavgjort

