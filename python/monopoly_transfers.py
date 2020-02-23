START_BALANCE = 1000
players = {}
groups = {}

#create player
def cp(name):
  players[name] = START_BALANCE

#create group
#player1 and player2 are indexes in the players dict
#cost and rev are floats that sum to one that denote share of cost and rev
#floats bad but rounding doesn't matter here
def cg(name, player1, player2, cost, rev):
  groups[name] = {'player1': player1,
                  'player2': player2, 
                  'cost_percents': cost,
                  'revenue_percents': rev,
  }

#transfer between players
#playerTo can be an index or a group
def t(amt, player_from_index, player_to, to_is_group=False):
  players[player_from_index] -= amt
  if to_is_group:
    players[player_to['player1']] += player_to['revenue_percents'][0] * amt
    players[player_to['player2']] += player_to['revenue_percents'][1] * amt
  else:
    players[player_to] += amt

#change balance of player
#player can be an index or a group
def chg(amt, playerIndex):
  players[playerIndex] -= amt

while True:
  try:
    exec(input())
  except:
    print('ERROR')