

def fantasy_file_writer(year, fantasy_site, team):
    roster_dict = dict()
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

    write_roster(year, fantasy_site, roster_dict)

def write_roster(year, fantasy_site, _dict):
    with open('roster_{}_{}'.format(year, fantasy_site), 'w') as fh:
        for k, v in _dict:
            fh.write('{}: {}'.format(k, v))

            


 