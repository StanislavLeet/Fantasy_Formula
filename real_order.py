Q_Bahrain_order = ['M. Verstappen', 'L. Hamilton', 
                   'V. Bottas', 'C. Leclerc',
                   'P. Gasly', 'D. Riccardo', 
                   'L. Norris', 'C. Saintz J.', 
                   'F. Alonso', 'L. Stroll',
                   
                   
                   'S. Perez', 'A. Giovinazzi',
                   'Y. Tsunoda', 'K. Raikkonen', 
                   'G. Russel', 'E. Ocon', 
                   'N. Latifi', 'S. Vettel',
                   'M. Schumacher', 'N. Mazepin']

Q_Bahrain_dnf = [False for i in range(20)]
Q_Bahrain_disq = [False for i in range(20)]
Q_Bahrain = [Q_Bahrain_order, Q_Bahrain_dnf, Q_Bahrain_disq]


R_Bahrain_order = ['L. Hamilton', 'M. Verstappen',
                   'V. Bottas', 'L. Norris', 
                   'S. Perez', 'C. Leclerc',
                   'D. Riccardo', 'C. Saintz J.', 
                   'Y. Tsunoda', 'L. Stroll',
                  
                   'K. Raikkonen', 'A. Giovinazzi',
                   'E. Ocon', 'G. Russel', 
                   'S. Vettel', 'M. Schumacher',
                   'P. Gasly', 'N. Latifi',
                   'F. Alonso', 'N. Mazepin']


R_Bahrain_dnf = [False for i in range(16)]
R_Bahrain_dnf += [True, True, True, True]
R_Bahrain_disq = [False for i in range(20)]
Fast_lap = 'V. Bottas'

R_Bahrain = [R_Bahrain_order, R_Bahrain_dnf, 
             R_Bahrain_disq, Fast_lap]


streak_q_drivers = [0 for i in range(20)]
streak_r_drivers = [0 for i in range(20)]
streak_q_teams = [0 for i in range(10)]
streak_r_teams = [0 for i in range(10)]

S_Bahrain = [streak_q_drivers, streak_r_drivers,
           streak_q_teams, streak_r_teams]



######################################################################

Q_Imola_order = ['L. Hamilton', 'S. Perez', 
                 'M. Verstappen', 'C. Leclerc',
                 'P. Gasly', 'D. Riccardo', 
                 'L. Norris', 'V. Bottas', 
                 'E. Ocon', 'L. Stroll',
                   
                   
                 'C. Saintz J.', 'G. Russel', 
                 'S. Vettel', 'N. Latifi', 
                 'F. Alonso', 'K. Raikkonen',
                 'A. Giovinazzi', 'M. Schumacher',
                 'N. Mazepin', 'Y. Tsunoda']


Q_Imola_dnf = [False for i in range(20)]
Q_Imola_dnf[-1] = True
Q_Imola_disq = [False for i in range(20)]
Q_Imola = [Q_Imola_order, Q_Imola_dnf, Q_Imola_disq]

R_Imola_order = ['M. Verstappen', 'L. Hamilton',
                 'L. Norris', 'C. Leclerc', 
                 'C. Saintz J.', 'D. Riccardo',
                 'P. Gasly', 'L. Stroll', 
                 'E. Ocon', 'F. Alonso',
                 
                 
                 'S. Perez', 'Y. Tsunoda',
                 'K. Raikkonen', 'A. Giovinazzi',
                 'S. Vettel', 'M. Schumacher',
                 'N. Mazepin', 'V. Bottas',
                 'G. Russel', 'N. Latifi']


R_Imola_dnf = [False for i in range(17)]
R_Imola_dnf += [True, True, True]
R_Imola_disq = [False for i in range(20)]
Fast_lap = 'L. Hamilton'

R_Imola = [R_Imola_order, R_Imola_dnf, 
             R_Imola_disq, Fast_lap]


streak_q_drivers = [0 for i in range(20)]
streak_r_drivers = [0 for i in range(20)]
streak_q_teams = [0 for i in range(10)]
streak_r_teams = [0 for i in range(10)]

S_Imola = [streak_q_drivers, streak_r_drivers,
           streak_q_teams, streak_r_teams]



######################################################################

Q_Portugal_order = ['V. Bottas', 'L. Hamilton',
                    'M. Verstappen', 'S. Perez',
                    'C. Saintz J.', 'E. Ocon', 
                    'L. Norris', 'C. Leclerc',
                    'P. Gasly', 'S. Vettel',
                    
                    
                    'G. Russel', 'A. Giovinazzi',
                    'F. Alonso', 'Y. Tsunoda',
                    'K. Raikkonen', 'D. Riccardo',
                    'L. Stroll', 'N. Latifi',
                    'M. Schumacher', 'N. Mazepin']




