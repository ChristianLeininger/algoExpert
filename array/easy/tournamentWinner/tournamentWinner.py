# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 24.05.2023

# -----------------------------------------------------------------------------
# time O(n) and space O(k) k number of teams and n number of competitions

def tournamentWinner(competitions, results):
    """ calculate the winner of the tournament
    given a list of competitions and a list of results  
    :param: list[list[str]] competitions
    :param: list[int] results
    :return: str winner
    """
    teams = {}
    for game, res,  in zip(competitions, results):
        if game[0] not in teams:
            teams.update({game[0]:0})
        if game[1] not in teams:
            teams.update({game[1]:0})
        if res == 1:
            teams[game[0]] +=3
        if res == 0:
            teams[game[1]] +=3
    
    return  max(teams, key=lambda k: teams[k])
