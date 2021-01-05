import pandas as pd 

def fantasy_file_writer(year, fantasy_site, team):
    fh = open('roster_{}_{}'.format(year, fantasy_site), 'w')
    team_df = pd.DataFrame()
    if fantasy_site == "DraftKings":
        roster_dict = {'PG': , 'SG': , 'SF': , 'PF': , 'C': }
    elif fantasy_site == "ESPN":
        roster_dict = {'PG': , 'SG': , 'SF': , 'PF': , 'C': , 'G': , 'F': , 'UTIL': }
    elif fantasy_site == "Yahoo":
        roster_dict = {'PG': , 'SG': , 'SF': , 'PF': , 'C': }
    else:
        import os
        os.remove('roster_{}_{}'.format(year, fantasy_site))
        print("Entered fantasy format currently not supported")


 