Q_Portugal_dnf = [False for i in range(20)]
Q_Portugal_disq = [False for i in range(20)]
Q_Portugal = [Q_Portugal_order, 
              Q_Portugal_dnf, 
              Q_Portugal_disq]


R_Portugal_order = ['L. Hamilton', 'M. Verstappen', 
                    'V. Bottas', 'S. Perez',
                    'L. Norris', 'C. Leclerc', 
                    'E. Ocon', 'F. Alonso',
                    'D. Riccardo', 'P. Gasly',
                   
                    'C. Saintz J.', 'A. Giovinazzi',
                    'S. Vettel', 'L. Stroll',
                    'Y. Tsunoda', 'G. Russel',
                    'M. Schumacher', 'N. Latifi',
                    'N. Mazepin', 'K. Raikkonen']


R_Portugal_dnf = [False for i in range(20)]
R_Portugal_dnf[-1] = True
R_Portugal_disq = [False for i in range(20)]
Fast_lap = 'V. Bottas'

R_Portugal = [R_Portugal_order, R_Portugal_dnf, 
              R_Portugal_disq, Fast_lap]


streak_q_drivers = [0 for i in range(20)]
streak_r_drivers = [0 for i in range(20)]
streak_q_teams = [0 for i in range(10)]
streak_q_teams[0] = 2
streak_r_teams = [0 for i in range(10)]
streak_r_teams[3] = 2

S_Portugal = [streak_q_drivers, streak_r_drivers,
              streak_q_teams, streak_r_teams]



######################################################################

Q_Spain_order = ['L. Hamilton', 'M. Verstappen',
                 'V. Bottas', 'C. Leclerc', 
                 'E. Ocon', 'C. Saintz J.',
                 'D. Riccardo', 'S. Perez',
                 'L. Norris', 'F. Alonso',
                
                 'L. Stroll', 'P. Gasly',
                 'S. Vettel', 'A. Giovinazzi',
                 'G. Russel', 'Y. Tsunoda',
                 'K. Raikkonen', 'M. Schumacher',
                 'N. Latifi',  'N. Mazepin']

Q_Spain_dnf = [False for i in range(20)]
Q_Spain_disq = [False for i in range(20)]
Q_Spain = [Q_Spain_order, 
           Q_Spain_dnf, 
           Q_Spain_disq]

R_Spain_order = ['L. Hamilton', 'M. Verstappen', 
                 'V. Bottas', 'C. Leclerc', 
                 'S. Perez', 'D. Riccardo',
                 'C. Saintz J.', 'L. Norris', 
                 'E. Ocon',  'P. Gasly',
                
                 'L. Stroll', 'K. Raikkonen',
                 'S. Vettel', 'G. Russel',
                 'A. Giovinazzi', 'N. Latifi',
                 'F. Alonso', 'M. Schumacher',
                 'N. Mazepin', 'Y. Tsunoda']


R_Spain_dnf = [False for i in range(20)]
R_Spain_dnf[-1] = True
R_Spain_disq = [False for i in range(20)]
Fast_lap = 'M. Verstappen'

R_Spain = [R_Spain_order, R_Spain_dnf, 
           R_Spain_disq, Fast_lap]


streak_q_drivers = [0 for i in range(20)]
streak_r_drivers = [0 for i in range(20)]
streak_q_teams = [0 for i in range(10)]
streak_r_teams = [0 for i in range(10)]

streak_q_drivers[1] = 2

S_Spain = [streak_q_drivers, streak_r_drivers,
           streak_q_teams, streak_r_teams]



######################################################################


Q_Monaco_order = []

Q_Monaco_dnf = [False for i in range(20)]
Q_Monaco_disq = [False for i in range(20)]
Q_Monaco = [Q_Monaco_order, 
            Q_Monaco_dnf, 
            Q_Monaco_disq]

R_Monaco_order = []


R_Monaco_dnf = [False for i in range(20)]
R_Monaco_disq = [False for i in range(20)]
Fast_lap = ''

R_Monaco = [R_Monaco_order, R_Monaco_dnf, 
           R_Monaco_disq, Fast_lap]


streak_q_drivers = [0 for i in range(20)]
streak_r_drivers = [0 for i in range(20)]
streak_q_teams = [0 for i in range(10)]
streak_r_teams = [0 for i in range(10)]


S_Monaco = [streak_q_drivers, streak_r_drivers,
            streak_q_teams, streak_r_teams]
