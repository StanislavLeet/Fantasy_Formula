drivers = ['L. Hamilton', 'M. Verstappen', 'L. Norris', 'C. Leclerc',
           'V. Bottas', 'C. Saintz J.', 'D. Riccardo', 'S. Perez',
           'P. Gasly', 'L. Stroll', 'Y. Tsunoda', 'E. Ocon',
           'F. Alonso', 'K. Raikkonen', 'A. Giovinazzi', 'G. Russel',
           'S. Vettel', 'M. Schumacher', 'N. Mazepin', 'N. Latifi']

teams = ['Mercedes', 'Red Bull', 'Ferrari',
         'McLaren', 'Aston Martin', 'Alpine',
         'AlphaTauri', 'Alfa Romeo', 'Williams',
         'Haas']

basic_drivers = dict()
for driver in drivers:
    basic_drivers[driver] = dict()
    basic_drivers[driver]['score'] = 0.0


basic_drivers['L. Hamilton']['Team'] = 'Mercedes'
basic_drivers['M. Verstappen']['Team'] = 'Red Bull'
basic_drivers['L. Norris']['Team'] = 'McLaren'
basic_drivers['C. Leclerc']['Team'] = 'Ferrari'
basic_drivers['V. Bottas']['Team'] = 'Mercedes'


basic_drivers['C. Saintz J.']['Team'] = 'Ferrari'
basic_drivers['D. Riccardo']['Team'] = 'McLaren'
basic_drivers['S. Perez']['Team'] = 'Red Bull'
basic_drivers['P. Gasly']['Team'] = 'AlphaTauri'
basic_drivers['L. Stroll']['Team'] = 'Aston Martin'


basic_drivers['Y. Tsunoda']['Team'] = 'AlphaTauri'
basic_drivers['E. Ocon']['Team'] = 'Alpine'
basic_drivers['F. Alonso']['Team'] = 'Alpine'
basic_drivers['K. Raikkonen']['Team'] = 'Alfa Romeo'
basic_drivers['A. Giovinazzi']['Team'] = 'Alfa Romeo'


basic_drivers['G. Russel']['Team'] = 'Williams'
basic_drivers['S. Vettel']['Team'] = 'Aston Martin'
basic_drivers['M. Schumacher']['Team'] = 'Haas'
basic_drivers['N. Mazepin']['Team'] = 'Haas'
basic_drivers['N. Latifi']['Team'] = 'Williams'


basic_team = dict()
for team in teams:
    basic_team[team] = dict()
    basic_team[team]['score'] = 0.0


basic_team['Mercedes']['drivers'] = ['L. Hamilton', 'V. Bottas']
basic_team['Red Bull']['drivers'] = ['M. Verstappen', 'S. Perez']
basic_team['Ferrari']['drivers'] = ['C. Leclerc', 'C. Saintz J.']
basic_team['McLaren']['drivers'] = ['L. Norris', 'D. Riccardo']
basic_team['Aston Martin']['drivers'] = ['L. Stroll', 'S. Vettel']


basic_team['Alpine']['drivers'] = ['E. Ocon', 'F. Alonso']
basic_team['AlphaTauri']['drivers'] = ['P. Gasly', 'Y. Tsunoda']
basic_team['Alfa Romeo']['drivers'] = ['K. Raikkonen', 'A. Giovinazzi']
basic_team['Williams']['drivers'] = ['G. Russel', 'N. Latifi']
basic_team['Haas']['drivers'] = ['M. Schumacher', 'N. Mazepin']


basic_drivers['L. Hamilton']['cost'] = 33.4
basic_drivers['M. Verstappen']['cost'] = 25.2
basic_drivers['L. Norris']['cost'] = 13.5
basic_drivers['C. Leclerc']['cost'] = 17.6
basic_drivers['V. Bottas']['cost'] = 23.4


basic_drivers['C. Saintz J.']['cost'] = 14.3
basic_drivers['D. Riccardo']['cost'] = 16.6
basic_drivers['S. Perez']['cost'] = 18.4
basic_drivers['P. Gasly']['cost'] = 11.7
basic_drivers['L. Stroll']['cost'] = 13.6


basic_drivers['Y. Tsunoda']['cost'] = 9.4
basic_drivers['E. Ocon']['cost'] = 9.7
basic_drivers['F. Alonso']['cost'] = 15.1
basic_drivers['K. Raikkonen']['cost'] = 9.4
basic_drivers['A. Giovinazzi']['cost'] = 7.8


basic_drivers['G. Russel']['cost'] = 6.2
basic_drivers['S. Vettel']['cost'] = 15.3
basic_drivers['M. Schumacher']['cost'] = 5.7
basic_drivers['N. Mazepin']['cost'] = 5.3
basic_drivers['N. Latifi']['cost'] = 6.5



basic_team['Mercedes']['cost'] = 37.7
basic_team['Red Bull']['cost'] = 26.1
basic_team['Ferrari']['cost'] = 18.8
basic_team['McLaren']['cost'] = 18.7
basic_team['Aston Martin']['cost'] = 16.8


basic_team['Alpine']['cost'] = 15.0
basic_team['AlphaTauri']['cost'] = 13.2
basic_team['Alfa Romeo']['cost'] = 8.9
basic_team['Williams']['cost'] = 6.3
basic_team['Haas']['cost'] = 6.1

