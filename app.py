from constants import PLAYERS
from constants import TEAMS
import copy
import random

my_list = []
last_dictionary = {}
my_collection = []
def clean_data():
    global my_list
    global last_dictionary
    global my_collection
    my_dictionary = {}

    my_collection = copy.deepcopy(PLAYERS)
    for dictionary in my_collection:
        my_dictionary['name'] = dictionary['name']
        my_dictionary['guardians'] = dictionary['guardians']        
        if dictionary['experience'] == "YES":
            my_dictionary['experience'] = True
        else:
            my_dictionary['experience'] = False
        my_dictionary['height'] = int(dictionary['height'].split()[0])
        last_dictionary = my_dictionary.copy()
        my_list.append(last_dictionary)
#    print(my_list)


clean_data()


def balance_teams():
    players_in_team = []
    
    num_players_team = int(len(my_list) / len(TEAMS))
    my_teams = copy.deepcopy(TEAMS)
    actual_team_list = my_teams
#    teams_num = input('Plese select an option to select the Team A: {}'.format())
    for team in my_teams:
#        team_index = my_teams.index(team)
#        team = actual_team_list[team_index]
        print(team)

        for player in my_list :
            random_index = random.randint(0, len(my_list) - 1)
            random_player = my_list[random_index]
#            if (len(my_list) > 0):
            if len(players_in_team) < 6:
                print(random_player)
                players_in_team.append(random_player)
                my_list.remove(random_player)
#            print(player)
                
                    
                    
                    
                
    print(num_players_team)
#    print(players_in_team)
#    print(random_player)
#    print(player)
    print(players_in_team)


balance_teams()
















#if __name__ == "__main__": 
# here comes the call of functions.